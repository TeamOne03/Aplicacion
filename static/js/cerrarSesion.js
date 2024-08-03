document.addEventListener('DOMContentLoaded', (event) => {
    var modal = document.getElementById('logoutModal');
    var logoutLink = document.getElementById('cerrarSesion');
    var span = document.getElementsByClassName('closeBtn')[0];
    var confirmBtn = document.getElementById('confirmBtn');
    var cancelBtn = document.getElementById('cancelBtn');

    logoutLink.onclick = function(event) {
        event.preventDefault();
        modal.style.display = 'block';
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    cancelBtn.onclick = function() {
        modal.style.display = 'none';
    }

    confirmBtn.onclick = function() {
    sessionStorage.removeItem('loggedIn'); // Eliminar el estado de sesión
    // Redirigir al usuario a la página de inicio de sesión
    window.location.href = '/templates/sitio/inicioSesion.html';
};

};

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});

