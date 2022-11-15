const numerot = []

let numero = prompt("Anna numero")

while (numerot.includes(numero)==false) {
    numerot.push(numero)
    numero = prompt("Anna numero")

}


if (numerot.includes(numero) ) {
alert("Numero jo syötetty!")
    numerot.sort((a,b) => a-b);
    console.log(numerot)
}




