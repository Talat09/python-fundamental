# file=open("demo.txt","w")
# file.write("I want to learn javascript tomorrow.Then i will learn React js.")#overwrite the entire file
file=open("demo.txt","a")#append the data to the end of the file
file.write("\nAfter that i will learn python.")
file.close()