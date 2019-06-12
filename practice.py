''' Given an array a of numbers and a target value t, 
find two numbers that sum to t (that is, a[i] + a[j] = t).'''


array = [2, 4, 19, 9, 3, 1 ,7]



def target_pair_sum(n):
    curr_val = 0
    upcom_val = 0
    found = False

    while found != True:
        if upcom_val <= len(array):
            upcom_val += 1
        
        if upcom_val == len(array):
            curr_val += 1
            upcom_val = curr_val + 1

        # adds pairs
        result = array[curr_val] + array[upcom_val]

        # Prints out every result
        # print(str(result) + '=' + str(array[curr_val]) + '+' + str(array[upcom_val]))

        if result == n:
            found == True
            return [array[curr_val],array[upcom_val]]


if __name__ == '__main__':
    print('Answer: ' + str(target_pair_sum(20)))
