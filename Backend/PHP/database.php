<?php

class DatabasePG {
    private $conexion;
  
    public function __construct($host, $port, $dbname, $user, $password) {
      $dsn = "pgsql:host=$host;port=$port;dbname=$dbname;user=$user;password=$password";
  
      try {
        $this->conexion = new PDO($dsn);
        $this->conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      } catch (PDOException $e) {
        echo 'Error al conectarse a la base de datos: ' . $e->getMessage();
        die();
      }
    }
  
    public function ejecutarConsulta($consulta) {
      try {
        $stmt = $this->conexion->query($consulta);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
      } catch (PDOException $e) {
        echo 'Error al ejecutar consulta: ' . $e->getMessage();
        die();
      }
    }
  }

?>
  