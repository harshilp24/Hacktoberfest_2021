limit1 = 236491
limit2 = 713787

def get_digits(number) :
    return [int(i) for i in str(number)]

def non_decreasing(number) :
    digits = get_digits(number)
    return len([digits[i] for i in range(len(digits)- 1) if digits[i + 1] >= digits[i] ]) == 5

def is_consecutive(number) :
    digits = get_digits(number)
    return len([i for i in range(len(digits) - 1) if digits[i + 1] == digits[i] ]) >= 1


def find_pair(number) :
    digits = get_digits(number)
    frequency = [(digits.count(i), i) for i in set(digits) if digits.count(i) >= 2 ]
    frequency.sort()
    return frequency[0][1]

def remove_pair(number) :
    digits = get_digits(number)
    pair = (find_pair(number))
    digits.remove(pair)
    digits.remove(pair)
    return digits

def is_matching_digits(number) :
    return len([i for i in remove_pair(number) if i == find_pair(number)]) == 0

passwords2 = [i for i in range(limit1 , limit2 + 1) if (is_consecutive(i)) and (non_decreasing(i)) and (is_matching_digits(i))]
print(passwords2)
print(len(passwords2))

