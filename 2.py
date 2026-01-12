from pyproj import Transformer , Geod

lonA, latA =map(float,input("Enter the longitude and latitude for point A separated by commas: ").split(","))
lonB, latB =map(float,input("Enter the longitude and latitude for point B separated by commas: ").split(","))

transformer = Transformer.from_crs("EPSG:4326","EPSG:32735",always_xy = True)

xA ,yA = transformer.transform(lonA,latA)
xB ,yB = transformer.transform(lonB,latB)

print("The UTM co-ordinates are: ")
print(f"Point A: Easting: {xA:.3f} , Northing: {yA:.3f}")
print(f"Point B: Easting: {xB:.3f} , Northing: {yB:.3f}")

geod  = Geod(ellps ='WGS84')
bearing_AB , _, distance_AB = geod.inv(lonA,latA,lonB,latB)
bearing_AB = (bearing_AB + 360) % 360

print(f"The bearing of point B from point A is {bearing_AB:.3f}")
print(f"The distance from point A to point B is {distance_AB:.3f}")
