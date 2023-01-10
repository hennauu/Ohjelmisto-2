let lista = [];
let numero = 0;

while (numero === 0) {
  let int = parseInt(prompt('Anna numero:'));
  if (lista.includes(int)){
    alert('Numero on jo syötetty!');
    numero = 1;
  }
  else{
    lista.push(int);
  }
}

lista.sort(function(a, b){return a-b});

for (let i = 0; i < lista.length; i++){
  console.log(lista[i]);
}