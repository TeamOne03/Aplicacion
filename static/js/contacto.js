function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "jardineriahernandez@gmail.com",
        Password : "hernandez03.",
        To : 'jardineria@gmail.com',
        From : document.getElementById("email").value,
        Subject : "nuevo contacto formulario consulta ",
        Body : "nombre: " + document.getElementById("nombre").value
        + "<br> Email: " + document.getElementById("email").value
        + "<br> telefono no: " + document.getElementById("telefono").value
        +"<br> Mensaje: " + document.getElementById("mensaje").value
    }).then(
    message => alert("Message sent Succesfully")
    );
}