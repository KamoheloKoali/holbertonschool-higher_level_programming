document.addEventListener('DOMContentLoaded', () => {
    const moviesList = document.getElementById('list_movies');
  
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => response.json())
      .then(data => {
        const movies = data.results;
        movies.forEach(movie => {
          const listItem = document.createElement('li');
          listItem.textContent = movie.title;
          moviesList.appendChild(listItem);
        });
      })
      .catch(error => {
        console.error('Error fetching movies:', error);
      });
  });