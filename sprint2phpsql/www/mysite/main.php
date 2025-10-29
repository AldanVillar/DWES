<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "mysitedb";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Consulta de todos los libros
    $stmt = $conn->query("SELECT * FROM tLibros");
    $libros = $stmt->fetchAll(PDO::FETCH_ASSOC);

} catch(PDOException $e) {
    die("❌ Error de conexión: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Catálogo de Libros</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: #f8f8f8;
        margin: 0;
        padding: 20px;
    }
    h1 {
        text-align: center;
        color: #333;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }
    .card {
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        padding: 15px;
        text-align: center;
    }
    img {
        width: 150px;
        height: 200px;
        object-fit: cover;
        border-radius: 5px;
    }
    a {
        display: inline-block;
        margin-top: 10px;
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
    }
    a:hover {
        text-decoration: underline;
    }
</style>
</head>
<body>
<h1>Catálogo de Libros</h1>

<div class="grid">
<?php foreach($libros as $libro): ?>
    <div class="card">
        <img src="<?= htmlspecialchars($libro['imagen']) ?>" alt="Portada">
        <h3><?= htmlspecialchars($libro['titulo']) ?></h3>
        <p><strong>Autor:</strong> <?= htmlspecialchars($libro['autor']) ?></p>
        <p><?= htmlspecialchars($libro['descripcion']) ?></p>
        <a href="detail.php?id=<?= $libro['id'] ?>">Ver detalles</a>
    </div>
<?php endforeach; ?>
</div>

</body>
</html>


