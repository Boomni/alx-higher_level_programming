$('document').ready(function () {
  $('DIV#add_item').click(function() {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function() {
    $('.my_list li:last-child').remove();
  });
  $('#clear_list').click(function() {
    $('.my_list').empty();
  });
});
