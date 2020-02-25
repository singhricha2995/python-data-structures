fname=input('Enter the file name:')
fn=open(fname,'r')
for lines in fn:
    print(lines.rstrip().upper())
