let target = document.getElementById('target');

let li1 = document.createElement('li')
li1.innerText = 'First item'
target.appendChild(li1)

let li2 = document.createElement('li')
li2.innerText = 'Second item'
target.appendChild(li2)
li2.classList.add('my-list')

let li3 = document.createElement('li')
li3.innerText = 'Third item'
target.appendChild(li3)