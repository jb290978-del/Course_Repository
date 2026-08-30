#while factorial loop
x = 1   #set initial value of x
y = int(input("Root: "))+1  #ask user for the value what they want to factorialise and add 1
output = 1  #initialise output value
while (x < y):  #create while loop as long as x is less than y
    output = output * x #multiply latest value of output by current x value
    print(output)   #print current output value
    x += 1 #increase value of x by 1
