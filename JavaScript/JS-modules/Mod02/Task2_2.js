let lista = [];

let osallistujat = parseInt(prompt('Anna osallistujien lukumäärä:'));

for (let i = 0; i < osallistujat; i++) {
  let nimi = prompt('Anna osallistujan nimi:');
  lista.push(nimi)
  lista.sort();

}
console.log(lista)

let list = document.getElementById('html');

for (let item of lista) {
  let li = document.createElement('li');
  li.innerHTML = item;
  list.append(li);
}