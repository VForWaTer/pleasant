//Create a map layer
function create_map() {
// please define your map server of choice as mapsource 	
	mapsource = new ol.source.OSM()

	maplayer = new ol.layer.Tile({
		source: mapsource,
	});

	mapview = new ol.View({
		center: ol.proj.fromLonLat([11.8810049, 50.0836865]),
		zoom: 6
	});
	
	map_tar = document.getElementById("map");
	map = new ol.Map({
		renderer: 'canvas',
		target: map_tar,
		layers: [maplayer],
		controls: [
			new ol.control.Zoom(),
			new ol.control.Attribution(),
			new ol.control.ZoomSlider(),
			new ol.control.MousePosition({
				projection: 'EPSG:4326',
				coordinateFormat: function(coord) {
					return ol.coordinate.format(coord, '{y}°, {x}°', 4);}
			}),
			new ol.control.ScaleLine(),
			],
			view: mapview
	});
}
