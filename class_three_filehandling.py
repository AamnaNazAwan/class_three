#for opening any file
#file = open("practice.txt",'r')

#READING FILE
infile = "practice.txt"

with open(infile) as f1:
    for l in f1:
        print(l)

#WRITTING TO A FILE
with open('practice.txt','w') as file:
    file.write("you excel")


#READING FROM A FILE
with open('practice.txt','r') as file:
    content = file.read()
    print(content)

#APPENDING THE FILE
with open('practice.txt','r') as file:
    file.write("\nAppending a new line.")

#CLOSING A FILE
file = open('practice.txt','r')
#perform the operation
file.close()


#performing readlines()
#performing writelines()
#how to remove lines from file