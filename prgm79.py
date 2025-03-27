QN:Write Python program to write the data given below to a CSV file named student.csv
fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [ ['Nikhil', 'CSE', '2', '8.0'],
['Sanchit', 'CSE', '2', '9.1'],
['Aditya', 'IT', '2', '9.3'],
['Sagar', 'IT', '1', '9.5']]
(June 2023)
"""
import pandas as pd  
fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [
    ['Nikhil', 'CSE', '2', '8.0'],
    ['Sanchit', 'CSE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'IT', '1', '9.5']
]
df = pd.DataFrame(rows, columns=fields)
df.to_csv("student.csv", index=False)
print("CSV file 'student.csv' has been created successfully!")