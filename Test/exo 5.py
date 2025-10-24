#TODO :
# bonus -> utiliser un type de recursion optimisé pour traiter un grand tableau

numb_array = [1, 2, 3, 4]


def calc_sum(array):
    total = 0
    for e in array:
        total += e
    return total

# bonus pour apres
# calc_sum_rec

print(calc_sum(numb_array))
# print(calc_sum_rec(numb_array))