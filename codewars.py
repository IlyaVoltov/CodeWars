def odd_or_even(arr):
    for i in arr:
        if sum(arr) % 2 == 0:
            return "even"
        else:
            return "odd"

odd_or_even([0, 1, 4])
