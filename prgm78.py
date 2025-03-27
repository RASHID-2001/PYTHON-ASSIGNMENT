"""
QN:Consider the above student.csv file with fields Name, Branch, Year, CGPA . Write python code using pandas to
1) To find the average CGPA of the students
2) To display the details of all students having CGPA > 9
3) To display the details of all CSE students with CGPA > 9
4) To display the details of student with maximum CGPA
5) To display average CGPA of each branch
	(June 2023)
"""
import pandas as pd  
df = pd.read_csv("student.csv")

# 1
average_cgpa = df["CGPA"].astype(float).mean()
print("Average CGPA of students:", average_cgpa)

# 2
students_above_9 = df[df["CGPA"].astype(float) > 9]
print("\nStudents with CGPA > 9:\n", students_above_9)

# 
cse_students_above_9 = df[(df["Branch"] == "CSE") & (df["CGPA"].astype(float) > 9)]
print("\nCSE students with CGPA > 9:\n", cse_students_above_9)

# 4
top_student = df.loc[df["CGPA"].astype(float).idxmax()]
print("\nStudent with maximum CGPA:\n", top_student)

# 5
avg_cgpa_by_branch = df.groupby("Branch")["CGPA"].astype(float).mean()
print("\nAverage CGPA of each branch:\n", avg_cgpa_by_branch)