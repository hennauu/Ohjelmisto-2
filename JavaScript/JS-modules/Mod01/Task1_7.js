let nopat = parseInt(prompt('Anna noppien lukumäärä.'));
let summa = 0;
for (let i = 1; i <= nopat; i++) {
  (summa += Math.floor(Math.random() * 6) + 1);
}

document.querySelector('#p1').innerHTML = 'Noppien summa on ' + (summa);