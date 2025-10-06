<?php
echo "<!DOCTYPE html>";
echo "<html lang='es'>";
echo "<head>";
echo "<meta charset='UTF-8'>";
echo "<title>Tabla del 7</title>";
echo "</head>";
echo "<body>";
echo "<h1>Tabla de multiplicar del 7</h1>";
echo "<table>";
echo "<tr><th>Operación</th><th>Resultado</th></tr>";

for ($i = 1; $i <= 10; $i++) {
    $resultado = 7 * $i;
    echo "<tr><td>7 x $i</td><td>$resultado</td></tr>";
}

echo "</table>";
echo "</body>";
echo "</html>";
?>
