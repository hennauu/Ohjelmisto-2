lista = []

function rollDice() {
  return Math.ceil(Math.random() * 6);
}

let roll = rollDice()

while (roll !== 6) {
  lista.push(roll)
  roll = rollDice()
}

lista.push(roll)

let list = document.getElementById('html');

for (let item of lista) {
  let li = document.createElement('li');
  li.innerHTML = item;
  list.append(li);
}