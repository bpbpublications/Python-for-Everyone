import pandas as mypd

# creating a DataFrame from a dictionary of lists
mydict = {'myname': ['Alex', 'John', 'Michael', 'Tom'],
        'myage': [35, 45, 55, 65],
        'mycountry': ['UK', 'USA', 'Australia', 'Finland']}
mypd_dataframe = mypd.DataFrame(mydict)
print(mypd_dataframe)
print('-'*50)

# creating a DataFrame from a list of dictionaries
mylist = [{'myname': 'Alex', 'myage': 35, 'mycountry': 'UK'},
        {'myname': 'John', 'myage': 45, 'mycountry': 'USA'},
        {'myname': 'Michael', 'myage': 55, 'mycountry': 'Australia'},
        {'myname': 'Tom', 'myage': 65, 'mycountry': 'Finland'}]
my_pd_dataframe2 = mypd.DataFrame(mylist)
print(my_pd_dataframe2)