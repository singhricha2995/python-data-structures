Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name)>1:name='mbox-short.txt'
fn = open(name)
lst=list()
for lines in fn:
    if not lines.startswith('From:'):continue
    words=lines.split()
    email=words[1]
    lst.append(email)
aa=dict()
for email in lst:
    aa[email]=aa.get(email,0)+1
    
bigword=None
bigcount=None
for words,count in aa.items():
    if bigcount is None or count>bigcount:
        bigword=words
        bigcount=count
print(bigword,bigcount)
