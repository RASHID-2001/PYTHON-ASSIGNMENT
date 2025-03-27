"""
QN: Consider a CSV file 'students.csv' with columns such as 'student_id', 'name',
'gender', 'birth_date', and 'grade'. Write commands to do the following using
panda library.
1) Display the first 5 records
2) Print all student names in ascending alphabetical order
3) Print the name of the student with the highest grade
4) List the names of male students
(JANUARY 2024)
"""
import pandas as pd  

df = pd.read_csv("students.csv")

# 1
print("First 5 records:\n", df.head())

# 2
print("\nStudent names in ascending order:\n", df['name'].sort_values())

#3
top_student = df.loc[df['grade'].idxmax(), 'name']
print("\nStudent with highest grade:", top_student)

# 4
male_students = df[df['gender'] == 'Male']['name']
print("\nMale students:\n", male_students)