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
.lok{
     position:absolute;
     left:500px;
    }
</style>
</head>
<body>
<div align="center"><a href="index.html"><img src="sea.png"></a></div>
</br>
<h1>Found </h1></br></br>
</br >
<div class="damn">
<?php
$host = "localhost";
$user = "569421";
$pass = "kasabisdead1994";
$db = "569421";


$connection = mysql_connect($host,$user,$pass) or dir ("unable to connect!! problem with internet");
mysql_select_db($db) or die ("unable to select database !!!");

$a=$_POST["name"];

$query= "SELECT * FROM men WHERE Name = '$a' ";

$result = mysql_query($query) or die ("query is wrong sir !!!");

echo "<div class=lok>";
if(mysql_num_rows($result)>0){
echo "<table border=1 width=800><tr><th size=50>"; echo "  Name</th>"; echo "  <th>'  Branch  '</th><th>Batch</th><th>Phone_No</th><th>Address</th></tr>";

while($row = mysql_fetch_row($result))
{
  echo "<tr>";
  for( $i=0;$i<5;$i++)
  echo"<td>$row[$i]</td>";
 
  echo "</tr>";
}
 echo "</table>";

}
else
{
 echo "wrong way man !!!";
}
echo "</div>";
mysql_free_result($result);

mysql_close($connection);

?>

</div>
</body>
</html>		