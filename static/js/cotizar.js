document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const selectedService = urlParams.get('servicio');
    const preciorecive = urlParams.get('precio');
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
        e.preventDefault();
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            if (!data[key]) {
                data[key] = value;
            } else {
                if (!Array.isArray(data[key])) {
                    data[key] = [data[key]];
                }
                data[key].push(value);
            }
        });

        localStorage.setItem('cotizacionData', JSON.stringify(data));
        localStorage.setItem('total', total);

        window.location.href = '/resultado';
    });

    const checkboxes = document.querySelectorAll('#servicios-adicionales input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            actualizarTotal();
        });
    });

    function actualizarTotal() {
        const precioInicial = parseFloat(preciorecive) || 0;
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
