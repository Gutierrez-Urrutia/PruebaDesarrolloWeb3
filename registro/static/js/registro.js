document.addEventListener('DOMContentLoaded', function() {
    fetch('pais/')
    .then(response => response.json())
    .then(data => {
        const selectPaises = document.getElementById('pais');
        data.forEach(pais => {
            const option = document.createElement('option');
            option.value = pais.id_pais;
            option.textContent = pais.nombre_pais;
            selectPaises.appendChild(option);
        });
        
    });

    document.getElementById('pais').addEventListener('change', function() {
        const paisId = this.value;
        const selectRegiones = document.getElementById('region');
        selectRegiones.removeAttribute('disabled');
        selectRegiones.innerHTML = '<option value="">Seleccione una región</option>'; // Limpiar regiones
        if (paisId) {
            fetch(`region/${paisId}/`)
            .then(response => response.json())
            .then(data => {
                data.forEach(region => {
                    const option = document.createElement('option');
                    option.value = region.id_region;
                    option.textContent = region.nombre_region;
                    selectRegiones.appendChild(option);
                });
            });
        }
    });

    document.getElementById('region').addEventListener('change', function() {
        const regionId = this.value;
        const selectComunas = document.getElementById('comuna');
        selectComunas.removeAttribute('disabled');
        selectComunas.innerHTML = '<option value="">Seleccione una comuna</option>'; // Limpiar comunas
        if (regionId && regionId !== 'undefined') { // Asegurarse de que regionId tenga un valor válido
            fetch(`comuna/${regionId}/`) // Ajustar la URL correctamente
            .then(response => response.json())
            .then(data => {
                data.forEach(comuna => {
                    const option = document.createElement('option');
                    option.value = comuna.id_comuna;
                    option.textContent = comuna.nombre_comuna;
                    selectComunas.appendChild(option);
                });
            })
            .catch(error => console.error('Error:', error));
        }
    });
});


window.addEventListener('scroll', function () {
    const supermanIcon = document.getElementById('scroll-top-icon');
    if (window.scrollY > 30) {
        supermanIcon.style.display = 'block';
    } else {
        supermanIcon.style.display = 'none';
    }
});
