fname=input()
lname=input()
age=(input())

if len(fname) and len(lname) > 5 :
    print((fname[0:2])+(lname[5])+(age[1]))
else :
    print((fname[0])+(age[0:2])+(lname[4]))