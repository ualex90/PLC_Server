def get_bit(num: int, n: int) -> bool:
    # Функция возвращает значение бита n двухбайтного числа num (0...65535)
    num_bin = bin(65536 + num)[3:]
    word = list(map(int, num_bin))
    word.reverse()
    return word[n] == True

if __name__ == "__main__":
    print(get_bit(6, 0))