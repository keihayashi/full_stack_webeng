
$(function() {
  var model = [
    {
      "name" : "Alice",
      "click" : 0
    }, {
      "name" : "Bob",
      "click" : 0
    }, {
      "name" : "Cathey",
      "click" : 0
    }, {
      "name" : "Dick",
      "click" : 0
    }, {
      "name" : "Edward",
      "click" : 0
    }
  ];

  var octopus = {
    addClick: function(cur) {
      model[cur - 1].click += 1;
      view_click.render(cur);
    },
    selectCat: function(cur) {
      view_select.render(cur);
    },
    init: function() {
      view_select.init();
      view_click.init();
    }
  };

  var view_select = {
    init: function() {
      var selectBtn = $('#submit-btn');
      selectBtn.click(function() {
          var cur = $('input[name=cat-select]:checked').val();
          octopus.selectCat(cur);
      });
    },
    render: function(cur) {
      var picture = "img/cat" + cur + ".jpg";
      $(".cat-img").attr("src", picture);
      $('#cat-name').text(model[cur - 1].name);
      $('#click-num').text(model[cur - 1].click);
    }
  };

  var view_click = {
    init: function() {
      var clickCat = $('#cat-button');
      clickCat.click(function() {
        var cur = $('input[name=cat-select]:checked').val();
        octopus.addClick(cur);
      });
    },
    render: function(cur) {
      $('#click-num').text(model[cur - 1].click);
    }
  };

  octopus.init();
}());
