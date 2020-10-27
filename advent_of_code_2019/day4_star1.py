limit1 = 236491
limit2 = 713787


def get_digits(number) :
    return [int(i) for i in str(number)]

def non_decreasing(number) :
    digits = get_digits(number)
    return len([digits[i] for i in range(1 , len(digits)) if digits[i] >= digits[i-1] ]) == len(digits) - 1

def is_consecutive(number) :
    digits = get_digits(number)
    return len([i for i in range(1, len(digits)) if digits[i] == digits[i-1] ]) >= 1

passwords1 = [i for i in range(limit1 , limit2 + 1) if (is_consecutive(i)) and (non_decreasing(i))]
print(passwords1)
print(len(passwords1))


