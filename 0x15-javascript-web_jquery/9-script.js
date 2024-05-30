// Script to fetch data from the given URL and display the value of 'hello' in the <div> element with the ID hello
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('div#hello').text(data.hello);
});
