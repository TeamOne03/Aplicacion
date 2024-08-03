document.querySelector(".form-olvido").addEventListener("submit", function(event) {
    event.preventDefault(); // Previene el comportamiento predeterminado de enviar el formulario

    const email = document.querySelector(".correo-olvi").value;
    let valid = true;

    if (!email || !validateEmail(email)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        valid = false;
    }

    if (valid) {
        // Simulación de envío de correo de recuperación (puedes implementar la lógica real aquí)
        alert("Si el correo está registrado, recibirá un enlace para restablecer su contraseña.");
        // Redirige al usuario a la página de inicio de sesión
        window.location.href = 'inicioSesion.html';
    }
});

// Función para validar el formato del correo electrónico
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
