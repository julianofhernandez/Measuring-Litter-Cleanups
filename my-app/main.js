import Map from 'ol/Map';
import View from 'ol/View';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import KML from 'ol/format/KML';
import {Icon, Style} from 'ol/style';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {fromLonLat} from 'ol/proj.js';

import GeoJSON from 'ol/format/GeoJSON';
import {OSM, Vector} from 'ol/source';

const iconFeature = new Feature({
  geometry: new Point([-13518000.0, 4660000.0]),
  name: 'Null Island',
  population: 4000,
  rainfall: 500,
});

const iconStyle = new Style({
  image: new Icon({
    anchor: [0.5, 46],
    anchorXUnits: 'fraction',
    anchorYUnits: 'pixels',
    src: 'icons/icon-waste.svg',
    scale: 0.5,
  }),
});

iconFeature.setStyle(iconStyle);

const vectorSource = new Vector({
  features: [iconFeature],
});

var vectorLayer = new VectorLayer({
  source: vectorSource
});

var trashCans = new Vector({
  source: new Vector ({
    url:'test.geojson',
    format: new GeoJSON(),
  })
})

const milePartners = new VectorLayer({
  source: new Vector({
    url: 'miles.kml',
    format: new KML(),
  }),
});


var trashCansLayer = new VectorLayer({
  source: trashCans
});

const map = new Map({
  layers: [    
    new TileLayer({source: new OSM(),}), vectorLayer, milePartners],
  target: 'map',
  view: new View({
    maxZoom: 18,
    //        X           Y
    // center: [-13518000.0, 4660000.0],
    center: fromLonLat([-121.426095,38.562671]),
    zoom: 13,
  }),
});