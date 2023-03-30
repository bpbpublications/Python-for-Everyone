import pandas as mypd

# creating a Pandas Series
mylist = [11, 12, 13, 14, 15]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])
print(mypd_series)
print('-'*50)

# filtering the Pandas Series using Boolean indexing
my_bool_filter = mypd_series > 3
print(my_bool_filter)
print('-'*50)

my_filtered_mypdseries = mypd_series[my_bool_filter]
print(my_filtered_mypdseries)