##In the name of God

# Get 10 number from user
numbers =[]
print ("Enter 10 numbers")

for i in range(0,10):
    number = input()
    number = int(number)
    numbers.append(number)

print ("---------------------------------")
# Set max of resulte and count  of primitve roots
max_number = 0
max_count = 0

# Dive in the numbers' set
for n in numbers:

    # Setting main values
    root = 2
    count = 0
    number = n # the number will divide by the finded primitve root

    while(number > 1):

        # Check if number is prime
        number_divisors_count = 0

        for i in range(1,number):
            if  number % i == 0:
                number_divisors_count += 1

        if number_divisors_count == 1 :

            # print (str(number) + " is prime!")
            count += 1
            # print ("now count is " + str(count))
            number = number // number #stop

        else:
            # print (str(number) + " is not prime!")

            # Check if root is prime
            root_divisors_count = 0

            for j in range(1,root):
                if  root % j == 0:
                    root_divisors_count += 1

            if root_divisors_count == 1 :

                # print (str(root) + " is prime!")

                # Check if number is divisible
                if number % root == 0:

                    # print (str(number) + " % " + str(root) + " == 0")
                    count += 1
                    # print ("now count is " + str(count))
                    number = number // root 

                    # Countinue division until number is not divisible by the primitve root
                    while number % root == 0:
                        number = number // root 

                else : #skip

                    # print (str(number) + " % " + str(root) + " != 0")

                    # Skipping the even numbers
                    if ( root == 2):
                        root += 1
                    else :
                        root += 2
                    # print ( " Now root is " + str(root))

            else: #skip

                # print (str(root) + " is not prime!")
                root += 1
                # print ( " Now root is " + str(root))

    print (str(n) + " , " + str(count))

    # Check if count is the maximum
    if (count > max_count):

        max_count = count
        max_number = n

    elif (n > max_number and count == max_count):

        max_number = n

# Results
print ("\n>>>> Resulte is : "+ str(max_number) + " whit " + str(max_count) + " primitve roots")

        
#by @JopperKing