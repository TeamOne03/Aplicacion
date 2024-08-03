// Recuperar el total final del sessionStorage
const totalFinal = sessionStorage.getItem('totalFinal');
// Mostrar el total final en el elemento correspondiente
document.getElementById('importePagado').textContent = `RD$${totalFinal}`;

// Recuperar el número de tarjeta del sessionStorage
const numeroTarjeta = sessionStorage.getItem('numeroTarjeta');
// Mostrar el número de tarjeta en el elemento correspondiente
document.getElementById('numeroTarjeta').textContent = numeroTarjeta ? `**** **** **** ${numeroTarjeta.slice(-4)}` : '**** **** **** 0000';

// Obtener la fecha y hora actual
const currentDate = new Date();
const optionsDate = { year: 'numeric', month: '2-digit', day: '2-digit' };
const optionsTime = { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true };

const formattedDate = currentDate.toLocaleDateString('es-DO', optionsDate);
const formattedTime = currentDate.toLocaleTimeString('es-DO', optionsTime);

// Mostrar la fecha y hora actual en los elementos correspondientes
document.getElementById('currentDate').textContent = formattedDate;
document.getElementById('currentTime').textContent = formattedTime;

document.addEventListener("DOMContentLoaded", function() {
    // Función para finalizar la compra
    function finalizarCompra() {
        // Mostrar alerta de compra exitosa
        alert("Su compra se realizó con éxito");

        // Vaciar el carrito 
        localStorage.removeItem('carrito');

        // devolver a el usuario al catálogo
        window.location.href = "catalogo";
    }

    // Agregar un listener al botón "Continuar"
    const continuarBtn = document.querySelector('.continue-button');
    if (continuarBtn) {
        continuarBtn.addEventListener('click', function(event) {
            event.preventDefault(); 
            finalizarCompra(); // Llamar a la función para finalizar la compra
        });
    }
});