document.getElementById('pais').addEventListener('change', function() {
    const region = document.getElementById('region');
    region.removeAttribute('disabled');
});

document.getElementById('region').addEventListener('change', function() {
    const comuna = document.getElementById('comuna');
    comuna.removeAttribute('disabled');
    
});


window.addEventListener('scroll', function () {
    const supermanIcon = document.getElementById('scroll-top-icon');
    if (window.scrollY > 30) {
        supermanIcon.style.display = 'block';
    } else {
        supermanIcon.style.display = 'none';
    }
});