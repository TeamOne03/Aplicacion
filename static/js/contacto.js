function Send(){
    var name = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var mensaje = document.getElementById('mensaje').value;

    var body = "nombre:" + name + "<br/> email:" + email + "<br/> telefono :" + telefono + "<br/>"

    console.log(body);
    // Email.send({
    // Host : "smtp.elasticemail.com",
    // Username : "jardineriahernandez3@gmail.com",
    // Password : "DADD835B9A6C2384459FF31BA5E17874EBC2",
    // To : 'jardineriahernandez3@gmail.com',
    // From : "jardineriahernandez3@gmail.com",
    // Subject : "This is the subject",
    // Body : "And this is the body"
    // }).then(
    //     message => alert(message)
    //     );

    
}