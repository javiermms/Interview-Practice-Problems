'''Given a 32-bit signed integer, reverse digits of an integer.'''

def reverse(x: int) -> int:
    x = str(x)
    string = ''

    # checks to see if number is negative
    if x[0] == '-':
            string += x[0]
    
    # reverse string of ints
    for index in x[::-1]:
        # skips the negatuve sign or zero at the end of string
        if index != '-' and x[len(x)-1] != 0:
            string += str(index)
    
    number = int(string)
    
    # checks to see if its within range
    if number >= 2147483648 or number <= -2147483648:
        return 0 
        
    return number

if __name__ == '__main__':
    print(reverse(-101010101010101010101010101010))