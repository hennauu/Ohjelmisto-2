let target = document.getElementById('target');

target.addEventListener('mouseenter', (e) => {
  target.src = 'img/picA.jpg'
});

target.addEventListener('mouseleave', (e) => {
  target.src = 'img/picB.jpg'
});