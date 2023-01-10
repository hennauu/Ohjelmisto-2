function rollDie(tahkot) {
  return Math.ceil(Math.random() * tahkot);
}

function playgame(tahkot) {
  let resultselem = document.getElementById('results');
  let ulelem = document.createElement('ol');
  resultselem.append(ulelem);

  let dievalue = -1;

  while (dievalue !== tahkot) {
    dievalue = rollDie(tahkot);
    console.log(dievalue);
    const lielem = document.createElement('li');
    lielem.innerText = 'Heiton tulos ' + dievalue;
    ulelem.append(lielem);

  }
}

const diesize = parseInt(prompt('Kuinka monta tahkoa nopalla on?'));
playgame(diesize);