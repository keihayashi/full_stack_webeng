'use strict';

var initialPlaces = [
  {name: 'Recchiuti Confections', latLng: {lat:'37.795547', lng: '-122.393421'}},
  {name: 'Dandelion Chocolate', latLng: {lat: '37.761025', lng: '-122.421782'}},
  {name: 'Chocolate Covered', latLng: {lat: '37.751242', lng: '-122.433351'}},
  {name: 'Socola Chocolatier + Barista', latLng: {lat: '37.786623', lng: '-122.395110'}},
  {name: 'Poco Dolce Chocolates', latLng: {lat: '37.759400', lng: '-122.388228'}},
  {name: 'Sixth Course', latLng: {lat: '37.766967', lng: '-122.418802'}},
  {name: 'Feve Artisan Chocolatier', latLng: {lat: '37.727083', lng: '-122.390954'}},
  {name: 'Christopher Elbow Chocolates', latLng: {lat: '37.776703', lng: '-122.423125'}}
];

var googleMap;
var infowindow;

function initMap() {
  // used style from https://snazzymaps.com/style/93/lost-in-the-desert
  var styles = [{"elementType":"labels","stylers":[{"visibility":"off"},{"color":"#f49f53"}]},{"featureType":"landscape","stylers":[{"color":"#f9ddc5"},{"lightness":-7}]},{"featureType":"road","stylers":[{"color":"#813033"},{"lightness":43}]},{"featureType":"poi.business","stylers":[{"color":"#645c20"},{"lightness":38}]},{"featureType":"water","stylers":[{"color":"#1994bf"},{"saturation":-69},{"gamma":0.99},{"lightness":43}]},{"featureType":"road.local","elementType":"geometry.fill","stylers":[{"color":"#f19f53"},{"weight":1.3},{"visibility":"on"},{"lightness":16}]},{"featureType":"poi.business"},{"featureType":"poi.park","stylers":[{"color":"#645c20"},{"lightness":39}]},{"featureType":"poi.school","stylers":[{"color":"#a95521"},{"lightness":35}]},{},{"featureType":"poi.medical","elementType":"geometry.fill","stylers":[{"color":"#813033"},{"lightness":38},{"visibility":"off"}]},{},{},{},{},{},{},{},{},{},{},{},{"elementType":"labels"},{"featureType":"poi.sports_complex","stylers":[{"color":"#9e5916"},{"lightness":32}]},{},{"featureType":"poi.government","stylers":[{"color":"#9e5916"},{"lightness":46}]},{"featureType":"transit.station","stylers":[{"visibility":"off"}]},{"featureType":"transit.line","stylers":[{"color":"#813033"},{"lightness":22}]},{"featureType":"transit","stylers":[{"lightness":38}]},{"featureType":"road.local","elementType":"geometry.stroke","stylers":[{"color":"#f19f53"},{"lightness":-10}]},{},{},{}]
  googleMap = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.761, lng: -122.412},
    zoom: 13,
    styles: styles
  });
  infowindow = new google.maps.InfoWindow();
  ko.applyBindings(new ViewModel());
}

function ErrorHandling() {
  alert('Map could not be loaded.');
}

var ViewModel = function() {
  var self = this;

  this.prefix = ko.observable('');
  // in case the initialPlaces changes
  this.places = ko.observableArray(initialPlaces);

  this.client_id = 'YOUR_CLIENT_ID';
  this.client_secret = 'YOUR_CLIENT_SECRET';
  // create markers
  this.places().forEach(function(place) {
    var latLng = new google.maps.LatLng(place.latLng.lat, place.latLng.lng);
    var markerOptions = {
      map: googleMap,
      position: latLng,
      animation: google.maps.Animation.DROP,
    };

    var url = "https://api.foursquare.com/v2/tips/search?&limit=3&v=20170112&client_id=" +
              self.client_id + "&client_secret=" + self.client_secret +
              "&ll=" + place.latLng.lat + "," + place.latLng.lng +
              "&query=" + place.name;

    place.contentString = "<div><h4>"+place.name+"</h4><h5>tips provided by foursquare:</h5>";

    $.getJSON(url, function(data) {
      if (data.response && data.response.tips) {
        var tipsList = data.response.tips;
        for (var i = 0; i < tipsList.length; i++) {
            var t = tipsList[i];
            if (t.text) {
              place.contentString += t.text + '</br>';
            }
        }
        place.contentString += "</div>";
      } else {
        place.contentString = "Tips are not avaialble";
      }
    }).fail(function(e){
      place.contentString += 'Foursquare URLs Could Not Be Loaded';
    }).always(function () {
      place.marker = new google.maps.Marker(markerOptions);
      place.marker.addListener('click', function() {
        place.marker.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout(function(){ place.marker.setAnimation(null); }, 700);
        infowindow.setContent(place.contentString);
        infowindow.open(googleMap, place.marker);
      });
      place.infowindow = infowindow;
    });

    place.getMarker = function(data) {
      google.maps.event.trigger(data.marker, 'click');
    };
  });

  this.filteredPlaces = ko.computed(function() {
    var search = self.prefix().toLowerCase();
    return ko.utils.arrayFilter(self.places(), function($data) {
      return $data.name.toLowerCase().indexOf(search) >= 0;
    }, this);
  });

  this.filteredPlaces.subscribe(function() {
    for (var l in self.places()) {
      self.places()[l].marker.setVisible(false);
      infowindow.close();
    }
    var placeToShow = self.filteredPlaces();
    for (var s in placeToShow) {
      placeToShow[s].marker.setVisible(true);
    }
  });
};
