'use strict';

let noppa = 0

let sivut = prompt("Anna sivujen määrä!")

function heita() {
  let tulos = Math.floor(Math.random() * sivut) + 1;
  return tulos;
}


while (noppa!=sivut) {
  heita();
  noppa=heita();
  document.getElementById('kohde').innerHTML += `<ul>${noppa}</ul>`;
}
