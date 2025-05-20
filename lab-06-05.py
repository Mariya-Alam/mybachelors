# from statistics import median, variance
#
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy.matrixlib.defmatrix import matrix
# #ques 1
# matrix_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# matrix_b = np.array([[10,11],[12,13],[14,15]])
#
# result_matrix = np.dot(matrix_a,matrix_b)
#
# print("Matrix A:\n",matrix_a)
# print("Matrix_B:\n",matrix_b)
# print("\nResultant Matrix:\n",result_matrix)
# print("\nShape of Resultant Matrix:",result_matrix.shape)
#
# #ques 2
# data = np.array([1,2,3,4,5,6,7,8,9,10])
# mean = np.mean(data)
# median = np.median(data)
# std_dev = np.std(data)
# variance = np.var(data)
#
# print(
#     f"Data:\n{data}\n\nMean:{mean}\nMedian:{median}\nStandard Deviation:{std_dev}\nVariance:{variance}"
# )
#
# #ques 3
# data = np.random.rand(1000)
#
# plt.hist(data,bins=30,color = 'blue',edgecolor = 'black')
# plt.title("Histogram of random data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()
#
#
# #ques 4
# data = np.arange(12)
# try:
#     reshaped_data = data.reshape(2,6)
#     print("Original Array:\n",data)
#     print("\nReshaped Array:\n",reshaped_data)
# except ValueError as e:
#     print("Reshaping not possible:",e)
#
# #ques 5
#
# data = np.array([1,2,3,4,5,6,7,8,9,10])
#
# filtered_data = data[data>5]
#
# print("Original Array:\n",data)
#
# print("\nFiltered Array(elements>5):\n",filtered_data)
#
# #ques 6
#
# data = np.array([1,2,3,4,5])
# modified_data = data+10
#
# print("Original Array:\n",data)
#
# print("\nModified Array(after broadcasting):\n",modified_data)
#
#
# #ques 7
# data = np.array([[1,2,3],[4,5,6]])
# np.savetxt("my_array.txt",data)
# loaded_data = np.loadtxt("my_array.txt")
# print("Original Array:\n",data)
# print("\nLoaded Array:\n",loaded_data)
# print("\nArrays are equal:",np.array_equal(data,loaded_data))
#

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a small 3x3 RGB image
# img = np.zeros((5, 5, 3), dtype=np.uint8)  # Initialize with all zeros (black)
#
# # --- Pixel Locations ---
# # (row, column)
# top_left     = (0, 0)
# top_middle   = (0, 1)
# top_right    = (0, 2)
# far_top_left = (0,3)
# mmm = (0,4)
#
# middle_left  = (1, 0)
# middle_middle= (1, 1)
# middle_right = (1, 2)
# ddd = (1,3)
# nnn = (1,4)
#
# bottom_left  = (2, 0)
# bottom_middle= (2, 1)
# bottom_right = (2, 2)
# bottom_far_right = (2,3)
# ooo = (2,4)
#
# eee = (3,0)
# fff =(3,1)
# ggg = (3,2)
# hhh = (3,3)
# ppp = (3,4)
#
# iii = (4,0)
# jjj = (4,1)
# kkk = (4,2)
# lll = (4,3)
# qqq = (4,4)
# # --- Color Definitions ---
# red   = [255, 0, 0]
# green = [0, 255, 0]
# blue  = [0, 0, 255]
# white = [255, 255, 255]
# black = [0, 0, 0]
# magenta = [255, 0, 255]
# cyan = [0, 255, 255]
# yellow = [255, 255, 0]
#
# # --- Manipulating Pixels ---
#
# # First Row
# img[top_left]     = white       # Top-left pixel to red
# img[top_middle]   = black     # Top-middle pixel to green
# img[top_right]    = white      # Top-right pixel to blue
# img[far_top_left] = black
# img[mmm] = white
#
# # Second Row
# img[middle_left]  = black    # Middle-left pixel to yellow
# img[middle_middle]= white   # Center pixel to magenta
# img[middle_right] = black      # Middle-right pixel to cyan
# img[ddd] = white
# img[nnn] = black
#
# # Third Row
# img[bottom_left]  = white     # Bottom-left pixel to white
# img[bottom_middle]= black # Gray
# img[bottom_right] = white     # Bottom-right pixel to black
# img[bottom_far_right] = black
# img[ooo] = white
#
# # Forth Row
# img[eee]  = black     # Bottom-left pixel to white
# img[fff]= white # Gray
# img[ggg] = black     # Bottom-right pixel to black
# img[hhh] = white
# img[ppp] = black
#
# #fifth row
# img[iii]  =  white    # Bottom-left pixel to white
# img[jjj]= black# Gray
# img[kkk] = white     # Bottom-right pixel to black
# img[lll] = black
# img[qqq] = white
# # --- Display the Image ---
# plt.imshow(img)
# plt.title("Manipulated 3x3 RGB Image")
# # plt.axis('off')  # Hide axes
# plt.show()

# # --- Explanation ---
# print("Explanation:")
# print("- `img[row, column] = [R, G, B]` sets the color of the pixel at the specified row and column.")
# print("- `R`, `G`, and `B` are the red, green, and blue color components, ranging from 0 to 255.")
# print("- The pixel locations (top_left, middle_middle, etc.) are defined as tuples (row, column) for clarity.")
# print("- You can change the colors and pixel locations to experiment with different patterns.")



import numpy as np
import matplotlib.pyplot as plt
# a=np.arange(25)
# print(a)
# print("\n")
# print(a[::2])
# print("\n")
# print(a[1::2])
# print("\n")
# #print(a[::2,::2])#??
# a_2d = a.reshape(5, 5)
# print(a_2d)
# print("\n")
# print(a_2d[::2, ::2])
# print("\n")
# print(a_2d[1::2, 1::2])
#
# result = a_2d[::2, :][:, [1,3]]
# print(result)
# result = a_2d[::2,][:,[1,3]]
# print(result)

#
# chekarboard = np.zeros((5, 5, 3), dtype=np.uint8)
# black = [0,0,0]
# white = [255,255,255]
# for i in range(5):
#     for j in range(i):
#        if  i + j % 2 ==0 :
#            chekarboard[i,j] = white
#        else:
#            chekarboard[i,j] = black
#
# print(chekarboard)
# plt.imshow(chekarboard)
# plt.show()


# from PIL import Image
# img = plt.imread('Skz wallpaper.jpeg')
# img = Image.open('Skz wallpaper.jpeg')
# img_array = np.array(img)
# plt.imshow(img)
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# from fontTools.ttLib.tables.ttProgram import Program
# from sympy import false
#
# data = {
#     'StudentId' : [1,2,3,4,5],
#     'Name' : ['Rahim','Karim','Jalila','farida','Dalil'],
#     'Age' : [32,52,34,64,'NAN'],
#     'Gender' : ['male','male','female','female','male'],
#     'Program' : ['Physics','chemistry','Biology','Math','Art'],
#     'Registration date' : ['2020-09-19','2000-09-19','2019-09-19','1991-09-19','2025-09-19'],
#     'Status' : ['A','D','D','D','A']
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# df.to_csv('student.csv', index = False)
#
# df_loaded = pd.read_csv('student.csv')
# print(df_loaded.isnull().sum())

# PY lAB 20/05/25

import pandas as pd
import matplotlib.pyplot as plt
from fontTools.ttLib.tables.ttProgram import Program
from numpy.ma.core import product
from sympy import false, latex, rotations

data = pd.read_csv('supermarket_sales.csv')
print(data.columns)

df = pd.DataFrame(data)

total_sales = df['Total'].sum()
print(f'Total Sales :{total_sales}')

average_unit_price = df['Unit price'].mean()
print(f'Average Unit Price:{average_unit_price}')

unique_customers = df['Invoice ID'].nunique()
print(f'Unique Customers:{unique_customers}')

max_rating = df['Rating'].max()
min_rating = df['Rating'].min()
print(f'Max Rating:{max_rating},Min Rating:{min_rating}')

total_quantity = df['Quantity'].sum()
print(f'Total quantity sold:{total_quantity}')

most_common_payment = df['Payment'].mode()[0]
print(f'Most Common payment method:{most_common_payment}')

gender_counts = df['Gender'].value_counts()
print(gender_counts)

customer_type_counts = df['Customer type'].value_counts()
print(customer_type_counts)

# df['DateTime'] = pd.to_datetime(df['Date'] + '' + df['Time'])
# print(df['Date'])
# daily_sales = df.groupby(df['DateTime'].dt.date)['Total'].sum()
# plt.figure(figsize=(10,5))
# plt.plot(daily_sales.index,daily_sales.values,marker = 'o')
# plt.title('Daily Sales Trend')
# plt.xlabel('Date')
# plt.ylabel('Total Sales')
# plt.xticks(rotation= 45)
# plt.grid()
# plt.show()

payment_methods  = df['Payment'].value_counts()
plt.figure(figsize=(8,5))
payment_methods.plot(kind = 'bar')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.xticks(rotation = 45)
plt.grid(axis='y')
plt.show()

gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8,5))
gender_counts.plot(kind = 'pie',autopct = '%1.1f%%',startangle = 90)
plt.title('Customer Gender Distribution')
plt.ylabel('')
plt.show()

customer_type_counts = df['Customer type'].value_counts()
plt.figure(figsize=(8,5))
customer_type_counts.plot(kind = 'bar')
plt.title('Customer Type Distribution')
plt.xlabel('Customer Type')
plt.ylabel('Number of Customers')
plt.xticks(rotation = 0)
plt.grid(axis = 'y')
plt.show()

sales_per_branch = df.groupby('Branch').agg({'Total':'sum','Invoice ID':'count'})
sales_per_branch.columns = ['Total sales','Number of Transactions']
print(sales_per_branch)

customer_demographics = df.groupby(['Gender','Customer type']).size().unstack()
print(customer_demographics)

product_line_analysis = df.groupby('Product line').agg({'Total':'sum','gross margin percentage':'mean'})
print(product_line_analysis)

unit_price_impact = df[['Unit price','Total']].corr()
print(unit_price_impact)

average_quantity = df['Quantity'].mean()
print(f'Average Quantity Sold:{average_quantity}')

tax_contributions = df.groupby('Branch')['Tax 5%'].sum()
print(tax_contributions)

# df['DateTime'] = pd.to_datetime(df['Date']+''+df['Time'])
# daily_sales = df.groupby(df['DateTime'].dt.date)['Total'].sum()
# print(daily_sales)

payment_methods = df['Payment'].value_counts()
print(payment_methods)

ratings_correlation = df[['Rating','Total']].corr()
print(ratings_correlation)

gross_margin_analysis = df.groupby('Product line')['gross margin percentage'].mean()
print(gross_margin_analysis)

cogs_analysis = df.groupby('Product line').agg({'cogs':'sum','Total':'sum'})
print(cogs_analysis)

Q1 = df['Total'].quantile(0.25)
Q3 = df['Total'].quantile(0.75)
IQR = Q3-Q1
outliers = df[(df['Total']<(Q1-1.5*IQR))|(df['Total']>(Q3+1.5*IQR))]
print(outliers)










