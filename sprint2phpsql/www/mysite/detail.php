<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "mysitedb";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Obtener ID desde la URL
    $id = isset($_GET['id']) ? intval($_GET['id']) : 0;

    // Obtener datos del libro
    $stmt = $conn->prepare("SELECT * FROM tLibros WHERE id = ?");
    $stmt->execute([$id]);
    $libro = $stmt->fetch(PDO::FETCH_ASSOC);

    // Obtener comentarios asociados
    $stmt2 = $conn->prepare("SELECT * FROM tComentarios WHERE id_libro = ? ORDER BY fecha DESC");
    $stmt2->execute([$id]);
    $comentarios = $stmt2->fetchAll(PDO::FETCH_ASSOC);

} catch(PDOException $e) {
    die("❌ Error: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title><?= htmlspecialchars($libro['titulo']) ?></title>
<style>
    body { font-family: Arial, sans-serif; margin: 30px; background: #fafafa; }
    img { width: 200px; height: 260px; object-fit: cover; border-radius: 6px; }
    .comentario { background: white; padding: 10px; border-radius: 8px; margin-top: 10px; }
    .fecha { color: gray; font-size: 0.9em; }
</style>
</head>
<body>

<a href="main.php">&larr; Volver al listado</a>

<h1><?= htmlspecialchars($libro['titulo']) ?></h1>
<img src="<?= htmlspecialchars($libro['imagen']) ?>" alt="Portada">
<p><strong>Autor:</strong> <?= htmlspecialchars($libro['autor']) ?></p>
<p><?= htmlspecialchars($libro['descripcion']) ?></p>

<h2>Comentarios</h2>
<?php if (count($comentarios) > 0): ?>
    <?php foreach ($comentarios as $comentario): ?>
        <div class="comentario">
            <p><strong><?= htmlspecialchars($comentario['usuario']) ?>:</strong> <?= htmlspecialchars($comentario['comentario']) ?></p>
            <p class="fecha"><?= htmlspecialchars($comentario['fecha']) ?></p>
        </div>
    <?php endforeach; ?>
<?php else: ?>
    <p>No hay comentarios todavía.</p>
<?php endif; ?>

</body>
</html>
