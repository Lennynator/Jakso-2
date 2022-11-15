'use strict'

const maara = prompt("Anna osallistujien määrä:")

const osallistujat = []

for (let i=0; i < maara; i++) {
  osallistujat.push(prompt(`Syötä osallistujan nimi `));
}



osallistujat.sort();

for (let koira of osallistujat) {
  document.getElementById('kohde').innerHTML += `<ol>${koira}</ol>`;}