#File I/O in python
#Python can be used to perform operations on a file .(read and write data )

"""
Types of all files:
1. Text files: .txt, .docx, .log etc --> forms in characters

2. Binary files: .mp4, .mov, .png, .jpg, .jpeg etc
 * All types of data store in memory by bits
Learn This Chapter;
 How can we open a file?
 How can we read data from a file?
 How can we write some data to a file?
 How can we close a file?
 How can we delete a file?


Open,read and close file:
we have to open a file before reading or writing.

f=open("file_name","mode")

file_name-> sample.txt/demo.docx
mode->r->read,w->write,a->append
mode-> if we don't specify the mode, it will be read by default.

r=open for reading
w=open for writing,truncating the file first
x=create a new file and open it for writing
a=open for writing, appending to the end of the file if it exits
b=binary mode
t=text mode(default)
+=open a disk for updating(reading and writing)
"""

