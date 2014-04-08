<html>
<head>
<title>find men</title>
<meta author="nkman" content="nkman"></meta>
<style>
body{
     background: -webkit-linear-gradient(top,#540C0C,#BA8B58);
     color:white;   
 }
h1{
     text-align:center;
     font-color:#FFFFFF;
   }
.damn{
       text-align:center;
       margin-left:auto;
       margin-right:auto;
       color:#FFFFFF;
      }

</style>
</head>
<body>
<div align="center"><a href="index.html"><img src="sea.png"></a></div>
</br>
<h1> submitted </h1></br></br>
</br >
<div class="damn">
<?php
$host = "localhost";
$user = "569421";
$pass = "kasabisdead1994";
$db = "569421db2";


$connection = mysql_connect($host,$user,$pass) or dir ("unable to connect!! problem with internet");
mysql_select_db($db) or die ("unable to select database !!!");

$a = $_POST["name"];
$b = $_POST["branch"];
$c = $_POST["batch"];
$d = $_POST["phone_num"];
$e = $_POST["address"];
$f = $_POST["fb"];




$query= "INSERT INTO `569421db2`.`initial` (`Name`, `Branch`, `Batch`, `Phone_number`, `Facebook`, `Address`) VALUES ('$a ', '$b', '$c', '$d', '$f', '$e')";

$result = mysql_query($query) or die ("query is wrong sir !!!");








mysql_free_result($result);

mysql_close($connection);

















?>

</div>
</body>
</html>	