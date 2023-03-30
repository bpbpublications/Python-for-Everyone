import pandas as mypd

# creating a DataFrame from a dictionary of lists
mydict = {'myname': ['Alex', 'John', 'Michael', 'Tom'],
        'myage': [35, 45, 55, 65],
        'mycountry': ['UK', 'USA', 'Australia', 'Finland']}
mypd_dataframe = mypd.DataFrame(mydict)
print(mypd_dataframe)
print('-'*50)

# getting the second row of the DataFrame
print(mypd_dataframe.loc[1])
print('-'*50)

# getting the mycountry column of the DataFrame
print(mypd_dataframe['mycountry'])
print('-'*50)

# getting the subset of the DataFrame
print(mypd_dataframe.loc[0:2, ['myname', 'myage']])
print('-'*50)