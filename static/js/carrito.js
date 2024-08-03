document.addEventListener("DOMContentLoaded", function() {
    const añadiralcarritoBtn = document.getElementById('añadiralcarritoBtn');
    const procederPagoLink = document.getElementById('procederPagoLink'); // Enlace "Proceder al Pago"

    // Agregar un listener al botón de agregar al carrito
    if (añadiralcarritoBtn) {
        añadiralcarritoBtn.addEventListener('click', function() {
            // Obtener la información del producto específico
            const producto = {
                nombre: this.closest('.cuadro').querySelector('.nombre h2').textContent,
                precio: parseFloat(this.closest('.cuadro').querySelector('.precio p').textContent.replace('Precio: RD$', '').trim()),
                cantidad: parseInt(this.closest('.cuadro').querySelector('#cantidad').value),
                imagen: this.closest('.cuadro').querySelector('.articulo img').getAttribute('src')
            };

            // Obtener el carrito actual desde el localStorage
            let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

            // Verificar si el producto ya está en el carrito
            let productoExistente = carrito.find(item => item.nombre === producto.nombre);

            if (productoExistente) {
                // Si el producto ya existe, incrementar la cantidad
                productoExistente.cantidad += producto.cantidad;
            } else {
                // Si el producto no existe, agregarlo al carrito
                carrito.push(producto);
            }

            // Guardar el carrito actualizado en el localStorage
            localStorage.setItem('carrito', JSON.stringify(carrito));

            // Notificar al usuario
            alert("Producto agregado al carrito");

            // Actualizar el carrito en la interfaz
            actualizarCarrito();
        });
    }

    const carritoContainer = document.getElementById('carritoContainer');
    const articulosSeleccionados = document.getElementById('articulosSeleccionados');
    const totalCarrito = document.getElementById('totalCarrito');
    const totalItebis = document.getElementById('totalItebis');
    const mensajeCarritoVacio = document.getElementById('mensajeCarritoVacio');

    // Obtener el carrito desde el localStorage
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    function actualizarCarrito() {
        carritoContainer.innerHTML = '';
        let totalProductos = 0;
        let totalPrecio = 0;
        let totalItebisCalculado = 0;
        let totalFinal = 0;

        // Mostrar los productos en el carrito
        if (carrito.length === 0) {
            // Mostrar mensaje de carrito vacío
            mensajeCarritoVacio.style.display = 'block';
            articulosSeleccionados.textContent = '0';
            totalCarrito.textContent = 'RD$0.00';
            totalItebis.textContent = 'RD$0.00';
            return; // Salir de la función si el carrito está vacío
        } else {
            mensajeCarritoVacio.style.display = 'none'; // Ocultar mensaje de carrito vacío si no está vacío
        }

        carrito.forEach((producto, index) => {
            const productoRow = document.createElement('tr');
            
            // Calcular el ITBIS para este producto
            const itebis = producto.precio * producto.cantidad * 0.18;
            totalItebisCalculado += itebis;

            productoRow.innerHTML = `
                <td>
                    <a href="#">
                        <div class="ctd-img">
                            <img class="img-carrito" src="${producto.imagen}" alt="${producto.nombre}" style="width: 80px; height: 80px; margin-right: 10px;">
                            ${producto.nombre}
                        </div>
                    </a>
                </td>
                <td>RD$${producto.precio.toFixed(2)}</td>
                <td>
                    <button class="cantidad-btn" data-action="decrease" data-index="${index}">-</button>
                    <span>${producto.cantidad}</span>
                    <button class="cantidad-btn" data-action="increase" data-index="${index}">+</button>
                </td>
                <td>RD$${(producto.precio * producto.cantidad).toFixed(2)}</td>
                <td>RD$${itebis.toFixed(2)}</td>
                <td><button class="eliminar-btn" data-index="${index}"><i class="fas fa-trash"></i></button></td>
            `;

            productoRow.classList.add('producto-row'); // Clase para la fila del producto
            productoRow.querySelector('.ctd-img').classList.add('ctd-img'); // Clase para la imagen del producto

            carritoContainer.appendChild(productoRow);

            // Calcular el total de productos y el precio total
            totalProductos += parseInt(producto.cantidad);
            totalPrecio += (producto.precio * producto.cantidad);
        });

        totalFinal = totalPrecio + totalItebisCalculado + 200;

        // Actualizar los totales en la interfaz
        articulosSeleccionados.textContent = totalProductos;
        totalCarrito.textContent = `RD$${totalFinal.toFixed(2)}`;
        totalItebis.textContent = `RD$${totalItebisCalculado.toFixed(2)}`;
        // Guardar totalFinal en el sessionStorage para ser utilizado en la página de pago
        sessionStorage.setItem('totalFinal', totalFinal.toFixed(2));
    }

    // Función para modificar la cantidad de un producto
    function modificarCantidad(index, action) {
        if (action === 'increase') {
            carrito[index].cantidad++;
        } else if (action === 'decrease' && carrito[index].cantidad > 1) {
            carrito[index].cantidad--;
        }
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    // Añadir eventos a los botones de modificar cantidad
    carritoContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('cantidad-btn')) {
            const action = event.target.getAttribute('data-action');
            const index = parseInt(event.target.getAttribute('data-index'));
            modificarCantidad(index, action);
        }
    });

    // Función para eliminar un producto del carrito
    function eliminarProducto(index) {
        carrito.splice(index, 1);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    // Añadir eventos a los botones de eliminar
    carritoContainer.addEventListener('click', function(event) {
        if (event.target.closest('.eliminar-btn')) {
            const index = parseInt(event.target.closest('.eliminar-btn').getAttribute('data-index'));
            eliminarProducto(index);
        }
    });

    // Prevenir el acceso a la página de pago si el carrito está vacío
    if (procederPagoLink) {
        procederPagoLink.addEventListener('click', function(event) {
            if (carrito.length === 0) {
                event.preventDefault();
                alert("Tu carrito está vacío. No puedes proceder al pago.");
            } else {
                // Crear la factura y guardarla en el localStorage
                const factura = {
                    numeroOrden: Math.floor(Math.random() * 100000), // Generar un número de orden aleatorio
                    fecha: new Date().toLocaleDateString(),
                    hora: new Date().toLocaleTimeString(),
                    productos: carrito,
                    total: parseFloat(sessionStorage.getItem('totalFinal'))
                };
                localStorage.setItem('factura', JSON.stringify(factura));
            }
        });
    }

    // Inicializar la visualización del carrito
    actualizarCarrito();
});