document.addEventListener("DOMContentLoaded", function() {
    const añadiralcarritoBtn = document.getElementById('añadiralcarritoBtn');
    const procederPagoLink = document.getElementById('procederPagoLink');
    const carritoContainer = document.getElementById('carritoContainer');
    const articulosSeleccionados = document.getElementById('articulosSeleccionados');
    const totalCarrito = document.getElementById('totalCarrito');
    const totalItebis = document.getElementById('totalItebis');
    const mensajeCarritoVacio = document.getElementById('mensajeCarritoVacio');

    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    if (añadiralcarritoBtn) {
        añadiralcarritoBtn.addEventListener('click', function() {
            const producto = {
                nombre: this.closest('.cuadro').querySelector('.nombre h2').textContent,
                precio: parseFloat(this.closest('.cuadro').querySelector('.precio p').textContent.replace('Precio: RD$', '').trim()),
                cantidad: parseInt(this.closest('.cuadro').querySelector('#cantidad').value),
                imagen: this.closest('.cuadro').querySelector('.articulo img').getAttribute('src'),
                cantidadDisponible: parseInt(this.closest('.cuadro').querySelector('.cantidad-control').dataset.cantidadDisponible)
            };

            let productoExistente = carrito.find(item => item.nombre === producto.nombre);

            if (productoExistente) {
                if (productoExistente.cantidad + producto.cantidad <= producto.cantidadDisponible) {
                    productoExistente.cantidad += producto.cantidad;
                } else {
                    productoExistente.cantidad = producto.cantidadDisponible;
                    alert("Se ha alcanzado la cantidad máxima disponible para este producto.");
                }
            } else {
                carrito.push(producto);
            }

            localStorage.setItem('carrito', JSON.stringify(carrito));
            alert("Producto agregado al carrito");
            actualizarCarrito();
        });
    }

    function actualizarCarrito() {
        carritoContainer.innerHTML = '';
        let totalProductos = 0;
        let totalPrecio = 0;
        let totalItebisCalculado = 0;
        let totalFinal = 0;

        if (carrito.length === 0) {
            mensajeCarritoVacio.style.display = 'block';
            articulosSeleccionados.textContent = '0';
            totalCarrito.textContent = 'RD$0.00';
            totalItebis.textContent = 'RD$0.00';
            return;
        } else {
            mensajeCarritoVacio.style.display = 'none';
        }

        carrito.forEach((producto, index) => {
            const productoRow = document.createElement('tr');
            
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
                    <span>${producto.cantidad}<span/>
                    <button class="cantidad-btn" data-action="increase" data-index="${index}">+</button>
                </td>
                <td>RD$${(producto.precio * producto.cantidad).toFixed(2)}</td>
                <td>RD$${itebis.toFixed(2)}</td>
                <td><button class="eliminar-btn" data-index="${index}"><i class="fas fa-trash"></i></button></td>
            `;

            productoRow.classList.add('producto-row');
            productoRow.querySelector('.ctd-img').classList.add('ctd-img');

            carritoContainer.appendChild(productoRow);

            totalProductos += parseInt(producto.cantidad);
            totalPrecio += (producto.precio * producto.cantidad);
        });

        totalFinal = totalPrecio + totalItebisCalculado + 200;

        articulosSeleccionados.textContent = totalProductos;
        totalCarrito.textContent = `RD$${totalFinal.toFixed(2)}`;
        totalItebis.textContent = `RD$${totalItebisCalculado.toFixed(2)}`;
        sessionStorage.setItem('totalFinal', totalFinal.toFixed(2));
    }

    function modificarCantidad(index, action) {
        const producto = carrito[index];
        if (action === 'increase' && producto.cantidad < producto.cantidadDisponible) {
            producto.cantidad++;
        } else if (action === 'decrease' && producto.cantidad > 1) {
            producto.cantidad--;
        }
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    carritoContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('cantidad-btn')) {
            const action = event.target.getAttribute('data-action');
            const index = parseInt(event.target.getAttribute('data-index'));
            modificarCantidad(index, action);
        }
    });

    carritoContainer.addEventListener('change', function(event) {
        if (event.target.classList.contains('cantidad-input')) {
            const index = parseInt(event.target.getAttribute('data-index'));
            const nuevaCantidad = parseInt(event.target.value);
            const producto = carrito[index];
            
            if (nuevaCantidad >= 1 && nuevaCantidad <= producto.cantidadDisponible) {
                producto.cantidad = nuevaCantidad;
            } else if (nuevaCantidad < 1) {
                producto.cantidad = 1;
            } else {
                producto.cantidad = producto.cantidadDisponible;
            }
            
            localStorage.setItem('carrito', JSON.stringify(carrito));
            actualizarCarrito();
        }
    });

    function eliminarProducto(index) {
        carrito.splice(index, 1);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }

    carritoContainer.addEventListener('click', function(event) {
        if (event.target.closest('.eliminar-btn')) {
            const index = parseInt(event.target.closest('.eliminar-btn').getAttribute('data-index'));
            eliminarProducto(index);
        }
    });

    if (procederPagoLink) {
        procederPagoLink.addEventListener('click', function(event) {
            if (carrito.length === 0) {
                event.preventDefault();
                alert("Tu carrito está vacío. No puedes proceder al pago.");
            } else {
                const factura = {
                    numeroOrden: Math.floor(Math.random() * 100000),
                    fecha: new Date().toLocaleDateString(),
                    hora: new Date().toLocaleTimeString(),
                    productos: carrito,
                    total: parseFloat(sessionStorage.getItem('totalFinal'))
                };
                localStorage.setItem('factura', JSON.stringify(factura));
            }
        });
    }

    actualizarCarrito();
});