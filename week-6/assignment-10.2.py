Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours=dict()

for lines in handle:
    lines.rstrip()
    if not lines.startswith("From "):continue
    words=lines.split()
    
    words=words[5].split(":")
    hours[words[0]]=hours.get(words[0],0) + 1

lst=[]

for h,s in hours.items():
    lst.append((h,s))
    
lst.sort()

for h,s in lst:
    print(h,s)
