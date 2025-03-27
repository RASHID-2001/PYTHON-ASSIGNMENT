"""
QN:MAY2023
Write Python program to write the following University topper data of CSE
branch to a CSV file.
	REG.NO			   NAME		SEMESTER		COLLEGE		CGPA
	ABC123			GANESH KUMAR   	   S8			   ABC		9.8
	ECH265			JOHN MATHEW	   S7			   ECH		9.9
	FET345			REENA K		   S6			   FET 		9.7
	GMT734			ADIL M		   S5			   GMT		9.75
"""
import pandas as pd

fields = ["REG.NO", "NAME", "SEMESTER", "COLLEGE", "CGPA"]
rows = [["ABC123", "GANESH KUMAR", "S8", "ABC", 9.8],
    ["ECH265", "JOHN MATHEW", "S7", "ECH", 9.9],
    ["FET345", "REENA K", "S6", "FET", 9.7],
    ["GMT734", "ADIL M", "S5", "GMT", 9.75]]

df = pd.DataFrame(rows, columns=fields)

df.to_csv("university_toppers.csv", index=False)

print("CSV file 'university_toppers.csv' has been created successfully!")