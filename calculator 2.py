def main():
    while True:
        
        first_value = int(input ('Enter the first value:'))
        first_operator = input('write the first operator:')
        second_value = int(input ('Enter the second value:'))
        second_operator = input ('Enter the second operator:') 
        third_value = int(input ('Enter the third value:'))

        if((first_operator == '/') and (second_operator == '*')):
            fir = divide(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', multiply(fir, third_value))
            
            
        elif((first_operator == '/') and (second_operator == '+')):
            fir = divide(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', add(fir, third_value))

        elif((first_operator == '/') and (second_operator == '-')):
            fir = divide(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(fir, third_value))

        elif((first_operator == '/') and (second_operator == '/')):
            fir = divide(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', divide(fir, third_value))
##################################################################################
        
        elif((first_operator == '*') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', multiply(first_value, fir))
            
        elif((first_operator == '*') and (second_operator == '+')):
            fir = multiply(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', add(fir, third_value))

        elif((first_operator == '*') and (second_operator == '-')):
            fir = divide(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(fir, third_value))

        elif((first_operator == '*') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', multiply(fir, third_value))

###################################################################################

        elif((first_operator == '+') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', add(first_value, fir))
            
        elif((first_operator == '+') and (second_operator == '+')):
            fir = add(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', add(fir, third_value))

        elif((first_operator == '+') and (second_operator == '-')):
            fir = add(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(fir, third_value))

        elif((first_operator == '+') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', add(first_value, fir))

#################################################################################
        
        elif((first_operator == '-') and (second_operator == '/')):
            fir = divide(second_value, third_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(first_value, fir))
            
        elif((first_operator == '-') and (second_operator == '+')):
            fir = add(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(fir, third_value))

        elif((first_operator == '-') and (second_operator == '-')):
            fir = add(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(fir, third_value))

        elif((first_operator == '-') and (second_operator == '*')):
            fir = multiply(first_value, second_value)
            print(f'Answer for {first_value} {first_operator} {second_value} {second_operator} {third_value} equation is :', subtract(first_value, fir))

        
        else:
            print(f'wrong')

        quit()





if __name__ =="__main__":
    main()