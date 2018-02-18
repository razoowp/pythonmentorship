
## Write a python program to print a triangle of asterisk

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print("\n")
    print('')

   #output
'''*
   **
   ***
   ****
   *****'''

    '''print("Asterisk triangle")
    for g in range(11, 0, -1):
        print(g * ' ' + (11 - g) * '*')'''