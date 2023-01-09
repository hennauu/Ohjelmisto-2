const numberOfDice = +prompt("Montako noppaa heitetään?")
const sumOfEyes = +prompt("Paljonko haluat pisteitä?")

let totalSums = 0;
for(let i = 0; i < 10_000; i++) {
  let sum = 0
  for (let j = 0; j < numberOfDice; j++) {
    sum += Math.ceil(Math.random() * 6)
  }
  if (sum == sumOfEyes) totalSums++
}

const percentage = ((totalSums / 10_000) * 100).toFixed(2)

document.querySelector("h1").textContent += `Todennäköisyys saada silmäluku ${sumOfEyes} näin monella nopalla: ${numberOfDice}, on ${percentage} prosenttia`