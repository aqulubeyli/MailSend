import sys
import csv
# import os


# # path = os.path.join("Data/dannie.csv")
# reader = csv.reader(open('../Data/dannie.csv'), delimiter=";")

# for Name, Email, Contry, Religion in reader:
#     if Contry=='' and Religion=='MUS':
#         print(Email)


def sort(Contry, Religion):
    # reader = csv.reader(open('../Data/dannie.csv'), delimiter=";")
    reader = csv.DictReader(open('../Data/dannie.csv'), delimiter=";")
    
    for row in reader:
        if row['Contry']==Contry or row['Religion']==Religion:
            print(row['Name'], row['Email'])
            # return row['Email']
        
        

   
if __name__ == "__main__":
    sort('','MUS')