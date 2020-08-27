# PGN-Parser

Parser de archivos PGN. Dado un archivo con varias partidas de ajedrez, decide si el archivo es sintácticamente válido (superficialmente) y si lo es
devuelve cuál fue la jugada inicial más común del blanco y cuál fue el máximo nivel de anidamiento de los comentarios que contienen alguna partida.

_______________________________________

## Uso:

> python main.py Path/Al/Archivo/PGN

Por ejemplo:
> python main.py ../entradas/validas/entrada1.txt
resulta en
<pre>
La jugada inicial mas popular fue e4, y la maxima profundidad 2
</pre>

_______________________________________

## Créditos:

Este fue un trabajo para la materia Teoría de Lenguajes por Mateo Marenco, Olivia Peretti, Marcos Blufstein y Maximiliano Martino.
