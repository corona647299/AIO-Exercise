import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x >= 0 else alpha * (math.exp(x) - 1)

def evaluate_activation(x, activation_function):
    # check x
    if is_number(x) == False:
        print('x must be a number')
        return

    # check tên hàm
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_function} is not supported')
        return

    x = float(x)

    # Tính toán giá trị hàm kích hoạt
    if activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'elu':
        result = elu(x)


    print(f'{activation_function}: f({x}) = {result}')

if __name__ == "__main__":
    evaluate_activation(3, 'relu')
    evaluate_activation(3, 'sigmoid')
    evaluate_activation(-2, 'elu')
    evaluate_activation('abc', 'relu')
    evaluate_activation(5, 'belu')