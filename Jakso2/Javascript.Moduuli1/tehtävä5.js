'use strict';

const vuosi = +prompt('Syötä vuosiluku:');

console.log(vuosi % 4 == 0);

if (vuosi % 4 == 0 && vuosi % 100 != 0) {
  const target = document.getElementById('kohde');
  target.innerHTML = 'Vuosi on karkausvuosi!';
} else if (vuosi % 400 == 0) {
  const target = document.getElementById('kohde');
  target.innerHTML = 'Vuosi on karkausvuosi!';
} else {
  const target = document.getElementById('kohde');
  target.innerHTML = 'Vuosi ei ole karkausvuosi!';
}





