#!/usr/bin/node
/* global $ */
/* JavaScript script that fetches and lists the title for all movies
  by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
  */
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const films = data.results;
  for (const film of films) {
    $('UL#list_movies').append('<li>${film.title}</li>');
  }
});
