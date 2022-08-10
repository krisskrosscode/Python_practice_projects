from argparse import FileType
from class_data import data

filename = "new_file5.txt"
filetype = filename.split(".")[1]
date = '27-07-2022'
size = 23

file1 = data(filename, filetype, date, size)

file1.file_open(filename)

# count = 1
# append_text = "This is append number " + str(count)
file1.file_append(filename, "This is the nth time i am appending")

file1.file_read(filename)