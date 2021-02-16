def count_uniq_sub_str(str_):
    res = set()

    for len_sub_str in range(1, len(str_)):
        start = 0
        end = len_sub_str
        while True:
            if end > len(str_):
                break
            res.add(hash(str_[start:end]))
            start += 1
            end += 1

    return len(res)


str_ = input("Введите строку без пробелов: ")
print(count_uniq_sub_str(str_))
