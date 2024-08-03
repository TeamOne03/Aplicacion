    document.addEventListener("DOMContentLoaded", function() {
        const servicios = document.querySelectorAll(".servicios__img");
        const serviciosAgregadosList = document.getElementById("servicios-agregados");

        servicios.forEach(servicio => {
            const btn = servicio.querySelector(".solicitar-btn");
            btn.addEventListener("click", function() {
                const serviceName = btn.getAttribute("data-servicio");
                const li = document.createElement("li");
                li.textContent = serviceName;
                serviciosAgregadosList.appendChild(li);
            });
        });
    });

