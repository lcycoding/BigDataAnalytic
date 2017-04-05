import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import folium
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors


def get_cmap(N):

    color = colors.Normalize( vmin = 0 , vmax = N-1 )
    scalar_map = cmx.ScalarMappable( norm=color , cmap='nipy_spectral' )
    def map_to_rgb(index):
        return scalar_map.to_rgba(index)
    return map_to_rgb

FilePath = '../yellow_tripdata_2016-05.csv'

dataset = pd.read_csv( FilePath )

print("There are %d rows." , len(dataset) )

coord = dataset.as_matrix(columns=['pickup_latitude','pickup_longitude'])

'''
DBSCAN FOCUS
'''

kpr = 6371.0088
epsi = 1.25 / kpr
db = DBSCAN( eps = epsi , min_samples = 10, algorithm='ball_tree' , metric='euclidean' ).fit( np.radians(coord) )

c_labels = db.labels_
num = len(set(c_labels))
cluster = \
    pd.Series([coord[c_labels == n] for n in range(-1 , num)])

plt.figure(figsize = (12, 12))

m = Basemap(projection='merc', resolution='l', epsg = 4269,
            llcrnrlon=-76,llcrnrlat=39.8, urcrnrlon=-71.5,urcrnrlat=42)

uni_lab = np.unique( c_labels )
cmaps = get_cmap(num)

for i , col in enumerate(cluster):
    lon_select = col[:, 1]
    lat_select = col[:, 0]
    x, y = m( coord[:, 1] , coord[:, 0]  )
    m.scatter(x,y,5,marker='o',color='b',zorder =10)

m.arcgisimage(service='World_Shaded_Relief', xpixels = 5000 , verbose = False)
plt.show()
