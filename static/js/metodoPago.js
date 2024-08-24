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

    // Eliminamos la función de agregar tarjeta ya que ahora se maneja desde el backend en Python
});
