var initialPlaces = [
  {name: 'Recchiuti Confections', latLng: {lat:'37.795547', lng: '-122.393421'}},
  {name: 'Dandelion Chocolate', latLng: {lat: '37.761025', lng: '-122.421782'}},
  {name: 'Chocolate Covered', latLng: {lat: '37.751242', lng: '-122.433351'}},
  {name: 'Socola Chocolatier + Barista', latLng: {lat: '37.786623', lng: '-122.395110'}},
  {name: 'Poco Dolce Chocolates', latLng: {lat: '37.759400', lng: '-122.388228'}},
  {name: 'Sixth Course', latLng: {lat: '37.766967', lng: '-122.418802'}},
  {name: 'Feve Artisan Chocolatier', latLng: {lat: '37.727083', lng: '-122.390954'}},
  {name: 'Christopher Elbow Chocolates', latLng: {lat: '37.776703', lng: '-122.423125'}}
]

var ViewModel = function() {
  var self = this;

  // set up google map
  this.googleMap = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.761, lng: -122.412},
    zoom: 13
  });

  this._prefix = ko.observable('');
  // in case the initialPlaces changes
  this.places = ko.observableArray(initialPlaces);
  // create markers
  this.places().forEach(function(place) {
    var latLng = new google.maps.LatLng(place.latLng.lat, place.latLng.lng);
    var markerOptions = {
      map: self.googleMap,
      position: latLng,
      animation: google.maps.Animation.DROP,
    };

    this.client_id = 'YOUR_CLIENT_ID';
    this.client_secret = 'YOUR_CLIENT_SECRET';

    var url = "https://api.foursquare.com/v2/tips/search?&limit=3&v=20170112&client_id=" +
              this.client_id + "&client_secret=" + this.client_secret +
              "&ll=" + place.latLng.lat + "," + place.latLng.lng
              + "&query=" + place.name;

    var contentString = "<div><h3>"+place.name+"</h3>"
    $.getJSON(url, function(data){
      tipsList = data.response.tips;
      for (var i = 0; i < tipsList.length; i++) {
          var t = tipsList[i];
          if (t.text) {
            contentString += t.text + '</br>';
          };
      };
      contentString += "</div>";
      // console.log(contentString);
      var infowindow = new google.maps.InfoWindow({content: contentString});
      place.marker = new google.maps.Marker(markerOptions);
      place.marker.addListener('click', function() {
        infowindow.open(self.googleMap, place.marker);
      });
      place.infowindow = infowindow;
    }).error(function(e){
        contentString += 'Foursquare URLs Could Not Be Loaded';
    });

    place.getMarker = function(data) {
      // console.log(data);
      data.infowindow.open(self.googleMap, data.marker);
    };
  });

  this.filteredPlaces = ko.computed(function() {
    var search = self._prefix().toLowerCase();
    return ko.utils.arrayFilter(self.places(), function($data) {
      return $data.name.toLowerCase().indexOf(search) >= 0;
    }, this);
  });

  this.filteredPlaces.subscribe(function() {
    for (var l in self.places()) {
      self.places()[l].marker.setMap(null);
    }
    var placeToShow = self.filteredPlaces();
    for (var l in placeToShow) {
      placeToShow[l].marker.setMap(self.googleMap);
    }
  });
};

ko.applyBindings(new ViewModel());
