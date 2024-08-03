  // Obtener la fecha actual en el formato AAAA-MM-DD
        const hoy = new Date().toISOString().split('T')[0];
        document.getElementById('fecha').setAttribute('min', hoy);