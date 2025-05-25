with open('testfile.txt', 'r') as f:
    content = f.read(5) # print only 5 characters
    print(content) 
    
    # for line in f:
    #     print(line, end='') # prnt all lines ,end='' will remove the new line character 
    
    # fcontent = f.readlines()   #readlines() will read the file line by line
    # print(fcontent, end='')
# f = open('testfile.txt', 'r')
# print(f.name)

# f.close()

