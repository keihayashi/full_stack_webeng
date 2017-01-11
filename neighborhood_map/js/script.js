var initialPlaces = [
  'Recchiuti Confections',
  'Dandelion Chocolate',
  'Chocolate Covered',
  'Socola Chocolatier + Barista',
  'Poco Dolce Chocolates',
  'Sixth Course',
  'Feve Artisan Chocolatier',
  'Christopher Elbow Chocolates'
];

var ViewModel = function(prefix) {
  var self = this;
  this.prefix = ko.observable(prefix);
  this.places = ko.observableArray(initialPlaces);
  // if (this.prefix() != "") {
  //   this.places = ko.observableArray([]);
  //   for (i in initialPlaces) {
  //     if (initialPlaces[i].indexOf(this.prefix()) != 0) {
  //       this.places.push(initialPlaces[i]);
  //     }
  //   };
  // } else {
  //   this.places = ko.observableArray(initialPlaces);
  // }
};

ko.applyBindings(new ViewModel());
