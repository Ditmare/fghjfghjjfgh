import math

def calculate_entropy(veroyatn):
    return -sum(p * math.log2(p) for p in veroyatn)

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
    veriyatn = [float(input(f"Введите вероятность символа {i + 1} (0 < p <= 1): ")) for i in range(N)]

    H_A = calculate_entropy(veriyatn)
    H_max_A = math.log2(N)
    codes = shannon_fano(veriyatn)
    l = sum(len(code) * p for code, p in zip(codes, veriyatn))
    R_A = l - H_A
    C_eff = sum(p * len(code) for p, code in zip(veriyatn, codes))

    print(f"Энтропия H(A): {H_A:.3f} бит")
    print(f"Максимальная энтропия Hmax(A): {H_max_A:.3f} бит")
    print(f"Средняя длина кода l: {l:.3f} бит")
    print(f"Избыточность R(A): {R_A:.3f} бит")
    print(f"Эффективная пропускная способность C_eff: {C_eff:.3f} бит")

if __name__ == "__main__":
    main()
