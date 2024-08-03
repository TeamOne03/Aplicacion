function abrirVentana() {
    var modal = document.getElementById("modal");
    modal.style.display = "flex";
}

function cerrarVentana() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}

function subirFoto() {
    var inputFile = document.getElementById("inputArchivo");
    var file = inputFile.files[0];
    
    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var imagenPerfil = document.getElementById("imagenPerfil");
            imagenPerfil.src = e.target.result;
            cerrarVentana();
        }
        reader.readAsDataURL(file);
    }
}