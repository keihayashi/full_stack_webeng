
$(function() {
  var model = {
    currentCat: 1,
    cats: [
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
    ]
  };

  var octopus = {
    getModelCurrent: function() {
      return model.currentCat;
    },
    getCurrentCat: function() {
      return model.cats[model.currentCat - 1];
    },
    setCurrentCat: function(cur) {
      model.currentCat = cur;
      view_select.render();
    },
    addClick: function() {
      this.getCurrentCat().click += 1;
      view_click.render();
    },
    init: function() {
      view_select.init();
      view_click.init();
      view_admin.init();
    }
  };

  var view_admin = {
    init: function() {
      document.getElementById("set-value").style.display="none";
      var admin = $("#admin");
      admin.click(function() {
        if (admin.value == false) {
          admin.value = true;
          document.getElementById("set-value").style.display="none";
        } else {
          admin.value = false;
          document.getElementById("set-value").style.display="block";
        }
      });
    }
  };

  var view_select = {
    init: function() {
      var selectBtn = $('input[name=cat-select]:radio');
      selectBtn.change(function() {
          var cur = $('input[name=cat-select]:checked').val();
          octopus.setCurrentCat(cur);
      });
    },
    render: function() {
      var cur = octopus.getModelCurrent();
      var picture = "img/cat" + cur + ".jpg";
      $(".cat-img").attr("src", picture);
      $('#cat-name').text(octopus.getCurrentCat().name);
      $('#click-num').text(octopus.getCurrentCat().click);
    }
  };

  var view_click = {
    init: function() {
      var clickCat = $('#cat-button');
      clickCat.click(function() {
        octopus.addClick();
      });
    },
    render: function() {
      $('#click-num').text(octopus.getCurrentCat().click);
    }
  };

  octopus.init();
}());
