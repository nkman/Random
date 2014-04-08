<html>
<head>
<meta title="finding" author="nkman" content="nkman" />
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
     left:450px;
    }
</style>
</head>
<body>
<div align="center"><a href="index.html"><img src="sea.png"></a></div>
<h1>FOUND</h1>
<?php
$host = "localhost";
$user = "569421";
$pass = "kasabisdead1994";
$db = "569421";


$connection = mysql_connect($host,$user,$pass) or dir ("unable to connect!! problem with internet");
mysql_select_db($db) or die ("unable to select database !!!");

$a = $_POST["batch"];

$query= "SELECT * FROM men WHERE Batch = '$a' ";

$result = mysql_query($query) or die ("query is wrong sir !!!");

echo "<div class=lok>";
if(mysql_num_rows($result)>0){
echo "<table border=2 width=800><tr><th>Name</th><th>Branch</th><th>Batch</th><th>Phone_No</th><th>Address</th></tr>";

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
 echo "<h1>";
 echo "no such men found !!!";
 echo "</h1>";
}
echo "</div>";
mysql_free_result($result);

mysql_close($connection);
?>


</body>
</html>
  