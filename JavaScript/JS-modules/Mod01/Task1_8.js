const aloitusvuosi = parseInt(prompt('Anna aloitusvuosi: '));
const lopetusvuosi = parseInt(prompt('Anna lopetusvuosi: '));
let lista = [];

let vuosi = aloitusvuosi;
while (vuosi < lopetusvuosi) {
  if (vuosi % 4 === 0 && !(vuosi % 100 === 0) || (vuosi % 400 === 0)) {
    lista.push(vuosi);
  }
  vuosi++;
}

console.log(lista)

let list = document.getElementById('html');

for (let item of lista) {
  let li = document.createElement('li');
  li.innerHTML = item;
  list.append(li);
}