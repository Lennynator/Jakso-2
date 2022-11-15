'use strict';

// prompt kysy kandidaattaje

const maara = prompt("Anna ehdokkaiden määrä:");

const osallistujat = [];

for (let i=0; i < maara; i++) {
  const nimet = prompt(`Syötä ehdokkaiden nimi `);
  osallistujat.push({nimi:nimet,aanet:0})

}



const aanestajat = prompt("Anna äänestäjien määrä:");

for (let i=0; i < aanestajat; i++) {
  let keta = prompt("Ketä äänestät?");
  for (let osallistuja of osallistujat) {
    if (keta==osallistuja.nimi) {
      osallistuja.aanet = osallistuja.aanet+1
    }
  }


}

osallistujat.sort((a, b) => {
   return (b.aanet - a.aanet);
});

console.log(`Voittaja oli ${osallistujat[0].nimi} äänimäärällä ${osallistujat[0].aanet}`)
console.log("Tulokset:")
osallistujat.forEach((e) => {
  console.log(`${e.nimi}: ${e.aanet} ääntä`);
})



// äänien pitää alkaa 0 ja siitä kasvattaa
//silmukka alkaa
// kysy kandidaattien nimiä
//säily kandidaattien nimet ja äänimäärät
//silmukka loppuu


// ohjelma kysyy äänestäjien määrän
//  silmukka (äänestäjien lukumäärä)
//  kysy joka äänestäjältä keitä he äänestävät
//  toinen silmukka (ehdokkaat)
//  jos (if) ääni = ehdokas.nimi)
//    kasvata ehdokas.vote yhdellä
//  silmukka päättyy
//silmukka päättyy

// järjestä ehdokkaat äänien mukaan, suurimmasta pienimpään