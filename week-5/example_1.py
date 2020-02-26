#Find the most occuring word in the text file and print the number of times it appeared in the text.


fname=input('Enter the filename:')
handle = open(fname)
aa=dict()
for lines in handle:
    lines=lines.split()
    for words in lines:
        aa[words]=aa.get(words,0)+1
bigword=None
bigcount=None
for words,count in aa.items():
    if bigcount is None or count>bigcount:
        bigword=words
        bigcount=count
print(bigword,bigcount)
