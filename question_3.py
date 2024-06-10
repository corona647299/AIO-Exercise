import random
import math

def calculate_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)

    samples = [f'sample-{i}' for i in range(num_samples)]
    predicts = [random.uniform(0, 10) for i in range(num_samples)]
    targets = [random.uniform(0, 10) for i in range(num_samples)]

    if loss_name == 'MAE':
        loss = sum(abs(targets[i] - predicts[i]) for i in range(num_samples)) / num_samples
    elif loss_name == 'MSE':
        loss = sum((targets[i] - predicts[i]) ** 2 for i in range(num_samples)) / num_samples
    elif loss_name == 'RMSE':
        mse = sum((targets[i] - predicts[i]) ** 2 for i in range(num_samples)) / num_samples
        loss = math.sqrt(mse)
    else:
        print('Unsupported loss function')
        return

    # Print the results
    print(f'Loss name: {loss_name}')
    for i in range(num_samples):
        print(f'Sample{[i]}: Predict: {predicts[i]:.2f}, Target: {targets[i]:.2f}')
    print(f'Loss: {loss:.2f}')

if __name__ == "__main__":   
    num_samples = input('Enter number of samples: ')
    loss_name = input('Enter loss function (MAE, MSE, RMSE): ')
    calculate_loss(num_samples, loss_name)