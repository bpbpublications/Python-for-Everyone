import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])
print(mypd_series)
print('-'*50)

# applying a function to each element of the Pandas Series
def mycube(mynum):
    return mynum ** 3

mycube_pdseries = mypd_series.apply(mycube)
print(mycube_pdseries)