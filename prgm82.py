"""
QN:(JUNE 2022)
columns(name, gender, start_date ,salary, team).
Write commands to do the following using panda library.
1. print first 7 records from employees file
2. print all employee names in alphabetical order
3. find the name of the employee with highest salary
4. list the names of male employees
5. to which all teams employees belong
"""
import pandas as pd


df = pd.read_csv("employees.csv")

# 1
print("\nFirst 7 records of employees:")
print(df.head(7))

#2
sorted_names = df["name"].sort_values()
print("\nEmployee names in alphabetical order:")
print(sorted_names)

#3
highest_salary = df.loc[df["salary"].idxmax(), "name"]
print("\nEmployee with highest salary:", highest_salary)

#4
male_employees = df[df["gender"] == "Male"]["name"]
print("\nNames of male employees:")
print(male_employees)

#5
unique_teams = df["team"].unique()
print("\nTeams employees belong to:")
print(unique_teams)
		
