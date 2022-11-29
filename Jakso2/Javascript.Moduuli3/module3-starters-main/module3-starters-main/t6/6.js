const button = document.querySelector('button');

function popup(evt){
  alert('Button clicked');
}

button.addEventListener('click', popup);