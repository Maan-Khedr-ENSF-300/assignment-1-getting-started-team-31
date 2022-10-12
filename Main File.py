##Assignmnet 1
## Sayma Sayed- 30161459 , Shahnoor Rakin- 30140555, Sudarshan Naicker- 30162797




def add(x,y):
    return x + y
  

def subtract(x,y):
    return x - y
  
def multiply(x,y):
    return x * y

def divide(x,y):
    return x // y

def intval(x):

    while True:
        try:
            x = int(input ('Enter the first value:'))


        except ValueError:
            print(f'your entered value is not an integer \n try again!')
            continue
        else:
            return (x)
            break




def main ():
    while True:
        
        first_value = int(intval)(input ('Enter the first value:'))
        first_operator = input('write the first operator:')
        second_value = int(input ('Enter the second value:'))
        second_operator = input ('Enter the second operator:') 
        third_value = int(input ('Enter the third value:'))

        if((first_operator == '/') and (second_operator == '*')):
            fir = divide(first_value, second_value)
            print(f'Answer is :', multiply(fir, third_value))
            
            
        elif((first_operator == '/') and (second_operator == '+')):
            fir = divide(first_value, second_value)
            print(f'sub:', add(fir, third_value))

        elif((first_operator == '/') and (second_operator == '-')):
            fir = divide(first_value, second_value)
            print(f'sub:', subtract(fir, third_value))

        elif((first_operator == '/') and (second_operator == '/')):
            fir = divide(first_value, second_value)
            print(f'sub:', divide(fir, third_value))
##################################################################################
        
        elif((first_operator == '*') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer is :', multiply(first_value, fir))
            
        elif((first_operator == '*') and (second_operator == '+')):
            fir = multiply(first_value, second_value)
            print(f'sub:', add(fir, third_value))

        elif((first_operator == '*') and (second_operator == '-')):
            fir = divide(first_value, second_value)
            print(f'sub:', subtract(fir, third_value))

        elif((first_operator == '*') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'sub:', multiply(fir, third_value))

###################################################################################

        elif((first_operator == '+') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer is :', add(first_value, fir))
            
        elif((first_operator == '+') and (second_operator == '+')):
            fir = add(first_value, second_value)
            print(f'sub:', add(fir, third_value))

        elif((first_operator == '+') and (second_operator == '-')):
            fir = add(first_value, second_value)
            print(f'sub:', subtract(fir, third_value))

        elif((first_operator == '+') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'sub:', add(first_value, fir))

#################################################################################
        
        elif((first_operator == '-') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer is :', subtract(first_value, fir))
            
        elif((first_operator == '-') and (second_operator == '+')):
            fir = add(first_value, second_value)
            print(f'sub:', subtract(fir, third_value))

        elif((first_operator == '-') and (second_operator == '-')):
            fir = add(first_value, second_value)
            print(f'sub:', subtract(fir, third_value))

        elif((first_operator == '-') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'sub:', subtract(first_value, fir))

        
        else:
            print(f'wrong')

        quit()



if __name__ =="__main__":
    main()
