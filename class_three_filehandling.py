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
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # .strip() removes the newline character at the end of each line


#performing writelines()
lines_to_write = ['First line\n', 'Second line\n', 'Third line\n']

with open('example.txt', 'w') as file:
    file.writelines(lines_to_write)
#how to remove lines from file
word_to_remove = 'remove'

# Step 1: Read lines from the file
with open('example.txt', 'r') as file:
    lines = file.readlines()

# Step 2: Filter out lines containing the specific word
filtered_lines = [line for line in lines if word_to_remove not in line]

# Step 3: Write the remaining lines back to the file
with open('example.txt', 'w') as file:
    file.writelines(filtered_lines)
