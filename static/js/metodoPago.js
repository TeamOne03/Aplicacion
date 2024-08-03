document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.formaPago');
    const numTarjetaInput = document.getElementById('numTarjeta');
    const añosSelect = document.getElementById('años');

    // Rellenar select de años
    const currentYear = new Date().getFullYear();
    for (let i = currentYear; i < currentYear + 10; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        añosSelect.appendChild(option);
    }

    // Formatear número de tarjeta
    numTarjetaInput.addEventListener('input', function(event) {
        let value = event.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
        let formattedValue = '';
        for (let i = 0; i < value.length; i++) {
            if (i > 0 && i % 4 === 0) {
                formattedValue += ' ';
            }
            formattedValue += value[i];
        }
        event.target.value = formattedValue;
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const nombre = document.getElementById('nombre').value;
        let numTarjeta = document.getElementById('numTarjeta').value.replace(/\s+/g, '');
        const mesExpiracion = document.getElementById('meses').value;
        const añoExpiracion = document.getElementById('años').value;
        const cvv = document.getElementById('cvv').value;

        if (numTarjeta.length !== 16) {
            alert('El número de la tarjeta debe tener 16 dígitos.');
            return;
        }

        // Validar si es Visa o MasterCard
        const firstDigit = numTarjeta.charAt(0);
        if (!(firstDigit === '4' || (firstDigit >= '5' && firstDigit <= '5'))) {
            alert('El número de tarjeta debe ser Visa o MasterCard.');
            return;
        }

        const tarjeta = {
            nombre,
            numTarjeta,
            mesExpiracion,
            añoExpiracion,
            cvv
        };

        // Guardar en localStorage
        let tarjetas = JSON.parse(localStorage.getItem('tarjetas')) || [];
        tarjetas.push(tarjeta);
        localStorage.setItem('tarjetas', JSON.stringify(tarjetas));

        alert('Tarjeta agregada con éxito');
        window.location.href = 'procedePago';
    });
});