function guardar (){
    let user = document.getElementById("usuario").value;
    let pass= document.getElementById("contraseña").value;


if(user=="admin" && pass=="123"){
    window.location="a_administrador.html";
    // alert("Usuario y contraseña introducido correctamnete")
} else {
    if(user=="Juana Almanzar" && pass=="123"){
        window.location="index.html";
        // alert("Usuario y contraseña introducido correctamnete")
    } else {
        swal("Error", "Ingresar tus datos correctos", "error")
    }
}



}