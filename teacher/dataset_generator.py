import math
import random
import numpy as np
# import matplotlib.pyplot as plt


def exp_smoothing(series, alpha=0.1):
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1-alpha) * result[index-1])
    return result


def get_factor(series):
    result = 0
    for index in range(98):
        result += math.fabs(series[index+1] - series[index])
    return result


def gen():
    label = 0
    data = list((random.uniform(250, 300) for _ in range(100)))

    left = random.randint(0, 20)
    right = random.randint(20, 40)
    factor = random.randint(0, 100)

    if factor < 50:
        label = 1
        data[left:right] = [
            value//random.random() if factor > 50 else value*random.random()
            for value in data[left:right]
        ]
    return data, label


if __name__ == '__main__':
    dataset = list()
    labels = list()
    for data, label in (gen() for _ in range(50000)):
        factor = get_factor(data)
        dataset.append(exp_smoothing([value/factor for value in data]))
        labels.append(label)

    np.save('dataset', np.array(dataset))
    np.save('labels', np.array(labels))
