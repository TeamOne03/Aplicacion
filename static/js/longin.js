// Selecciona el formulario de inicio de sesión por su ID
const iniciosesion_form = document.querySelector('#iniciosesion_form');

// Agrega un evento de escucha para el evento 'submit' del formulario
iniciosesion_form.addEventListener('submit', (e) => {
    e.preventDefault(); // Previene el comportamiento predeterminado de enviar el formulario

    // Obtiene el valor del campo de correo electrónico
    const correo = document.querySelector('#correo').value;

    // Obtiene el valor del campo de contraseña
    const pass = document.querySelector('#pass').value;

    // Obtiene los usuarios almacenados en el almacenamiento local o inicializa un array vacío si no hay ninguno
    const Users = JSON.parse(localStorage.getItem('users')) || [];

    // Busca un usuario en el array de usuarios que coincida con el correo electrónico y la contraseña ingresados
    const validUser = Users.find(user => user.email === correo && user.password === pass);

    // Si no se encuentra ningún usuario válido, muestra un mensaje de alerta y detiene el proceso
    if (!validUser) {
        return alert('Usuario y/o contraseña incorrectos!');
    }

    // Si se encuentra un usuario válido, muestra un mensaje de bienvenida con el nombre del usuario
    alert(`Bienvenido ${validUser.name}`);

    // Guarda los detalles del usuario en el almacenamiento local
    localStorage.setItem('login_success', JSON.stringify(validUser));

    // Redirige al usuario a la página de inicio
    window.location.href = 'index.html';
});


function myFuntion(){
    var x = document.getElementById("pass");
    var y = document.getElementById("ocultar");
    var z = document.getElementById("ocultar2");

    if(x.type === 'password'){
        x.type = "text";
        y.style.display = "block";
        z.style.display = "none";
    }
    else{
        x.type = "password";
        y.style.display = "none";
        z.style.display = "block";
    }
}



// Selecciona el formulario de cambio de contraseña por su ID
const formCambiarContrasena = document.querySelector('#formCambiar-contrasena');

// Agrega un evento de escucha para el evento 'submit' del formulario
formCambiarContrasena.addEventListener('submit', function(event) {
    event.preventDefault(); // Previene el comportamiento predeterminado de enviar el formulario

    // Obtiene los valores de los campos
    const contrasenaActual = document.getElementById('contrasenaActual').value;
    const nuevaContrasena = document.getElementById('nuevaContrasena').value;
    const confirmarContrasena = document.getElementById('confirmarContrasena').value;
    const mensajeElemento = document.getElementById('mensaje');

    // Limpia mensajes anteriores
    mensajeElemento.textContent = '';

    // Validaciones
    if (nuevaContrasena.length < 8) {
        mensajeElemento.textContent = 'La nueva contraseña debe tener al menos 8 caracteres.';
        mensajeElemento.className = 'error';
        return;
    }

    if (nuevaContrasena !== confirmarContrasena) {
        mensajeElemento.textContent = 'Las contraseñas no coinciden.';
        mensajeElemento.className = 'error';
        return;
    }

    if (nuevaContrasena === contrasenaActual) {
        mensajeElemento.textContent = 'La nueva contraseña no puede ser igual a la contraseña actual.';
        mensajeElemento.className = 'error';
        return;
    }

    // Simulación de cambio de contraseña exitoso
    mensajeElemento.textContent = 'Contraseña cambiada exitosamente.';
    mensajeElemento.className = 'success';

    // Aquí podrías enviar el formulario al servidor si fuera necesario
    // formCambiarContrasena.submit();
});
