'use strict'
const nimi = prompt("Anna nimesi:");

let result = Math.floor(Math.random()*4)+1;

if (result == 1) {
    const target = document.getElementById('kohde');
target.innerHTML = nimi+", olet Puuskupuh."
        }
 else if (result==2) {
     const target = document.getElementById('kohde');
target.innerHTML= nimi+", olet Korpinkynsi."
        }
 else if (result==3) {
     const target = document.getElementById('kohde');
target.innerHTML = nimi+", olet Luihuinen."
        }
 else {const target = document.getElementById('kohde');
target.innerHTML = nimi+", olet Rohkelikko"
}

