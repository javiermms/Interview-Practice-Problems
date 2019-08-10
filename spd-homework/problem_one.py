n = [4, 5, 6,7 ,8 ,4, 3]

dict = dict()

def any_duplicates(array):
    for element in array:
    
        if element in dict:
            return True
        else:
            dict[element] = element

    return False

print(any_duplicates(n))

