
var marker;

function loadMap() {
    var mapOptions = {
        center: new google.maps.LatLng(latVal,lngVal),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("sample"), mapOptions);

    google.maps.event.addListener(map, 'click', function (e) {
        addMarker(e.latLng, map);
    });
    var contentString = postTitle + "<br>" + 'Latitude: ' + latVal + "<br>" + 'Longitude: ' + lngVal;
    var location = { lat: latVal, lng: lngVal};
    marker = new google.maps.Marker({
        position: location,
        map: map,
    });
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    marker.addListener('click', function () {
        infowindow.open(map, marker);
    }); 
}
google.maps.event.addDomListener(window, 'load', loadMap);