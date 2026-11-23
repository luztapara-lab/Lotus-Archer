
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template_string("""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Lotus Archer</title>

<style>
body {
    margin: 0;
    min-height: 100vh;
    background: radial-gradient(circle, #54234e, #160d27);
    color: #ffe5ee;
    font-family: Georgia, serif;
    text-align: center;
    padding: 30px 15px;
    box-sizing: border-box;
}

h1 {
    color: #ffb6d0;
    font-size: 38px;
}

.subtitulo {
    color: #f7d7e8;
    font-style: italic;
}

.loto {
    font-size: 110px;
    margin: 20px;
    animation: flotar 3s infinite ease-in-out;
    filter: drop-shadow(0 0 20px #ff91c5);
}

@keyframes flotar {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.carta {
    max-width: 520px;
    margin: auto;
    padding: 25px;
    border: 1px solid #ffb6d0;
    border-radius: 25px;
    background: #ffffff12;
    box-shadow: 0 0 25px #ff91c544;
    line-height: 1.9;
}

.poema {
    white-space: pre-line;
    font-size: 17px;
}

.firma {
    color: #ffb6d0;
    font-style: italic;
    margin-top: 25px;
}

</style>
</head>

<body>

<h1>Lotus Archer</h1>

<p class="subtitulo">
Un alma entre flores y estrellas ♐
</p>

<div class="loto">🪷</div>

<div class="carta">

<p class="poema" id="mensaje"></p>

<p class="firma">
Con admiración, entre flores y estrellas. 🌷
</p>

</div>

<script>
const poema = `Hay personas que parecen llevar fuego en el alma,
que nacieron para explorar, soñar y perseguir sus destinos.

Tú eres como Sagitario,
un arquero que apunta hacia sus sueños
sin miedo a descubrir nuevos caminos.

Tienes algo de flor de loto,
porque incluso ante las dificultades
encuentras la manera de seguir creciendo.

Admiro tu pasión y tu manera de ser,
esa libertad que acompaña tus pasos.

Y hay dos detalles que tienen un encanto especial:
tus ojos, que podrían contar historias sin palabras,
y tu sonrisa, capaz de iluminar un instante sencillo.

Que tus flechas siempre encuentren sus sueños,
que tus raíces nunca olviden su fortaleza
y que tu alma nunca deje de florecer.`;

let i = 0;

function escribir() {
    if (i < poema.length) {
        document.getElementById("mensaje").textContent += poema[i];
        i++;
        setTimeout(escribir, 45);
    }
}

escribir();
</script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(debug=True)
