var count = 0;

$(function() {
  $('.cat-button').click(function(e) {
    //the element has been clicked... do stuff here
    count += 1;
    console.log(count);
    $('#click-num').text('You clicked ' + count + ' times.');
    return false;
  });
});
