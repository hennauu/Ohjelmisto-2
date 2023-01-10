'use strict';
let target = document.getElementById('target');
const names = ['John', 'Paul', 'Jones'];


for (let x of names) {
  let li = document.createElement('li')
  li.innerText = x
  target.appendChild(li)

}