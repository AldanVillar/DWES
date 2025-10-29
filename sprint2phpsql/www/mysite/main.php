<?php
$host = "localhost";
$user = "root";
$password = "1234";
$dbname = "mysitedb";

try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "✅ Conexión exitosa a la base de datos '$dbname'";
} catch (PDOException $e) {
    echo "❌ Error de conexión: " . $e->getMessage();
}
?>

