document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario-producto');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault();

        // Obtener los valores del formulario
        const nombre = document.getElementById('nombre').value;
        const precio = document.getElementById('precio').value;
        const imagen = document.getElementById('imagen').files[0];
        const categoria = document.getElementById('categoria').value;

        // Crear el elemento de producto
        const nuevoProducto = document.createElement('div');
        nuevoProducto.classList.add('M-producto');
        nuevoProducto.setAttribute('data-category', categoria);

        const imagenProducto = document.createElement('img');
        imagenProducto.src = URL.createObjectURL(imagen);
        imagenProducto.alt = nombre;

        const nombreProducto = document.createElement('h2');
        nombreProducto.textContent = nombre;

        const precioProducto = document.createElement('p');
        precioProducto.textContent = `$${precio}`;
        precioProducto.classList.add('M-precio-color');

        nuevoProducto.appendChild(imagenProducto);
        nuevoProducto.appendChild(nombreProducto);
        nuevoProducto.appendChild(precioProducto);

        // Botón para eliminar el producto
        const botonEliminar = document.createElement('button');
        botonEliminar.textContent = 'Eliminar';
        botonEliminar.classList.add('M-eliminar-producto');
        nuevoProducto.appendChild(botonEliminar);

        // Agregar el nuevo producto a la sección de productos
        const contenedorProductos = document.querySelector('.M-productos');
        contenedorProductos.appendChild(nuevoProducto);

        // Limpiar el formulario
        formulario.reset();
    });

    // Escuchar eventos de clic en los botones de eliminar producto
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('M-eliminar-producto')) {
            const producto = event.target.closest('.M-producto');
            producto.remove(); // Eliminamos el producto
        }
    });

    // Filtrar productos por categoría
    const enlacesCategorias = document.querySelectorAll('.desplegable-menu a');
    enlacesCategorias.forEach(enlace => {
        enlace.addEventListener('click', function(event) {
            event.preventDefault();

            const categoria = event.target.getAttribute('data-category');
            const productos = document.querySelectorAll('.M-producto');

            productos.forEach(producto => {
                if (categoria === 'all' || producto.getAttribute('data-category') === categoria) {
                    producto.style.display = '';
                } else {
                    producto.style.display = 'none';
                }
            });
        });
    });
});
