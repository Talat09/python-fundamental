file=open("sample.txt","r+")
#r+ mode is used to read and write a file. here file don't deleted.r+ mode is overwrite starting of the pointer
file.write("abc")
file.close()
#w+ mode is used to write and read a file. here file  deleted.