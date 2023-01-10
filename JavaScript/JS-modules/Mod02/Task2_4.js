let lista = [];
let listareverse = [];
let numero = 1

for (let i = 1; numero !== 0; i++) {
  let numero = parseInt(prompt('Anna numero'));
  lista.push(numero);
  lista.sort();
}

for (let i = lista.length - 1; i > -1; i--) {
  listareverse.push(lista[i]);

}