'''import numpy as np
a = np.array([[1, 4, 2], 
[3, 4, 6], 
[0, -1, 5]]) 
# sorted array 
print ("Array elements in sorted order:\n", 
np.sort(a, axis = None)) 
# sort array row-wise 
print ("Row-wise sorted array:\n", 
np.sort(a, axis = 1)) 
# specify sort algorithm 
print("Column wise sort by applying mergesort:\n", 
np.sort(a, axis = 0, kind = 'mergesort')) 

dtypes = [('name', 'S10'), 
('grad_year', int), ('cgpa', float)] 
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), 
('Ajay', 2008, 8.7),
('Pankaj', 2008, 7.9), ('Aakash', 
2009, 9.0)] 
# Creating array 
arr = np.array(values, dtype = 
dtypes) 
print ("\nArray sorted by names:\n", 
np.sort(arr, order = 'name')) 
print ("Array sorted by graduation year and then cgpa:\n", np.sort(arr, 
order = ['grad_year', 'cgpa']))'''
'''
import array as arr    
a = arr.array('i',[1,3,4,5,66])
print("First element is:", a[0])    
print("Second element is:", a[1])   
print("Third element is:", a[2])  
print("Forth element is:", a[3])  
print("last element is:", a[-1])    
print("Second last element is:", a[-2])    
print("Third last element is:", a[-3])    
print("Forth last element is:", a[-4])    
print(a[0], a[1], a[2], a[3], a[-1],a[-2],a[-3],a[-4])  

'''
import pandas as pd
print(pd.__version__)




'''
import sys    
# Here, we are printing the path using sys.path    
print("Path of the sys module in the system is:", sys.path)
'''
