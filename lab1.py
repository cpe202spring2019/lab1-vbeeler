def max_list_iter(int_list):
    if int_list == []:
        return None
    elif int_list == None:
        raise ValueError
    maxval = int_list[0]
    for val in int_list:
        if val > maxval:
            maxval = val
    return maxval

def reverse_rec(int_list):
    if int_list == None:
        raise ValueError
    elif len(int_list) == 0:
       return []
    return reverse_rec(int_list[1:]) + [int_list[0]]

def bin_search(target, low, high, int_list):
    if int_list == None:
        raise ValueError
    mid = (high + low)//2
    if target > int_list[mid] and low != high:
        mid = (high + low + 1)//2
        low = mid
        return bin_search(target,low,high,int_list)
    elif target < int_list[mid] and low != high:
        high = mid
        return bin_search(target,low,high,int_list)
    elif target == int_list[mid]:
        return mid
    else:
        return None