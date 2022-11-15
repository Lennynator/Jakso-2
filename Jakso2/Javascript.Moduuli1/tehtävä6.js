'use strict';

const answer = confirm('Laskenko neliöjuuren?');


if (answer===false) {
  const target = document.getElementById('kohde');
  target.innerHTML = 'Neliöjuurta ei lasketa';
}

else if (answer===true) {
  let luku = prompt("Anna luku!")

if (luku > 0) {
  const target = document.getElementById('kohde');
  target.innerHTML = "Neliöjuuri on "+(Math.sqrt(luku))+"!";
}
else {const target = document.getElementById('kohde');
  target.innerHTML = 'Negatiivisen luvun neliöjuurta ei ole määritelty!';}}

