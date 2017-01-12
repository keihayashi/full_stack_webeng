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

var ViewModel = function() {
  var self = this;

  this._prefix = ko.observable('');
  // in case the initialPlaces changes
  this.places = ko.observableArray(initialPlaces);

  this.filteredPlaces = ko.computed(function() {
    var search = self._prefix().toLowerCase();
    return ko.utils.arrayFilter(self.places(), function($data) {
      return $data.toLowerCase().indexOf(search) == 0;
    });
  });
};

ko.applyBindings(new ViewModel());
