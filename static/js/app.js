const menu__horizontal = document.querySelector('.menu__horizontal');
const cierraMenu = document.querySelector('.cierraMenu');
const abreMenu = document.querySelector('.abreMenu');


abreMenu.addEventListener('click',show);
cierraMenu.addEventListener('click',close);

function show(){
    menu__horizontal.style.display = 'flex';
    menu__horizontal.style.top = '0';
}
function close(){
    menu__horizontal.style.top = '100%';
}