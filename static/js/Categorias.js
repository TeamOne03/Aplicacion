document.addEventListener("DOMContentLoaded", function() {
var dropdownToggle = document.querySelector(".desplegable-desplasado"); /* toma la informacion de el menu para poder desplegarlo */
var dropdownMenu = document.querySelector(".desplegable-menu");

dropdownToggle.addEventListener("click", function() { /* este es el codigo para hacer que se despliegue */ 
    if (dropdownMenu.style.display === "none") {
    dropdownMenu.style.display = "block";
    } else {
    dropdownMenu.style.display = "none";
    }
});
});

const categoryLinks = document.querySelectorAll('.desplegable-menu a');
const products = document.querySelectorAll('.M-producto');

categoryLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const category = this.getAttribute('data-category');

        products.forEach(product => {
            if (category === 'all' || product.getAttribute('data-category') === category) {
                product.style.display = 'block';
            } else {
                product.style.display = 'none';
            }
        });
    });
});