import math

def calculate_entropy(veroyatn):
    return -sum(p * math.log2(p) for p in veroyatn if p > 0)

def shannon_fano(veroyatn):
    # Сортируем вероятности от большего к меньшему
    sorted_symbols = sorted(enumerate(veroyatn), key=lambda x: x[1], reverse=True)
    codes = [""] * len(veroyatn)

    # Присваиваем коды
    for i, (index, _) in enumerate(sorted_symbols):
        # Код для первого символа будет "1", для второго "01", для третьего "001" и так далее
        codes[index] = '0' * i + '1'

    return codes

def main():
    N = 8
    veriyatn = []
    
    for i in range(N):
        while True:
            try:
                p = float(input("Введите вероятность символа {} (0 < p <= 1): ".format(i + 1)))
                if 0 < p <= 1:
                    veriyatn.append(p)
                    break
                else:
                    print("Ошибка: вероятность должна быть в диапазоне (0, 1]. Попробуйте снова.")
            except ValueError:
                print("Ошибка: введите корректное число.")

    H_A = calculate_entropy(veriyatn)
    H_max_A = math.log2(N)
    codes = shannon_fano(veriyatn)
    l = sum(len(code) * p for code, p in zip(codes, veriyatn))
    R_A = l - H_A
    C_eff = sum(p * len(code) for p, code in zip(veriyatn, codes))

    print("Энтропия H(A): {:.3f} бит".format(H_A))
    print("Максимальная энтропия Hmax(A): {:.3f} бит".format(H_max_A))
    print("Средняя длина кода l: {:.3f} бит".format(l))
    print("Избыточность R(A): {:.3f} бит".format(R_A))
    print("Эффективная пропускная способность C_eff: {:.3f} бит".format(C_eff))
    
    # Вывод кодов Шеннона-Фано
    print("\nКоды Шеннона-Фано для символов:")
    for i, code in enumerate(codes):
        print("Символ {}: Код {}".format(i + 1, code))

if __name__ == "__main__":
    main()
