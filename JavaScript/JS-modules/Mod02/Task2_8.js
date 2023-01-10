let strlist = ['Ba', 'naani', 'Ome', 'na'];

function concat(array){
  let concat = ''
  for (let i = 0; i < array.length; i++){
    concat = concat + array[i];
  }
  return concat;
}

document.querySelector('#p').textContent = concat(strlist);