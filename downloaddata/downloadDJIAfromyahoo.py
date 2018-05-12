import numpy as np
from pandas_datareader import data as wb
import fix_yahoo_finance as yf



yf.pdr_override()
#DJ = wb.get_data_yahoo("DJI", start="2015-05-01", end="2018-05-01")

from yahoo_historical import Fetcher
data = Fetcher("VZ", [2015,5,1], [2018,5,2], '1mo')
print(data.getHistorical().ix[:,[0,5]])
data.getHistorical().ix[:,[0,5]].to_csv("/Users/adityaprasann/IdeaProjects/PythonProj/downloaddata/temp.csv")

import csv
with open("/Users/adityaprasann/IdeaProjects/PythonProj/downloaddata/temp.csv","rt") as source:
    rdr= csv.reader( source )
    with open("/Users/adityaprasann/IdeaProjects/PythonProj/downloaddata/VZ.csv","wt") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[1], r[2]))



#print(DJ.head())