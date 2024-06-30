def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0 # total start off by being 0
    i=0 # i and 0 are the same thing in this equation
    while i < 5: 
    #while will work if the condition is true, meaning if i is less than 5 numbers
        num = int(input('Enter your input: ')) #num = the input of the user
        total += num # this will add the total amount to the num amount
        i+=1 # this increments the value of i By 1, IE i = i + 1
    # the purpose of i+=1 is ensure that loop will eventually stop
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
