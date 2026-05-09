document.addEventListener('DOMContentLoaded', function() {

    // 1. BOTONES DE WHATSAPP DIRECTO
    const botonesWsp = document.querySelectorAll('.btn-wsp-directo');
    
    if (botonesWsp.length) {
        botonesWsp.forEach(btn => {
            btn.addEventListener('click', () => {
                const textoDefault = 'Hola! Te escribo desde la web de Las Recetas de la Nona';
                const linkWsp = `https://wa.me/542665059906?text=${encodeURIComponent(textoDefault)}`;
                window.open(linkWsp, '_blank');
            });
        });
    }

    // 2. FORMULARIO DE CONTACTO
    const form = document.getElementById('formContacto');
    const mensajeExito = document.getElementById('mensajeExito');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const nombre = document.getElementById('nombre').value.trim();
            const telefono = document.getElementById('telefono').value.trim();
            const email = document.getElementById('email').value.trim();
            const mensaje = document.getElementById('mensaje').value.trim();

            if (!nombre || !telefono || !email) {
                alert('Completá nombre, teléfono y email porfa');
                return;
            }

            // WhatsApp
            const textoWhatsApp = `Hola ${nombre} Soy Yani!. Te escribo desde la web. Mi consulta: ${mensaje}. Mi tel: ${telefono}`;
            const linkWhatsApp = `https://wa.me/542665059906?text=${encodeURIComponent(textoWhatsApp)}`;
            
            window.open(linkWhatsApp, '_blank');

            // Envío por Formspree
            fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
                headers: { 'Accept': 'application/json' }
            })
            .then(response => {
                if (response.ok) {
                    if (mensajeExito) {
                        mensajeExito.style.display = 'block';
                    }
                    form.reset();
                } else {
                    alert('Hubo un error al enviar el mail. Probá de nuevo.');
                }
            })
            .catch(error => {
                console.log('Error:', error);
                alert('Hubo un error al enviar el mail. Probá de nuevo.');
            });
        });
    }

    // 3. MENÚ HAMBURGUESA (solo si existe en el HTML)
    const menuBtn = document.getElementById('menuBtn');
    const navLinks = document.getElementById('navLinks');

    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

});