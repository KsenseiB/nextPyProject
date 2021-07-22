def get_sum(num):
    return sum(int(digit) for digit in str(num))


def check_id_valid(id_number):
    id_string = str(id_number)
    id_map = map(int, id_string)
    id_num_list = list(id_map)
    # print(id_num_list)
    # phase 1
    new_num = [num * 2 if num % 2 == 0 else num for num in id_num_list]
    print(new_num)
    # phase 2
    num_greater_then_nine = [get_sum(num) if num > 9 else num for num in new_num]
    print(num_greater_then_nine)
    # phase 3
    id_numbers_sum = sum(num_greater_then_nine)
    # phase 4
    if id_numbers_sum % 10 == 0:
        print("True")
        return True
    else:
        print("False")
        return False
    # True if (id_numbers_sum % 10 == 0) else False


check_id_valid(123456789)


if __name__ == '__main__':
    print("yo")

