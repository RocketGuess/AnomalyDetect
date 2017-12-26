import os
import numpy

# Model path
MODEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.npy')


# Softmax function activation
def activate_softmax(x):
    return numpy.exp(x) / numpy.sum(numpy.exp(x), axis=1, keepdims=True)


# ReLu function activation
def activate_relu(x):
    return numpy.maximum(x, 0)


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class Network(object, metaclass=Singleton):
    def __init__(self, model_path=MODEL):
        self.weights = numpy.load(model_path)[()]

    def _forward_pass(self, x):
        layer1 = numpy.dot(x, self.weights['w1']) + self.weights['b1']
        layer1 = activate_relu(layer1)
        layer2 = numpy.dot(layer1, self.weights['w2']) + self.weights['b2']
        layer2 = activate_relu(layer2)
        layer3 = numpy.dot(layer2, self.weights['w3']) + self.weights['b3']
        return layer3

    def analyze(self, x):
        return numpy.argmax(activate_softmax(self._forward_pass(x)))
