# 1)                             kode wars!
def is_palindrome(s):
    lower_rversed_s = s.lower()[::-1]
    lower_s = s.lower()
    
    if lower_s == lower_rversed_s:
        return True
    else:
        return False
    

# 2)
def positive_sum(arr):
    sum = 0
    
    for i in arr:
        if i > 0:
            sum += i
    return sum


# 3)
def remove_every_other(my_list):
    return my_list[::2]