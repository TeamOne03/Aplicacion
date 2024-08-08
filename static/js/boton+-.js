document.addEventListener("DOMContentLoaded", function() {
    var botonDecremento = document.getElementById("decremento");
    var botonIncremento = document.getElementById("incremento");
    var cantidadInput = document.getElementById("cantidad");
    var cantidadControl = document.querySelector(".cantidad-control");
    var cantidadDisponible = parseInt(cantidadControl.dataset.cantidadDisponible);

    function actualizarBotones() {
        var valorActual = parseInt(cantidadInput.value);
        botonDecremento.disabled = valorActual <= 1;
        botonIncremento.disabled = valorActual >= cantidadDisponible;
    }

    botonDecremento.addEventListener("click", function() {
        var valorActual = parseInt(cantidadInput.value);
        if (valorActual > 1) {
            cantidadInput.value = valorActual - 1;
            actualizarBotones();
        }
    });

    botonIncremento.addEventListener("click", function() {
        var valorActual = parseInt(cantidadInput.value);
        if (valorActual < cantidadDisponible) {
            cantidadInput.value = valorActual + 1;
            actualizarBotones();
        }
    });

    cantidadInput.addEventListener("change", function() {
        var valorActual = parseInt(cantidadInput.value);
        if (valorActual < 1) {
            cantidadInput.value = 1;
        } else if (valorActual > cantidadDisponible) {
            cantidadInput.value = cantidadDisponible;
        }
        actualizarBotones();
    });

    actualizarBotones();

    // Modificar el evento de añadir al carrito
    var añadirAlCarritoBtn = document.getElementById("añadiralcarritoBtn");
    añadirAlCarritoBtn.addEventListener("click", function() {
        var cantidadSeleccionada = parseInt(cantidadInput.value);
        if (cantidadSeleccionada > cantidadDisponible) {
            alert("No hay suficiente stock disponible. Por favor, seleccione una cantidad menor.");
            return;
        }
        // Aquí va tu lógica para añadir al carrito
    });
});