'use strict';

const lista = [];

let numero = parseFloat(prompt('Anna numero: '));
while (numero != 0) {
  numero = (prompt('Anna numero: '));
  lista.push(numero);
}

if (numero == 0) {
  console.log(lista.sort(function(a, b){return b-a}));
}
