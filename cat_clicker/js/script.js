var count = 0;

$(function() {
  $('#my-elem').click(function(e) {
    //the element has been clicked... do stuff here
    count += 1;
    console.log(count);
    $('#click-num').text('You clicked ' + count + ' times.');
    return false;
  });
});
