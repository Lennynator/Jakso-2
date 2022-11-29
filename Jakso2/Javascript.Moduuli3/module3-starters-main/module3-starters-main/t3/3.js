'use strict';
const students = ['John', 'Paul', 'Jones'];


 for (let i = 0; i < students.length; i++){
    let lista = document.createElement('li');
    lista.innerText=students[i];
     document.querySelector('#target').appendChild(lista);
  }