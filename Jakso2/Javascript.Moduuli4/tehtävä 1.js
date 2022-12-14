'use strict';
const lomake = document.querySelector('form');
const apiUrl = 'https://api.tvmaze.com/search/shows?q=';

async function fetchJson(url, options = {}) {
  const vastaus = await fetch(url, options);
  if (!vastaus.ok) {
    throw new Error(vastaus.statusText);
  }
  return await vastaus.json();
}

lomake.addEventListener('submit', async function(evt) {
  try {
    evt.preventDefault();
    let hakusana = document.querySelector('#query').value;
    const show = await fetchJson(apiUrl + hakusana);
    console.log(show);
    //console.log(show[0].show.genres);
    for (let i = 0; i <= show.length; i++) {
      const name = show[i].show.name;
      const summary = show[i].show.summary;
      const linkki = show[i].show.url;
      const genret = show[i].show.genres;
      let commaSeperated = genret.join('/');
      const h2 = document.createElement('h2');
      const p = document.createElement('p');
      const genre = document.createElement('p');
      const img = document.createElement('img');
      const a = document.createElement('a');
      const dialogue = document.createElement('dialog');
      const iframe = document.createElement('iframe');

      iframe.src = linkki;


      dialogue.appendChild(iframe);


      //dialogue.src=linkki;







      let anchor = document.createElement('a');
      let link = document.createTextNode(linkki);
      anchor.appendChild(link);
      //anchor.href = (linkki + ('target="_blank"'));
      a.appendChild(anchor);

      anchor.addEventListener('click', () => {
        dialogue.showModal();
      });

      dialogue.addEventListener('click', () => {
        dialogue.close();
      });




      if (show[i].show.image == null) {
        img.src = 'https://via.placeholder.com/210x290?text=no+image';
      } else {
        img.src = show[i].show.image.medium;
        img.alt = name;
      }

      h2.innerText = name;
      p.innerHTML = summary;
      genre.innerText = commaSeperated;
      p.appendChild(img);

      document.querySelector('#pictures').appendChild(h2);
      document.querySelector('#pictures').appendChild(p);
      document.querySelector('#pictures').appendChild(a);
      document.querySelector('#pictures').appendChild(genre);
      document.querySelector('#pictures').appendChild(dialogue);

    }

  } catch (e) {
    console.error();
  }
});



