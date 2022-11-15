'use strict';
const eka = parseInt(prompt('Anna ensimmäinen numero'));
const toka = parseInt(prompt('Anna toinen numero'));
const kolmas = parseInt(prompt('Anna kolmas numero'));
const kert = eka * toka * kolmas;
const yht = eka + toka + kolmas;
const kesk = yht /3 ;
console.log(yht);
console.log(kert);
console.log(kesk);
const target = document.getElementById('kohde');
target.innerHTML = 'Antamiesi lukujen summa on ' +yht+ ', tulo on '+kert+', ja keskiarvo on '+kesk+'!'
