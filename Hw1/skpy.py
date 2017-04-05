import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

FilePath = '../yellow_tripdata_2016-05.csv'

dataset = pd.read_csv( FilePath ).tail(200000)

#df = zip(dataset["pickup_latitude"] , dataset["pickup_longitude"])
plt.axis([-180,180,-180,180])
plt.plot( dataset["pickup_latitude"] , dataset["pickup_longitude"] , 'b.' )

plt.show()

#db = DBSCAN( eps = 0.25 , min_samples = 100 ).fit(df)

#lb = db.labels_

#core_mask = np.zeros_like( lb , dtype = bool )
#core_mask[db.core_sample_indices_] = True

#cluster_num = len(set(lb)) - (1 if -1 in lb else 0)

#ulb = set(lb)
#color = plt.cm.Spectral(np.linspace(0,1, len(ulb)))

#for k , col in zip(ulb , color):
#    if k == -1:
#        col = 'k'

#    class_mask = ( lb == k )

#    xy = df[class_mask & core_mask]
#    plt.plot( xy[: , 0] , xy[: , 1] , 'o' , markerfacecolor = col,
#            markeredgecolor='k', markersize=14)

#plt.show()
