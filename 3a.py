from pyproj import Transformer
lat = float(input('Enter the latitude: '))
lon = float(input('Enter the longitude: '))

def wgs84_to_webMercator(lat,lon):
 transformer = Transformer.from_crs('EPSG:4326','EPSG:3857',always_xy=True)
 easting,northing = transformer.transform(lon,lat)
 return easting,northing

easting,northing = wgs84_to_webMercator(lat,lon)
print ('Easting: ',easting)
print ('Northing: ',northing)
