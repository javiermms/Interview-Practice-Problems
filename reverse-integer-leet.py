'''Given a 32-bit signed integer, reverse digits of an integer.'''

def reverse(x: int) -> int:
    x = str(x)
    string = ''
    
    if x[0] == '-':
            string += x[0]
            
    for index in x[::-1]:
        if index != '-' and x[len(x)-1] != 0:
            string += str(index)
            
    if int(string) >= 2147483648 or int(string) <= -2147483648:
        return 0 
        
    return int(string)

if __name__ == '__main__':
    print(reverse(-101010101010101010101010101010))