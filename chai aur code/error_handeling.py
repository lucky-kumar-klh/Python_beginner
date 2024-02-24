# 1st Method
'''
This method will create the file if not found, which leads to 
some misshappenings in file handeling
'''
file = open('test.txt', 'w')

# 2nd Method
'''
This method will try to write on a file, but If not found then
wil not excecute the command 
But Here, We need to close the file
'''
try:
    file.write('Writing on a file')
# except:
#     pass
finally:
    file.close()

# 3rd Method (Better)
'''
This is an alternative method of the above method with change in syntax
Here, File closing is automatically done    
'''
with open('test.txt', 'w') as file:
    file.write('Writing on a file')
