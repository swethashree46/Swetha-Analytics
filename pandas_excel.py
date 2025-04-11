import pandas as pd

# Read the data from excel file
df = pd.read_excel(r'swetha.xlsx')
print(df)
print(type(df))

# gives the total number of rows and columns in df variable
# print(df.shape)
#
# rows = df.shape[0]
# cols = df.shape[1]
# print("rows = " , rows)
# print("cols = " , cols)


# Extract the first n or last n rows using head and tail
# print(df.head(5))
# print("\n =================================== \n")
# print(df.tail(3))


# get or extract only the required columns this is equi to select coumns from table

# select single column
# res = df['name']
# res = df['age']
# print(res)

# select multiple columns
# res = df[['Academic']]
# print(res)


# slicing in DF
print(df[10:14])
print(df[14:20])


#### Till now we extracted the data from the excel file ##############



# create simple data frame and excel file

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# print(data)
# print(type(data))
#
# df = pd.DataFrame(data)
# print(df)
#
# df.to_excel(r'swetha.xlsx', index=False)
# df.to_csv(r'Faiz.csv', index=False)



# locate the row from DFor returs the row of the mentioned index
# df = pd.read_excel(r'sudeep.xlsx')
# print(df.loc[1])  # returns second row
# print(df.loc[[10,15,13]])
# print("\n \n ", df.loc[[0, 2 , 7 , 9]]) # returns first and sec row
# print("\n \n ", df.loc[[9,12,17,20]]) # returns first and sec row




#adding new column

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# print(type(data))
# df = pd.DataFrame(data)
# print(df)
#
# # # print("After adding column \n")
# df['time'] = [8,9,10]
# df['water'] = [3,4,3.5]
# df['steps'] = [3000,3500,4000]
#
#
# print(df)
#
# print("After deleting ")
# # #delete column
# df.drop(['duration','time'],axis=1,inplace=True)
# print(df)

# concatenate 2 DF


# import pandas as pd
#
# df_1 = pd.DataFrame(
#   [['ram', 68, 84, 78, 96],
#    ['krishna', 74, 56, 88, 85],
#    ['kalki', 77, 73, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# df_2 = pd.DataFrame(
#   [['satya', 72, 67, 91, 83],
#    ['thretha', 78, 69, 87, 92]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# print(df_1)
# print(df_2)
#
# frames = [df_1, df_2]
# # # # concatenate dataframes
# df = pd.concat(frames,ignore_index=True)
#
# # # print dataframe
# print("df_1\n------\n", df_1)
# print("\ndf_2\n------\n", df_2)
# print("\ndf\n--------\n", df)



#
# # another example of concatenate

# import pandas as pd
#
# df_1 = pd.DataFrame(
#   [['Somu', 68, 84, 78, 96],
#    ['Kiku', 74, 56, 88, 85],
#    ['Ajit', 77, 73, 82, 87]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# df_2 = pd.DataFrame(
#   [['Amol', 72, 67, 91, 83],
#    ['Lini', 78, 69, 87, 92]],
#   columns=['name', 'physics', 'chemistry', 'geometry', 'calculus'])
#
# frames = [df_1, df_2]
#
# # concatenate dataframes
# df = pd.concat(frames, sort=True, ignore_index=True)
#
# # print dataframe
# print("df_1\n------\n", df_1)
# print("\ndf_2\n------\n", df_2)
# print("\ndf\n--------\n", df)
#
# df.to_excel(r'sangeetha.xlsx',index=False)
#

### example to pick the data from 2 excelfiles and merge

# get max or min value


import pandas as pd

# mydictionary = {'physics': [68, 74, 77, 78],
#      'chemistry': [84, 56, 73, 69],
#      'algebra': [78, 88, 82, 87]}
#
# # Create DataFrame
# df_marks = pd.DataFrame(mydictionary)
# print('DataFrame\n----------')
# print(df_marks)
#
#
# # # # Calculate max along columns
# max_data = df_marks.max()
# print('\nMaximum Value\n------')
# print(max_data)
#
# min_data = df_marks.min()
# print('\nminimum Value\n------')
# print(min_data)
#
#
# maxdata = df_marks['physics'].max()
# print("Physics max value - " , maxdata)


# filter rows

# df_1 = pd.DataFrame(
#   [['Somu', 68, 84, 78, 96],
#    ['Kiku', 74, 56, 88, 85],
#    ['Ajit', 77, 73, 82, 87],
#    ['santhosh', 62, 65, 70, 77],
#    ['ramesh', 62, 65, 70, 32],
#    ['suresh', 62, 65, 70, 28]],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# print(df_1)
# print(df_1.shape)

# out = df_1['chemistry'].isin(range(50,70))
# resdf = df_1[out]
# print(resdf)
#
# out1 = df_1['calculus'].isin(range(0,35))
# resdf1 = df_1[out1]
# print(resdf1)
#
# out2 = df_1['calculus'].isin(range(80,90))
# resdf2 = df_1[out2]
# print(resdf2)





#### another example


# import pandas as pd



#
# df_1 = pd.DataFrame(
#   [['ram', 68, 84, 78, 96],
#    ['vishnu', 74, 56, 88, 85],
#    ['kiran', 77, 43, 82, 87],
#    ['ramesh', 62, 65, 70, 32],
#    ['suresh', 62, 65, 70, 28]
#    ],
#   columns=['name', 'physics', 'chemistry', 'algebra', 'calculus'])
#
# print(df_1)
# print(df_1.shape)
#
# resdf = df_1.query('algebra >= 80')
# print(resdf)
#
# resdf = df_1.query('chemistry == 65')
# print(resdf)
#
# resdf = df_1.query('calculus < 35')
# print(resdf)
#
# resdf = df_1.query('name = "')
# print(resdf)