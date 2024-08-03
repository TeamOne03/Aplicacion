document.addEventListener('DOMContentLoaded', function() {
    // Obtener totalFinal desde sessionStorage
    const totalFinal = sessionStorage.getItem('totalFinal');
    if (totalFinal) {
        document.getElementById('presioTotal').textContent = `RD$${totalFinal}`;
    }

    // Obtener número de tarjeta y URL de la imagen desde sessionStorage
    const numeroTarjeta = sessionStorage.getItem('numeroTarjeta');
    const urlImagen = sessionStorage.getItem('urlImagen');

    if (numeroTarjeta && urlImagen) {
        const ultimosCuatro = numeroTarjeta.slice(-4); // Obtener los últimos 4 dígitos
        document.getElementById('numero-tarjeta').textContent = `**** ${ultimosCuatro}`;
        document.getElementById('imagen-tarjeta').src = urlImagen;
    }
});
