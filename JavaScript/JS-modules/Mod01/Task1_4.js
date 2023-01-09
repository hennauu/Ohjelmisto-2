let nimi = prompt('Anna nimesi.');
let num = Math.floor(Math.random()*4)+1;

console.log(num);

if (num === 1) {
    document.querySelector('#p1').innerHTML = nimi + ', you are Gryffindor.';
}

if (num === 2) {
    document.querySelector('#p1').innerHTML = nimi + ', you are Slytherin.';
}

if (num === 3) {
    document.querySelector('#p1').innerHTML = nimi + ', you are Hufflepuff.';
}

if (num === 4) {
    document.querySelector('#p1').innerHTML = nimi + ', you are Ravenclaw.';
}