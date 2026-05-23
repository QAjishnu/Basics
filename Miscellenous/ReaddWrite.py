file =open('test.txt')

#to read all the content of the file given.
#print(file.read())

#to read n number of characters by passing parameter
#print(file.read(6))

#read one single line at a time.
print(file.readline())

#print line by line using readline method
'''line = file.readline()
while line!="":
    print(line)
    line= file.readline()'''

#readlines method:
for line in file.readlines():
    print(line)




file.close()
