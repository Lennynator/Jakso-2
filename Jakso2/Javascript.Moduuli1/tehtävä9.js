'use strict';


const nummero = parseInt(prompt("Anna luku"));
let onAlku = true;

 if (nummero > 1) {

    for (let i = 2; i < nummero; i++) {
        if (nummero % i == 0) {
            onAlku = false;
            break;
        }
    }

    if (onAlku) {
       const target = document.getElementById('kohde');
  target.innerHTML = 'Numero on alkuluku!';
    } else {
      const target = document.getElementById('kohde');
  target.innerHTML = 'Numero ei ole alkuluku!';
    }
}

else {
    console.log("Numero ei ole alkuluku");
}