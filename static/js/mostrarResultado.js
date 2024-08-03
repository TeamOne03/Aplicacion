document.addEventListener('DOMContentLoaded', () => {
    const data = JSON.parse(localStorage.getItem('cotizacionData'));
    const total = localStorage.getItem('total');

    if (data) {
        const resultadoDiv = document.getElementById('resultado');
        resultadoDiv.innerHTML = generateInvoiceHTML(data, total);
    }

    function generateInvoiceHTML(data, total) {
        let additionalServicesHTML = '';
        
        if (data['servicios[]']) {
            let additionalServices = data['servicios[]'];
            if (!Array.isArray(additionalServices)) {
                additionalServices = [additionalServices];
            }
            additionalServicesHTML = additionalServices.map(service => `<li>${service}</li>`).join('');
        }
        return `
            <h2>Factura de Servicio</h2>
            <table>
                <tr>
                    <th>Fecha:</th>
                    <td>${data.fecha}</td>
                </tr>
                <tr>
                    <th>Nombre:</th>
                    <td>${data.nombre}</td>
                </tr>
                <tr>
                    <th>Apellido:</th>
                    <td>${data.apellido}</td>
                </tr>
                <tr>
                    <th>Celular:</th>
                    <td>${data.celular}</td>
                </tr>
                <tr>
                    <th>Correo:</th>
                    <td>${data.correo}</td>
                </tr>
                <tr>
                    <th>Servicio a realizar:</th>
                    <td>${data.proyecto}</td>
                </tr>
                ${additionalServicesHTML ? `
                <tr>
                    <th>Servicios adicionales:</th>
                    <td>
                        <ul>${additionalServicesHTML}</ul>
                    </td>
                </tr>
                ` : ''}
                <tr>
                    <th>Requerimiento:</th>
                    <td>${data.requerimiento}</td>
                </tr>
                <tr>
                    <th>¿Cómo se enteró?:</th>
                    <td>${data.enterar}</td>
                </tr>
                <tr>
                    <th>Total:</th>
                    <td>RD$${total}.00</td>
                </tr>
            </table>
        `;
    }
});
