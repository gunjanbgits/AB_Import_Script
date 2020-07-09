from csv import DictReader
import io
import os
import shutil


# initializing bad_chars_list 
bad_chars = [';', ':', '!', "*", ",", "(", ")", "/"] 

# # printing original string  
# print ("Original String : " + test_string) 
        

parent = "works"
# Check if the Directory Exists
try:  
    os.mkdir(parent)
# Define the Path for the root text file for works folder
    filePath = os.path.join(parent, 'works.txt')
# Create the root file with the Default title
    file = io.open(filePath, "w", encoding='ISO-8859-1') 
    file.write("Title: Works") 
    file.close() 
except OSError as error:  
    print(error)
# open the csv file
with io.open('ab_export.csv', 'r', encoding='ISO-8859-1') as read_obj:
    csv_reader = DictReader(read_obj, delimiter=';')
# Get the Column Names 
    column_names = csv_reader.fieldnames
# Print the fist Column Name Just for Testing
    # print(column_names)
# Iterate over each line as a ordered dictionary from artbutler csv
    for index,row in enumerate(csv_reader, start=1):
        # initializing test string  
        test_string = row['Title'] + " " + row['Inventory Number']
        # using replace() to  
        # remove bad_chars  
        for i in bad_chars : 
            test_string = test_string.replace(i, '')
# Define the sub directory paths for the works
# Numbered Folders
#        directory = str(index) + "_" + "-".join(test_string.split(" "))
# Non Numbered Folders
        directory = "-".join(test_string.split(" "))
# Final Path for the directories
        path = os.path.join(parent, directory)
# Print Name of Works and Index
        print("-----------", "\n\n", index, " Work ", test_string)
# Get the Lenght of the columns
        col = len(row)
# Iterate over the columns of that row
        # for x in range(0, col):
        #     print(column_names[x], row[column_names[x]])
        # os.mkdir(path)
        try:  
            os.mkdir(path)
            filePathWork = os.path.join(path, 'work.txt')
            file = io.open(filePathWork, 'w', encoding='ISO-8859-1')
            for x in range(0, col):
                if column_names[x] == 'Image':
                    file.write("Cover: - " + row[column_names[x]].replace('binary/', '', 1) + "\n\n" + "----" + "\n\n")
                elif column_names[x] == 'Image(s)':
                    pass
                else:
                    file.write(column_names[x] + ": " + row[column_names[x]] + "\n\n" + "----" + "\n\n")
            file.close()
        # Copy Files
            imageList = row['Image(s)'].split(",")
            imageListLength = len(imageList)
            for x in range(0, imageListLength):
                # print(imageList[x])
                shutil.copy(imageList[x], path)
                imageListFileName = imageList[x].replace('binary/', '', 1) + ".txt"
                imageListPath = os.path.join(path, imageListFileName)
                print("Image(s) copied:", imageListFileName)
                file = io.open(imageListPath, "w", encoding='ISO-8859-1')
                file.write("Template: image" + "\n\n" + "----" + "\n\n" + "Caption: " + row['Title'])
                file.close()
            shutil.copy(row['Image'], path)
            imagetxtfilename = row['Image'].replace('binary/', '', 1) + ".txt"
            imagePath = os.path.join(path, imagetxtfilename)
            # print(imagetxtfilename)
            file = io.open(imagePath, "w", encoding='ISO-8859-1')
            file.write("Template: image" + "\n\n" + "----" + "\n\n" + "Caption: " + row['Title'])
            file.close()
        except OSError as error:  
            print(error)
print("-----------", "\n", "-----------", "\n", "Data parsing complete")