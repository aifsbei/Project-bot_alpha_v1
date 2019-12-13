def partial_sum(*args):
    summ = 0
    sum_list = []
    for value in args:
       sum_list.append(summ)
       summ += value
    sum_list.append(summ)
    return sum_list


print(partial_sum(1, 0.5, 0.25, 0.125))