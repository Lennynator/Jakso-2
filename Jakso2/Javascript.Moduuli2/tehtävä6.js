'use strict';

let noppa = 0


function heita() {
  let tulos = Math.floor(Math.random() * 6) + 1;
  return tulos;
}


while (noppa!=6) {
  heita();
  noppa=heita();
  document.getElementById('kohde').innerHTML += `<ul>${noppa}</ul>`;
}

//let noppa = 0;

//while (noppa != 6) {
  //noppa = result();
  //