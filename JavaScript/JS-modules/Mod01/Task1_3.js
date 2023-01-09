const int1 = parseInt(prompt('Anna ensimmäinen numero.'));
const int2 = parseInt(prompt('Anna toinen numero.'));
const int3 = parseInt(prompt('Anna kolmas numero.'))


console.log(int1 + int2 + int3);
console.log(int1 * int2 * int3);
console.log((int1 + int2 + int3) / 3);

document.querySelector('#p1').innerHTML = 'Lukujen summa on ' + (int1 + int2 + int3) + ' tulo on ' + (int1 * int2 * int3) + ' ja keskiarvo on ' + ((int1 + int2 + int3) / 3) + '.';