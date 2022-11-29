'use strict';

//1. valitse elementti / elementit
//2. kun nappia klikataan, hae arvot ja tee haluttu laskutoimitus

const trigger = document.querySelector('button');
trigger.addEventListener('click', function() {
  let ens = document.querySelector('#num1').value;
  let toi = document.querySelector('#num2').value;
  const vast = document.querySelector('#result');

  if (document.getElementById('operation').value = 'add') {
    const tulos = +ens + +toi;
    console.log(tulos);
    vast.innerText = tulos;
    return tulos;
  } else if (document.getElementById('operation').value = 'sub') {
    const tulos = ens - toi;
    console.log(tulos);
    vast.innerText = tulos;
    return tulos;
  } else if (document.getElementById('operation').value = 'multi') {
    const tulos = ens * toi;
    console.log(tulos);
    vast.innerText = tulos;
    return tulos;
  } else if (document.getElementById('operation').value = 'div') {
    const tulos = ens / toi;
    console.log(tulos);
    vast.innerText = tulos;
    return tulos;
  }

});


