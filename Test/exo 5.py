#TODO :
# done

numb_array = [1, 2, 3, 4]

def calc_sum(array):
    total = 0
    for e in array:
        total += e
    return total

# bonus
def calc_sum_rec(array, acc=0):
    return acc if len(array) == 0 else calc_sum_rec(array[1:], acc + array[0])

print(calc_sum(numb_array))
print(calc_sum_rec(numb_array))