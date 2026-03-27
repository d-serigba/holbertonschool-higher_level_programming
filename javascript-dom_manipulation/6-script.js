const characterElement = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    characterElement.textContent = data.name;
  });
