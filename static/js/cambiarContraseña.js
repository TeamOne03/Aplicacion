// Selecciona el formulario de cambio de contraseña por su ID
const passwordForm = document.getElementById('passwordForm');

// Agrega un evento de escucha para el evento 'submit' del formulario
passwordForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const contrasenaActual = document.getElementById('contrasenaActual').value;
    const nuevaContrasena = document.getElementById('nuevaContrasena').value;
    const confirmarContrasena = document.getElementById('confirmarContrasena').value;
    const messageElement = document.getElementById('message');

    // Limpiar mensajes anteriores
    messageElement.textContent = '';
    messageElement.className = '';

    // Para validar longitud de la nueva contraseña
    if (nuevaContrasena.length < 8) {
        messageElement.textContent = 'La nueva contraseña debe tener al menos 8 caracteres.';
        messageElement.className = 'error';
        return;
    }

    // Para validar coincidencia de contraseñas
    if (nuevaContrasena !== confirmarContrasena) {
        messageElement.textContent = 'Las contraseñas no coinciden.';
        messageElement.className = 'error';
        return;
    }

    // Obtiene los usuarios almacenados en el almacenamiento local
    const Users = JSON.parse(localStorage.getItem('users')) || [];

    // Supone que el usuario está logueado y se conoce su email
    const correo = 'usuario@example.com'; 
    const user = Users.find(user => user.email === correo);

    if (!user) {
        messageElement.textContent = 'Usuario no encontrado.';
        messageElement.className = 'error';
        return;
    }

    // Validar que la contraseña actual sea correcta
    if (user.password !== contrasenaActual) {
        messageElement.textContent = 'La contraseña actual no es correcta.';
        messageElement.className = 'error';
        return;
    }

    // Validar que la nueva contraseña sea diferente de la actual
    if (nuevaContrasena === contrasenaActual) {
        messageElement.textContent = 'La nueva contraseña no puede ser igual a la contraseña actual.';
        messageElement.className = 'error';
        return;
    }

    // Actualizar la contraseña del usuario
    user.password = nuevaContrasena;
    localStorage.setItem('users', JSON.stringify(Users));

    // Si todas las validaciones pasan
    messageElement.textContent = 'La contraseña ha sido cambiada exitosamente.';
    messageElement.className = 'success';

    // Redirige al usuario o muestra un mensaje de éxito
    setTimeout(() => {
        window.location.href = 'inicioSesion.html';
    }, 2000);
});
