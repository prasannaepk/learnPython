import time

i=1

while i<10:
    j = 1
    while j <= i:
        print '*',
        j += 1
    print "\n"
    i += 1

f = ["Hello", "world"]

for a in f:
    print a.islower()
    print a.upper()

def star(count,direction):
    if direction == "f":
        for i in range(1, count+1, 1):
            for j in range(1, i + 1, 1):

                print '*',
            print "\n"
            time.sleep(0.1)
    elif direction == "r":
        for i in range(count, 0,-1):
            for j in range(i, 0,-1):

                print '*',
            print "\n"
            time.sleep(0.1)
    else:
        print "Invalid direction\n"
j=1
while j>0:
    star(100,"r")
    star(100,"f")
