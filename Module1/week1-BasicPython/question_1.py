def calculate_classification(tp, fp, fn):
    # check datatype
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
    # check value
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

# caculate
    precision = tp / (tp + fp)
    recall = tp / (tp + tp)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print('precision:', precision)
    print('recall:', recall)
    print('f1_score:', f1_score)


if __name__ == "__main__":
    calculate_classification(5, 10, 15)
    calculate_classification(5, 10.5, 8)
    calculate_classification(8, 0, 6)
