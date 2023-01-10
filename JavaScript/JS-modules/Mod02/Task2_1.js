let lista = [];
let listareverse = []
for (let i = 0; i < 5; i++) {
  let numero = parseInt(prompt('Anna numero:'));
  lista.push(numero);
}

for (let i = lista.length - 1; i > -1; i--) {
  listareverse.push(lista[i]);
}

let list = document.getElementById('html');

for (let item of listareverse) {
  let li = document.createElement('li');
  li.innerHTML = item;
  list.append(li);
}