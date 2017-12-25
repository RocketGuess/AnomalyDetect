from __future__ import division, print_function, absolute_import

import math
import collections
import numpy as np
import matplotlib.pyplot as plt


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)


def relu(x):
    return np.maximum(x, 0)


class Model(object):
    def __init__(self):
        # Weights container
        self.weights = collections.defaultdict(np.array)

        # Layers sizes
        self.x = 100
        self.h1 = 55
        self.h2 = 1024
        self.y = 2

    def initialize(self):
        # Bias initialization
        self.weights['b1'] = np.zeros(self.h1)
        self.weights['b2'] = np.zeros(self.h2)
        self.weights['b3'] = np.zeros(self.y)

        # Weights initialization
        matrix_W1 = np.random.randn(self.x, self.h1)
        matrix_W2 = np.random.randn(self.h1, self.h2)
        matrix_W3 = np.random.randn(self.h2, self.y)

        self.weights['w1'] = math.sqrt(2 / self.x) * matrix_W1
        self.weights['w2'] = math.sqrt(2 / self.h1) * matrix_W2
        self.weights['w3'] = math.sqrt(2 / self.h2) * matrix_W3

    def forward_pass(self, x):
        layer1 = x.dot(self.weights['w1']) + self.weights['b1']
        layer1 = relu(layer1)
        layer2 = layer1.dot(self.weights['w2']) + self.weights['b2']
        layer2 = relu(layer2)
        layer3 = layer2.dot(self.weights['w3']) + self.weights['b3']
        return layer1, layer2, layer3

    def softmax_cross_entropy(self, x, y, prods, reg):
        w1_r = math.sqrt(reg * np.sum(self.weights['w1']*self.weights['w1']))
        w2_r = math.sqrt(reg * np.sum(self.weights['w2']*self.weights['w2']))
        w3_r = math.sqrt(reg * np.sum(self.weights['w3']*self.weights['w3']))

        loss_sum = math.fabs(np.sum(np.log(prods[range(len(y)), y])))
        return loss_sum / (len(x) + w1_r + w2_r + w3_r)

    def calc_gradient(self, x, y, reg):
        layer1, layer2, layer3 = self.forward_pass(x)
        prods = softmax(layer3)

        loss = self.softmax_cross_entropy(x, y, prods, reg)

        # Gradient container
        grad = collections.defaultdict(np.array)

        prods[range(len(x)), y] -= 1
        grad['w3'] = (layer2.T.dot(prods) / len(x)) + reg * self.weights['w3']
        grad['b3'] = np.sum(prods, axis=0, keepdims=True) / len(x)

        excess = prods.dot(self.weights['w3'].T) * relu(layer2)
        grad['w2'] = (layer1.T.dot(excess) / len(x)) + reg * self.weights['w2']
        grad['b2'] = np.sum(excess, axis=0, keepdims=True) / len(x)

        excess = layer2.dot(self.weights['w2'].T) * relu(layer1)
        grad['w1'] = (x.T.dot(excess) / len(x)) + reg * self.weights['w1']
        grad['b1'] = np.sum(excess, axis=0, keepdims=True) / len(x)
        return grad, loss

    def train(self, x, y, tr_x, tr_y, rate, decay, reg, epochs, batch_size):
        # History container
        history = collections.defaultdict(list)

        # Train cycle
        for epoch in range(epochs):
            indexes = np.random.choice(len(x), batch_size)
            data_batch = x[indexes]
            labels_batch = y[indexes]

            gradient, loss = self.calc_gradient(data_batch, labels_batch, reg)
            history['loss'].append(loss)

            # Update weight
            self.weights['w1'] -= rate * gradient['w1']
            self.weights['b1'] -= rate * gradient['b1'][0]

            self.weights['w2'] -= rate * gradient['w2']
            self.weights['b2'] -= rate * gradient['b2'][0]

            self.weights['w3'] -= rate * gradient['w3']
            self.weights['b3'] -= rate * gradient['b3'][0]

            accuracy_train = np.mean(self.predict(x) == y)
            accuracy_test = np.mean(self.predict(tr_x) == tr_y)
            history['acc_train'].append(accuracy_train)
            history['acc_test'].append(accuracy_test)

            print('Epoch:[{}/{}] Loss:[{}] Accuracy:[{}] Test:[{}]'.format(
                epoch, epochs, loss, round(accuracy_train, 2),
                round(accuracy_test, 2)))

            # Every epoch, check accuracy and dacay rate
            if epoch % max(len(x) / batch_size, 1) == 0:
                # Decay rate train
                rate *= decay
        return history

    def predict(self, x):
        prods = softmax(self.forward_pass(x)[2])
        return np.argmax(prods, axis=1)


if __name__ == '__main__':
    dataset = np.load('dataset.npy')
    labels = np.load('labels.npy')

    # Create model
    nn = Model()
    nn.initialize()

    # Train model
    stats = nn.train(
        x=dataset[:25000],
        y=labels[:25000],
        tr_x=dataset[25000:],
        tr_y=labels[25000:],
        rate=0.001,
        decay=0.95,
        reg=0.01,
        epochs=1500,
        batch_size=24
    )

    figure = plt.figure(figsize=(10, 10))
    loss_chart = figure.add_subplot(211)
    loss_chart.plot(stats['loss'])
    loss_chart.set_title('Loss hostory')
    loss_chart.set_xlabel('epoch')
    loss_chart.set_ylabel('loss')

    accuracy_chart = figure.add_subplot(212)
    accuracy_chart.plot(stats['acc_train'], label='train')
    accuracy_chart.plot(stats['acc_test'], label='test')
    accuracy_chart.set_title('Accuracay')
    accuracy_chart.set_xlabel('epoch')
    accuracy_chart.set_ylabel('avg')
    accuracy_chart.legend()
    plt.show()

    np.save('model', nn.weights)
