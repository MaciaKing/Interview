<?php


include 'database.php';


$fun=$_POST['dat']; // this param is used to know what function to call


if($fun=="getHeroes"){
    // Crear una instancia de la clase ConexionPG
    $conexion = new DatabasePG('localhost', 5432, 'marvel', 'macia', 'macia');

    // Ejecutar una consulta SELECT
    $resultados = $conexion->ejecutarConsulta('SELECT * FROM hero');
    echo json_encode($resultados);
}


?>