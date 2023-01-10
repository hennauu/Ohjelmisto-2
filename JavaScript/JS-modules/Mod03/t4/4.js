'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

let target = document.getElementById('target');

for (let x of students) {
  let li = document.createElement('option');
  li.innerHTML = x.name;
  li.value = x.id;
  target.appendChild(li);

}