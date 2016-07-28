file=open("gender.py","r+")
file.write("Enter your name in the file gender")
str=file.read(60)
def check():
        datafile = file('gender.py')
        found = False #this isn't really necessary 
        for line in datafile:
	 if blabla in line:
                #found = True #not necessary 
                return True
	 else:
		return False #because you finished the search without finding anything


print check()

file.close()
