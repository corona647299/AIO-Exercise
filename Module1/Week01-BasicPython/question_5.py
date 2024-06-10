def md_nre(y, y_hat, n, p):

    # Tính căn bậc n
    y_n = y ** (1/n)
    y_hat_n = y_hat ** (1/n)

    # Tính toán hàm loss với bậc p
    loss = abs(y_n - y_hat_n) ** p

    return loss

if __name__ == "__main__":
    examples = [
        (100, 99.5, 2, 1),
        (50, 49.5, 2, 1),
        (20, 19.5, 2, 1),
        (5.5, 5.0, 2, 1),
        (1.0, 0.5, 2, 1),
        (0.6, 0.1, 2, 1)
    ]

    for y, y_hat, n, p in examples:
        result = md_nre(y, y_hat, n, p)
        print(f"MD_nRE(y={y}, y_hat={y_hat}, n={n}, p={p}) = {result:}")