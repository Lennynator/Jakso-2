'use strict'

const nopMaara = prompt("Anna heitettävien noppien määrä:")
let summa = 0;

for (let i = 1; i <= nopMaara ; i++) {
            let result = Math.floor(Math.random()*6)+1;
             summa += result;
        }

const target = document.getElementById('kohde');
target.innerHTML = 'Heitettyjen noppien summa on '+summa
