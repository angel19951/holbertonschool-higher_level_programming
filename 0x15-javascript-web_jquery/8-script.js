$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (response, status) {
  if (status === 'success') {
    for (const i in response.results) {
      $('ul#list_movies').append('<li>' + response.results[i].title + '</li>');
    }
  }
});
