<?php
include 'database.php';
$fun=$_POST['dat']; // this param is used to know what function to call

if($fun=="getHeroes"){
    // Create a new instance of the class DatabasePG
    $conexion = new DatabasePG('localhost', 5432, 'marvel', 'macia', 'macia');

    // Execute the query and get the results
    $resultados = $conexion->ejecutarConsulta('SELECT * FROM hero');
    echo json_encode($resultados);
}


?>