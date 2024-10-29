import math

def calculate_entropy(veroyatn):
    return -sum(p * math.log2(p) for p in veroyatn if p > 0)

def shannon_fano(veroyatn):
    symbols = list(range(len(veroyatn)))
    sorted_symbols = sorted(zip(veroyatn, symbols), reverse=True)
    codes = [""] * len(veroyatn)

    def assign_codes(veroyatn, prefix=""):
        if len(veroyatn) == 1:
            codes[veroyatn[0][1]] = prefix
            return
        total = sum(p[0] for p in veroyatn)
        summa = 0
        for i, (p, _) in enumerate(veroyatn):
            summa += p
            if summa >= total / 2:
                assign_codes(veroyatn[:i + 1], prefix + "0")
                assign_codes(veroyatn[i + 1:], prefix + "1")
                break

    assign_codes(sorted_symbols)
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

if __name__ == "__main__":
    main()
