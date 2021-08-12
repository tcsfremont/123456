import sys

n = int(sys.argv[1])

if n % 2 == 1:

    print("not weird")

elif n in range (6,21):

    print("weird")

elif n in range(2,6):

    print("not weird")

else:

    print("weird")
