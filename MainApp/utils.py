import pandas as pd
import json

# this method take 2 arguments 

def candel_create(df,tf):
    open = []
    close = []
    high = []
    low = []
    date = []
    id = []
    h=[]
    lo=[]
    for i in range(len(df.OPEN)):
        open.append(df.OPEN[i])
        close.append(df.CLOSE[i])
        high.append(df.HIGH[i])
        low.append(df.LOW[i])
        date.append(df.DATE[i])
    ct = tf
    o=open[::tf]
    c=close[tf-1::tf]
    d=date[::tf]

    k=0
    for i in range(len(high)+1):
        if i==0:
            h.append(max(high[i:tf]))
            lo.append(min(low[i:tf]))
        else:
            if tf>=len(high):
                break
            else:
                k+=ct
                tf+=ct
                h.append(max(high[k:tf]))
                lo.append(min(low[k:tf]))
    
    for i in range(len(h)):
        id.append(i+1)

    
    data =pd.DataFrame({'id':id,'open':o,'high':h,'low':lo,'close':c,'date':d})
    return data
    