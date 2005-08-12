# example demonstrating how to draw a great circle on a map.
from matplotlib.toolkits.basemap import Basemap
from pylab import *

# setup a mercator projection.
m = Basemap(-90.,30.,30.,60.,\
            resolution='c',area_thresh=10000.,projection='merc',\
            lat_ts=20.)
# make figure with aspect ratio that matches map region.
xsize = rcParams['figure.figsize'][0]
fig=figure(figsize=(xsize,m.aspect*xsize))
fig.add_axes([0.1,0.1,0.8,0.8])
# nylat, nylon are lat/lon of New York
nylat = 40.78
nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53
lonlon = 0.08
# find 1000 points along the great circle.
#x,y = m.gcpoints(nylon,nylat,lonlon,lonlat,1000)
# draw the great circle.
#m.plot(x,y,linewidth=2)
# drawgreatcircle performs the previous 2 steps in one call.
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
# draw parallels
circles = [35,45,55]
m.drawparallels(circles,labels=[1,1,0,1])
# draw meridians
meridians = [-90,-60,-30,0,30]
m.drawmeridians(meridians,labels=[1,1,0,1])
title('Great Circle from New York to London')
show()