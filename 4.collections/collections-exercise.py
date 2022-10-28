books={"Author 1":"Book 1","Author 2":"Book 2","Author 3":"Book 3"}
author=input("Please enter Author's name: ")

if(author=="Author 1"):
	print(books["Author 1"])
elif(author=="Author 2"):
	print(books["Author 2"])
elif(author=="Author 3"):
	print(books["Author 3"])
else:
	print("Doesn't exist")

for key,value in sorted(books.items()):
	print (value)

'''
def main():
	while True:
		option=menu()

'''