document.addEventListener("DOMContentLoaded", function() {
    // Mostrar la información del pedido
    const pedidosContainer = document.getElementById('pedidosContainer');
    const factura = JSON.parse(localStorage.getItem('factura'));

    if (factura) {
        const pedidoDiv = document.createElement('div');
        pedidoDiv.classList.add('pedido');

        pedidoDiv.innerHTML = `
            <p>Número de orden: #${factura.numeroOrden}</p>
            <p>Fecha: ${factura.fecha}</p>
            <p>Hora: ${factura.hora}</p>
            <p>Productos: ${factura.productos.length} artículos</p>
            <p>Estado: En proceso</p>
            <p>Fecha de entrega estimada: ${new Date(new Date().setDate(new Date().getDate() + 5)).toLocaleDateString('es-DO')}</p>
            <p>Precio: RD$${factura.total.toFixed(2)}</p>
        `;
        pedidosContainer.appendChild(pedidoDiv);
    } else {
        pedidosContainer.innerHTML = '<p>No hay pedidos realizados.</p>';
    }
});
