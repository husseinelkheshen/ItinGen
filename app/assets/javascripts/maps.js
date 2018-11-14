handler = Gmaps.build('Google');
handler.buildMap({ provider: {}, internal: {id: 'map'}}, function(){
  markers = handler.addMarkers([
    {
      "lat": 37.3333945,
      "lng": -121.8806499,
      "picture": {
        "width":  32,
        "height": 32
      },
      "infowindow": "SJSU"
    }
  ]);
  handler.bounds.extendWith(markers);
  handler.fitMapToBounds();
});
