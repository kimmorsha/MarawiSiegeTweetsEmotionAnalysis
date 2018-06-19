import geocoder

g = geocoder.google([13.65966045, 121.06852702], method='reverse')
print g.json