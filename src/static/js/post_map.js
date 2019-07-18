
var marker;

function loadMap() {
    var mapOptions = {
        center: new google.maps.LatLng(27.240498, 77.287598),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("sample"), mapOptions);

    google.maps.event.addListener(map, 'click', function (e) {
        addMarker(e.latLng, map);
    });
}

function addMarker(location, map) {

    if (marker) {
        marker.setMap();
    }
   
    marker = new google.maps.Marker({
        position: location,
        map: map,
        draggable: true,
    });

    var contentString = marker.getPosition().lat() + ' , ' + marker.getPosition().lng();
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    marker.addListener('click', function () {
        infowindow.open(map, marker);
    });

    marker.addListener('dragstart', function () {
        infowindow.close();
    });

    marker.addListener('dragend', function () {
        infowindow = new google.maps.InfoWindow({
            content: marker.getPosition().lat() + ' , ' + marker.getPosition().lng()
        });
        infowindow.open();
    });

    document.getElementById("id_lat").value = marker.getPosition().lat();
    document.getElementById("id_lng").value = marker.getPosition().lng();
    //document.getElementById("info").value = contentString;
}

google.maps.event.addDomListener(window, 'load', loadMap);

