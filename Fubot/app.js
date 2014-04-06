var express = require("express");
var fbgraph = require("fbgraph");
var http = require("http");
var path = require("path");
var fs = require('fs');
var notify = require('node-notifier');

var app = express();

app.configure(function(){
	app.use(express.bodyParser());
	app.use(express.methodOverride());
	app.use(app.router);
	app.use(express.static(path.join(__dirname,"./public")));
	app.set("port", process.env.PORT || 3000);
});

var configs = require("./config/config.json");

fbgraph.setAccessToken(configs.AccessToken);

/*
var query = {result : "SELECT message_id, viewer_id,  body FROM message WHERE thread_id = 310061185776886 LIMIT 100,200"};
querys = ["select thread_id,message_count from thread where viewer_id = me() and folder_id = 0","select attachment, author_id, body, created_time, message_id, source, thread_id, viewer_id FROM message WHERE thread_id = 266956406748639 LIMIT 0,40"
"",]
*/

var query_start = {result : "SELECT thread_id from thread WHERE folder_id = 0"}

/* This writes the thread_id of messages in a file*/
var p = function(){
fbgraph.fql(query_start, function(err, res){
	var t = res.data[0].fql_result_set;
	var total = t.length;
	var THREAD_ID = '';
	for(var i=0;i<total;i++)
	THREAD_ID = THREAD_ID + t[i]["thread_id"] + '\n';
	
	fs.writeFile("./public/thread_id.json", THREAD_ID, function(err) {
		if(err) {
			console.log(err);
		} else {
			console.log("thread_id's are successfully written in file ./public/thread_id.json");
		}
		});
	});
}

var unseen_msg = function(){
	fbgraph.fql("SELECT thread_id, unread, originator FROM thread WHERE folder_id=0 AND unseen=1", function(err, res){
		var total = res["data"].length;
		var i = 0;
		var unread = 0;
		while(i<total)
		{
			var so;
			unread = res["data"][i]["unread"];  //defaq always remains the last result obtained.
			var thread_id_ = res["data"][i]["thread_id"];
			console.log(unread);
			/*
			var sender = res["data"][i]["originator"];
		    fbgraph.get('/'+sender, function(err2,res2){
				console.log(res2["first_name"]);
				so = res2["first_name"];
				fs.writeFile("./public/sender", so, function(err){});
			});
			*/
			var t = function GET_MSG(unread,thread_id_){
				fbgraph.fql("SELECT body, author_id FROM message WHERE thread_id="+thread_id_, function(err1, res1){
					//console.log(res1["data"][0]);
					var total_msg = res1["data"].length;
					for(var j=total_msg-unread;j<total_msg;j++)
					{
						//console.log(j);
						var msg = res1["data"][j]["body"];
						var author_id = res1["data"][j]["author_id"];
						/*
						console.log(msg);
						console.log(author_id);
						*/
						var Author_ = function(msg,author_id){
							fbgraph.get("/"+author_id, function(err3,res3){
							//console.log(unread);
							console.log(res3["first_name"]);
							console.log(msg);
							notify.notify({title: res3["first_name"],message: msg});
							});
						}
						Author_(msg,author_id);
						/*
						fs.readFile('./public/sender', 'utf8', function (err,data){
							notify.notify({title: data,message: msg});
						});
						*/
					}
				});
			}
			t(unread,thread_id_);
		i += 1;
		}
	});
}

/* Reads file(containing thread-id) and fetches messages */
var q = function(){
	var message_thread_id = [];
	fs.readFile('./public/thread_id.json', 'utf8', function (err,data) {
	if (err){
	return console.log(err);
	}
	message_thread_id = data.split('\n');
	console.log(message_thread_id);
	});
}

var poke = function(){
	var poked_by = '';
	fbgraph.get("/me/pokes",function(err,data) {
	var total = data["data"].length;
    for(var i=0;i<total;i++)
    poked_by = poked_by + data["data"][i]["from"]["id"] + '\n';
	fs.writeFile("./public/pokes.txt", poked_by, function(err) {
	if(err) {
		console.log(err);
	} else {
		console.log("pokers are successfully written in file ./public/pokes.txt");
	}
	});
    }
);
}

var notifications = function(){
	fbgraph.get("me?fields=notifications",function(err,data){
	var total = data["notifications"]["data"].length;
	for(var i=0;i<total;i++)
	notify.notify({
	title: 'Fubot',
    message: data["notifications"]["data"][i]["title"]
		});
	});
}

//p();
//poke();
//notifications();
unseen_msg();

app.get("/", function(req,res){
	res.send(" responses and counting..");
});

http.createServer(app).listen((process.env.PORT || 3000), function(){
	console.log("Express server running on port " + app.get("port"));
});

