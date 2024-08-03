
function guardarCambios(event) {
    event.preventDefault(); // Evitar que el formulario se envíe
    // Capturar los valores del formulario
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const celular = document.getElementById('celular').value;
    const pais = document.getElementById('pais').value;
    const ciudad = document.getElementById('ciudad').value;
    const sector = document.getElementById('sectores').value;
    const otroSector = document.getElementById('otro_sector').value;
    const calle = document.getElementById('calle').value;
    
    // Mostrar la ubicación en el perfil
    const ubicacionPerfil = document.getElementById('ubicacionPerfil');
    ubicacionPerfil.innerHTML = `
        <h3>Ubicación:</h3>
        <p>${nombre} ${apellido}</p>
        <p>Celular: ${celular}</p>
        <p>País: ${pais}</p>
        <p>Ciudad: ${ciudad}</p>
        <p>Sector: ${sector === 'otro' ? otroSector : sector}</p>
        <p>Calle: ${calle}</p>
    `;
} 

// Obtener referencia al formulario y agregar el evento de submit
const formulario = document.querySelector('.formulario');
formulario.addEventListener('submit', guardarCambios);

