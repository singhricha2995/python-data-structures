#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

fname=input('Enter the file name:')
fn=open(fname,'r')
for lines in fn:
    print(lines.rstrip().upper())
