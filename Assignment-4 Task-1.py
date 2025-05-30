#Task 1: Read a File and Handle Errors

# file = open('sample.txt', 'r')
# reading_file = file.read()
# print(reading_file)
# file.close()

try:
     file = open('sample.txt' 'r')
     reading_file = file.read()
     print(reading_file)
     file.close()
except FileNotFoundError:
     print('The file sample.txt was not found.')

