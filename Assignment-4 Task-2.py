#Task 2: Write and Append Data to a File

file1 = open('output.txt', 'w')
writing_file = input('Enter text to the file: ')
file1.write(writing_file)
print('Data successfully written to output.txt')
file1.close()

file1 = open('output.txt', 'a')
appending_file = input('Enter additional text to append: ')
file1.write('\n' + appending_file)
print('Data successfully appended')
file1.close()

file1 = open('output.txt', 'r+')
reading_file = file1.read()
print(reading_file)
file1.close()