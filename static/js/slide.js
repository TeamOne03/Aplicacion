let slideIndex = 0;
slide();

function slide() {
    let slides = document.getElementsByClassName("efecto");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex - 1].style.display = "block";  
    setTimeout(slide, 5000); // Change image every 5 seconds
}
