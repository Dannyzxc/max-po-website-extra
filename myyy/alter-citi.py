import os

print('current working directory is:  ' + os.getcwd())


with open('citi.txt', 'r') as f:
    b = f.read()          
    print(b)
    f.close()

