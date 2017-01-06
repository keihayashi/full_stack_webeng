var count = [0,0,0,0,0];
var name_list = ["Alice", "Bob", "Cathey", "Dick", "Edward"];
var cur = 1;

$(function() {
  $('#submit-btn').click(function(e) {
    // chenge the cat pic and value.
    var num = $('input[name=cat-select]:checked').val();
    console.log(num);
    cur = num;
    var picture = "img/cat" + num + ".jpg";
    $(".cat-img").attr("src", picture);
    $('#cat-name').text(name_list[num - 1]);
    $('#click-num').text(count[num - 1]);
    return false;
  });

  $('#cat-button').click(function(e) {
    //the element has been clicked... do stuff here
    count[cur - 1] += 1;
    console.log(count[cur - 1]);
    $('#click-num').text(count[cur - 1]);
    return false;
  });
});
