// Selecciona el formulario de registro por su ID
const registro_form = document.querySelector('#registro_form');

// Agrega un evento de escucha para el evento 'submit' del formulario
registro_form.addEventListener('submit', (e) => {
    e.preventDefault(); // Previene el comportamiento predeterminado de enviar el formulario

    // Obtiene el valor del campo de nombre y apellido
    const nom = document.querySelector('#nom').value;

    const ape = document.querySelector('#ape').value;

    // Obtiene el valor del campo de correo electrónico
    const correo = document.querySelector('#correo').value;

    // Obtiene el valor del campo de contraseña
    const passw = document.querySelector('#passw').value;

    // Obtiene el valor del campo de confirmar contraseña
    const confirmPassw = document.querySelector('#confirm_passw').value;

    // Para validar que las contraseñas coincidan
    if (passw !== confirmPassw) {
        return alert('Las contraseñas no coinciden.');
    }

    // Para validar la longitud de la contraseña
    if (passw.length < 8) {
        return alert('La contraseña debe tener al menos 8 caracteres.');
    }

    // Obtiene los usuarios almacenados en el almacenamiento local o inicializa un array vacío si no hay ninguno
    const Users = JSON.parse(localStorage.getItem('users')) || [];

    // Busca si el usuario ya está registrado mediante su correo electrónico
    const isUserRegistered = Users.find(user => user.email === correo);

    // Si el usuario ya está registrado, muestra un mensaje de alerta y detiene el proceso
    if (isUserRegistered) {
        return alert('El Usuario ya está registrado.');
    }

    // Agrega un nuevo usuario al array de usuarios con los datos ingresados
    Users.push({ name: nom, email: correo, password: passw });

    // Guarda los detalles del usuario en el almacenamiento local
    localStorage.setItem('users', JSON.stringify(Users));

    // Muestra un mensaje de alerta indicando que el registro fue exitoso
    alert('Registro Exitoso!');

    // Redirige al usuario a la página de inicio de sesión
    window.location.href = 'inicioSesion.html';
});
