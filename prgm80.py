"""
QN: Write Python program to write the data given below to a CSV file.(JANUARY 2024)
Sl No. 		   Title                         Author 	            Available 	    Count
  1 		The Great                 Gatsby F. Scott Fitzgerald            Y 	      20
  2 		Pride and Prejudice       Jane Austen                            Y 	      15
  3 		The Time Machine          H.G. Wells                             N 	       0
"""
import pandas as pd  
fields = ['Sl No.', 'Title', 'Author', 'Available', 'Count']
rows = [
    [1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Y', 20],
    [2, 'Pride and Prejudice', 'Jane Austen', 'Y', 15],
    [3, 'The Time Machine', 'H.G. Wells', 'N', 0]
]
df = pd.DataFrame(rows, columns=fields)
df.to_csv("books.csv", index=False)
print("CSV file 'books.csv' has been created successfully!")

