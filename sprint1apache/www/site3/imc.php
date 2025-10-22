<?php
function calcular_imc($peso, $altura) {
    // Fórmula del IMC = peso / (altura^2)
    return $peso / ($altura * $altura);
}

// Comprobamos si los parámetros están definidos
if (isset($_GET['peso']) && isset($_GET['altura'])) {
    $peso = floatval($_GET['peso']);
    $altura = floatval($_GET['altura']);
    $imc = calcular_imc($peso, $altura);

    echo "<!DOCTYPE html>";
    echo "<html lang='es'>";
    echo "<head><meta charset='UTF-8'><title>Calculadora IMC</title></head>";
    echo "<body style='font-family: Arial; margin: 40px;'>";
    echo "<h1>Calculadora de IMC</h1>";
    echo "<p>Peso: $peso kg</p>";
    echo "<p>Altura: $altura m</p>";
    echo "<p><strong>Tu IMC es: " . number_format($imc, 2) . "</strong></p>";

    if ($imc < 18.5) {
        echo "<p style='color: blue;'>Bajo peso</p>";
    } elseif ($imc >= 18.5 && $imc <= 24.9) {
        echo "<p style='color: green;'>Peso normal</p>";
    } else {
        echo "<p style='color: red;'>Sobrepeso</p>";
    }

    echo "</body></html>";
} else {
    echo "<!DOCTYPE html>";
    echo "<html lang='es'>";
    echo "<head><meta charset='UTF-8'><title>Calculadora IMC</title></head>";
    echo "<body style='font-family: Arial; margin: 40px;'>";
    echo "<h1>Calculadora de IMC</h1>";
    echo "<p>Por favor, introduce los parámetros en la URL, por ejemplo:</p>";
    echo "<code>imc.php?peso=70&altura=1.75</code>";
    echo "</body></html>";
}
?>
