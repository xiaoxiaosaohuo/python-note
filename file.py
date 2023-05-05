# r open a file for reading
# w open a file for writing
# x open a file for exclusive creation, if the file already exists, the operation fails
# a open a file for appending at the end of the file without truncating it
# t open in text mode
# open in binary mode
# + open a file for updating(reading and writing)
file1 = open('test.txt')

# read the file
read_content = file1.read()
print(read_content)
file1.close()


# Exception handling in files

try:
    file1 = open('test.txt','r')
    read_content = file1.read()
    print(read_content)
finally:
    file1.close()



with open('test.txt','r') as file1:
    read_content = file1.read()
    print(read_content)

# write to files

with open('test2.txt','w') as file2:
    file2.write('programming is fun.\n')
    file2.write("let's go")

# create the generator object
squares_generator = (i * i for i in range(5))
for i in squares_generator:
    print(i)

def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())