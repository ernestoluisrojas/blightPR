    var map = L.map('map', {
    center: [18.44639, -66.08276],
    zoom: 14
    });

    /*OpenStreetMap
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
    }).addTo(map);
    */

    /*OpenStreetMap.BlackAndWhite
    L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    */

    //Stamen_TonerLite
    L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 20,
    ext: 'png'
}).addTo(map);
    

    var shpfile = new L.Shapefile("/static/media/Desuso.zip",{
      onEachFeature:function(feature, layer) { 
        layer.bindPopup("<a href='/properties/"+feature.properties.Catastro+"'>"+feature.properties.Catastro+"</a>");
      }
    });
    shpfile.addTo(map);