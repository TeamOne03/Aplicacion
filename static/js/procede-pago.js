document.addEventListener('DOMContentLoaded', function() {
    const detallesPago = document.querySelector('.detalles-pago');

    // Obtener tarjetas del servidor
    fetch('/obtenerTarjetas', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(tarjetas => {
        if (tarjetas.length === 0) {
            detallesPago.innerHTML = '<p>No hay tarjetas agregadas.</p>';
        } else {
            tarjetas.forEach((tarjeta, index) => {
                const tarjetaDiv = document.createElement('div');
                tarjetaDiv.className = 'opcion-pago';

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.className = 'circulo-checkbox';
                checkbox.id = `checkbox-${index}`;

                const label = document.createElement('label');
                label.htmlFor = `checkbox-${index}`;

                const infoTarjeta = document.createElement('div');
                infoTarjeta.className = 'info-tarjeta';

                const logoTarjeta = document.createElement('p');
                logoTarjeta.className = 'logo-tarjeta';
                const logoImg = document.createElement('img');
                
                // Verificar el tipo de tarjeta y asignar la imagen correspondiente
                if (tarjeta.numTarjeta.startsWith('4')) {
                    logoImg.src = 'static/img/visarp.svg'; // Visa
                } else {
                    logoImg.src = 'static/img/MasterCard_Logo.svg.png'; // MasterCard u otro
                }
                logoTarjeta.appendChild(logoImg);

                const numTarjeta = document.createElement('p');
                numTarjeta.className = 'numero-tarjeta';
                numTarjeta.textContent = `**** ${tarjeta.numTarjeta.slice(-4)}`;
                numTarjeta.setAttribute('data-numero', tarjeta.numTarjeta);

                const expiracion = document.createElement('p');
                expiracion.className = 'expiracion';
                expiracion.textContent = `EXP ${tarjeta.mesExpiracion}/${tarjeta.añoExpiracion}`;

                const deleteButton = document.createElement('button');
                const deleteIcon = document.createElement('i');
                deleteIcon.className = 'fas fa-trash';
                deleteButton.className = 'eliminar-btn';
                deleteButton.setAttribute('data-id', tarjeta.idTarjeta);
                deleteButton.appendChild(deleteIcon);
                deleteButton.addEventListener('click', function() {
                    eliminarTarjeta(tarjeta.idTarjeta); // Enviar ID de la tarjeta para eliminar
                });

                infoTarjeta.appendChild(logoTarjeta);
                infoTarjeta.appendChild(numTarjeta);
                infoTarjeta.appendChild(expiracion);

                tarjetaDiv.appendChild(checkbox);
                tarjetaDiv.appendChild(label);
                tarjetaDiv.appendChild(infoTarjeta);
                tarjetaDiv.appendChild(deleteButton);

                detallesPago.appendChild(tarjetaDiv);

                // Asegurarse de que solo un checkbox pueda estar seleccionado a la vez
                checkbox.addEventListener('change', function() {
                    document.querySelectorAll('.circulo-checkbox').forEach(cb => {
                        if (cb !== checkbox) cb.checked = false;
                    });
                });
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        detallesPago.innerHTML = '<p>Hubo un problema al cargar las tarjetas.</p>';
    });

    document.getElementById('siguiente-btn').addEventListener('click', function(event) {
        const checkboxes = document.querySelectorAll('.circulo-checkbox');
        let selectedCheckbox = null;

        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                selectedCheckbox = checkbox;
            }
        });

        if (!selectedCheckbox) {
            alert('Por favor, selecciona al menos una opción de método de pago.');
            event.preventDefault(); // Evita que el botón haga lo que normalmente haría
        } else {
            const infoTarjeta = selectedCheckbox.nextElementSibling.nextElementSibling;
            const numeroTarjeta = infoTarjeta.querySelector('.numero-tarjeta').getAttribute('data-numero');
            const urlImagen = infoTarjeta.querySelector('.logo-tarjeta img').src;

            sessionStorage.setItem('numeroTarjeta', numeroTarjeta);
            sessionStorage.setItem('urlImagen', urlImagen);
            window.location.href = 'metodoPago';
        }
    });
});

function eliminarTarjeta(idTarjeta) {
    fetch('/eliminarTarjeta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ idTarjeta })
    })
    .then(response => {
        if (response.ok) {
            // Tarjeta eliminada exitosamente, recargar la página
            location.reload();
        } else {
            throw new Error('Error al eliminar la tarjeta.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un problema al eliminar la tarjeta.');
    });
}
