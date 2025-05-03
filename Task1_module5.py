try:
    file=input('Enter the file name to be opened :')
    file1=open(file,'r')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print('Enter a valid file name')
