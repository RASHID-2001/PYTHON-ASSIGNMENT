"""
QN: Write Python program to write the data given below to a CSV file(JANUARY 2024)
	  Name 		Age 	City 		Occupation 	Salary
	Ram Roy 	35 	Mumbai 		Teacher 	75,000
	Jack Tom 	37 	Delhi 		Doctor 		90,000
	Susan Jit 	33 	Chennai 	Engineer 	85,000
	Jilt Joy 	40 	Kolkata 	Architect	70,000

"""
import pandas as pd  

data = {
    "Name": ["Ram Roy", "Jack Tom", "Susan Jit", "Jilt Joy"],
    "Age": [35, 37, 33, 40],
    "City": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
    "Occupation": ["Teacher", "Doctor", "Engineer", "Architect"],
    "Salary": ["75,000", "90,000", "85,000", "70,000"]
}

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

print("CSV file 'data.csv' has been created successfully!")
