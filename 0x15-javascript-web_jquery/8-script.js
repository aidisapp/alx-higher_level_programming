// Script to fetch and list the titles of all movies using the provided URL
// The titles are appended as <li> elements to the <ul> element with the ID list_movies
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (let movie of data.results) {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  }
});
