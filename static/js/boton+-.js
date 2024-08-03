document.addEventListener("DOMContentLoaded", function() {
  var botonDecremento = document.getElementById("decremento"); /*toma la información del botón de decremento*/
  var botonIncremento = document.getElementById("incremento"); /*toma la información del botón de incremento*/
  var cantidadInput = document.getElementById("cantidad"); /*toma la información de la cantidad*/

  botonDecremento.addEventListener("click", function() { 
    var valorActual = parseInt(cantidadInput.value); /* este código es para que cuando se interactúe con el botón de decremento reste uno a la cantidad */
    if (valorActual > 1) {
      cantidadInput.value = valorActual - 1;
    }
  });

  botonIncremento.addEventListener("click", function() {
    var valorActual = parseInt(cantidadInput.value); /* este código es para que cuando se interactúe con el botón de incremento sume uno a la cantidad */
    if (valorActual < 99) { /* este es el límite que puede alcanzar */
      cantidadInput.value = valorActual + 1;
    }
  });
});