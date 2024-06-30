def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers= [0] * 5 #listing 5 zeros for the user to input values
    total=0 #the variable will = 0
    for i in range(len(numbers)): #loop through the index of the list
        numbers[i] = int(input('Enter a value '))
    for num in numbers:
        total += num
    print(total)
    

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
