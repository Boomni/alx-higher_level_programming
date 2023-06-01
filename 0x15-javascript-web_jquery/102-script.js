$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
      const translation = data.hello;
      $('#hello').text(translation);
    })
    .fail(function() {
      $('#hello').text('Translation not found');
    });
  });
});
