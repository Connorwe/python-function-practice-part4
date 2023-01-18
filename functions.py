def max_num(num1, num2, num3):
    return max(num1, num2, num3)  # max function returns max number in list


print(max_num(1, 2, 3))
# Output: 3


def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(mult_list([1, 7, 3, 9, 15]))
# Output: 2835


def rev_string(s):
    return s[::-1]


print(rev_string("Can you read this"))
# Output: "siht daer uoy naC"


def num_within(x, range):
    if range[0] <= x <= range[1]:
        return True
    else:
        return False


print(num_within(8, (5, 10)))
# Output: True


def pascal(n):
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        prev_row = row
        print(" ".join(str(x) for x in row))


pascal(5)
