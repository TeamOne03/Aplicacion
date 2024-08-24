// document.addEventListener('DOMContentLoaded', () => {
//     const urlParams = new URLSearchParams(window.location.search);
//     const selectedService = urlParams.get('servicio');
//     const preciorecive = urlParams.get('precio');
//     let total = 0;

//     if (selectedService) {
//         document.getElementById('proyecto').value = selectedService;

//         const checkboxes = document.querySelectorAll('#servicios-adicionales input[type="checkbox"]');
//         checkboxes.forEach(checkbox => {
//             if (checkbox.value === selectedService) {
//                 checkbox.parentElement.style.display = 'none';
//             }
//         });
//     }

//     const form = document.getElementById('cotizacionForm');
//     form.addEventListener('submit', (e) => {
//         // Cálculo final del total antes de enviar
//         actualizarTotal();
//         document.getElementById('total').value = total;

//         // El formulario se enviará normalmente ahora
//     });

//     const checkboxes = document.querySelectorAll('#servicios-adicionales input[type="checkbox"]');
//     checkboxes.forEach(checkbox => {
//         checkbox.addEventListener('change', () => {
//             actualizarTotal();
//         });
//     });

//     function actualizarTotal() {
//         const precioInicial = parseFloat(preciorecive) || 0;
//         total = precioInicial;

//         checkboxes.forEach(checkbox => {
//             if (checkbox.checked) {
//                 const precio = parseFloat(checkbox.getAttribute('data-precio')) || 0;
//                 total += precio;
//             }
//         });
//     }

//     actualizarTotal();
// });


document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const selectedService = urlParams.get('servicio');
    const precioRecibe = urlParams.get('precio');
    let total = 0;

    if (selectedService) {
        document.getElementById('proyecto').value = selectedService;
        const checkboxes = document.querySelectorAll('#servicios-adicionales input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            if (checkbox.value === selectedService) {
                checkbox.parentElement.style.display = 'none';
            }
        });
    }

    const form = document.getElementById('cotizacionForm');
    form.addEventListener('submit', (e) => {
        // Cálculo final del total antes de enviar
        actualizarTotal();
        document.getElementById('total').value = total;

        // Guardar servicios adicionales en el campo oculto
        const serviciosAdicionales = [];
        document.querySelectorAll('#servicios-adicionales input[type="checkbox"]:checked').forEach(checkbox => {
            serviciosAdicionales.push(checkbox.value);
        });
        document.getElementById('servicios_adicionales').value = serviciosAdicionales.join(',');

        // El formulario se enviará normalmente ahora
    });

    const checkboxes = document.querySelectorAll('#servicios-adicionales input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            actualizarTotal();
        });
    });

    function actualizarTotal() {
        const precioInicial = parseFloat(precioRecibe) || 0;
        total = precioInicial;

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                const precio = parseFloat(checkbox.getAttribute('data-precio')) || 0;
                total += precio;
            }
        });
    }

    actualizarTotal();
});
