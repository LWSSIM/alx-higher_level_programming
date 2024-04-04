$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, film) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
