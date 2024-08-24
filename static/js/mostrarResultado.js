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
                    <td>${data.telefono}</td>
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


// document.addEventListener('DOMContentLoaded', () => {
//     const data = JSON.parse(localStorage.getItem('cotizacionData'));
//     const total = localStorage.getItem('total');

//     if (data) {
//         const resultadoDiv = document.getElementById('resultado');
//         resultadoDiv.innerHTML = generateInvoiceHTML(data, total);
//     }

//     document.querySelector('.siguiente').addEventListener('click', () => {
//         // Aquí puedes implementar la lógica para pagar el 50% si es necesario
//         // Enviar datos a la ruta de pago (puedes ajustar según la lógica de tu aplicación)
//         fetch('/guardar_datos', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': getCsrfToken() // Asegúrate de incluir CSRF token si es necesario
//             },
//             body: JSON.stringify({
//                 ...data,
//                 total
//             })
//         }).then(response => {
//             if (response.ok) {
//                 window.location.href = '/confirmacion'; // Redirige a la página de confirmación
//             } else {
//                 console.error('Error al guardar los datos.');
//             }
//         });
//     });

//     function getCsrfToken() {
//         // Aquí deberías implementar la lógica para obtener el token CSRF, si es necesario
//         return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
//     }

//     function generateInvoiceHTML(data, total) {
//         let additionalServicesHTML = '';
        
//         if (data['servicios[]']) {
//             let additionalServices = data['servicios[]'];
//             if (!Array.isArray(additionalServices)) {
//                 additionalServices = [additionalServices];
//             }
//             additionalServicesHTML = additionalServices.map(service => `<li>${service}</li>`).join('');
//         }
//         return `
//             <h2>Factura de Servicio</h2>
//             <table>
//                 <tr>
//                     <th>Fecha:</th>
//                     <td>${data.fecha}</td>
//                 </tr>
//                 <tr>
//                     <th>Nombre:</th>
//                     <td>${data.nombre}</td>
//                 </tr>
//                 <tr>
//                     <th>Apellido:</th>
//                     <td>${data.apellido}</td>
//                 </tr>
//                 <tr>
//                     <th>Celular:</th>
//                     <td>${data.telefono}</td>
//                 </tr>
//                 <tr>
//                     <th>Correo:</th>
//                     <td>${data.correo}</td>
//                 </tr>
//                 <tr>
//                     <th>Servicio a realizar:</th>
//                     <td>${data.proyecto}</td>
//                 </tr>
//                 ${additionalServicesHTML ? `
//                 <tr>
//                     <th>Servicios adicionales:</th>
//                     <td>
//                         <ul>${additionalServicesHTML}</ul>
//                     </td>
//                 </tr>
//                 ` : ''}
//                 <tr>
//                     <th>Requerimiento:</th>
//                     <td>${data.requerimiento}</td>
//                 </tr>
//                 <tr>
//                     <th>¿Cómo se enteró?:</th>
//                     <td>${data.enterar}</td>
//                 </tr>
//                 <tr>
//                     <th>Total:</th>
//                     <td>RD$${total}.00</td>
//                 </tr>
//             </table>
//         `;
//     }
// });
