# Adapted for python2 and python3
from __future__ import division, print_function, absolute_import

import os
import math
import numpy

from flask import Flask, jsonify, request


# Create web application
APP = Flask(__name__)
PORT = int(os.environ.get('PORT', 8000))

# Model path
MODEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.npy')


@APP.route('/', methods=['GET'])
def index():
    return jsonify({'server': 'Server start in 8000 port.'})


@APP.route('/test', methods=['GET'])
def test_url():
    nn = Model()
    return jsonify({
        'w1': {
            'w1': nn.weights['w1'].tolist(),
            'b1': nn.weights['b2'].tolist()
        },
        'w2': {
            'w2': nn.weights['w2'].tolist(),
            'b1': nn.weights['b2'].tolist()
        },
        'w3': {
            'w3': nn.weights['w3'].tolist(),
            'b3': nn.weights['b3'].tolist()
        }
    })


@APP.route('/analyze', methods=['POST'])
def analyzer_url():
    try:
        # Create nn model
        nn = Model()
        # Get time series from request and prepare it
        series = request.json['series']

        # Check series for instance
        if not isinstance(series, list):
            return jsonify({'error': 'Series must be list.'})

        # Analyze series
        result = list()
        for index, part in enumerate(split_array(series)):
            # Only for an array of 100 long
            if len(part) < 100:
                continue

            # Format response
            series_array = [item['value'] for item in part]
            prods = nn.analyze(numpy.array([prepare_series(series_array)]))
            result.append({
                'start': part[0]['timestamp'],
                'end': part[-1]['timestamp'],
                'anomaly': bool(prods)
            })
        return jsonify({'result': result})
    except KeyError:
        return jsonify({'error': 'Key error. Not found.'})


# Split array to chunks
def split_array(array, length=100):
    for index in range(0, len(array), length):
        yield array[index:index+length]


# Prepare series for nn
def prepare_series(series):
    burst_factor = get_burst_factor(series)
    return exp_smoothing([value / burst_factor for value in series])


# Exponential smoothing for graphics
def exp_smoothing(series, alpha=0.4):
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1 - alpha) * result[index-1])
    return result


# Calculation of strong emissions in the graph
def get_burst_factor(series):
    result = 0
    for index in range(len(series)-1):
        result += math.fabs(series[index+1] - series[index])
    return result


# Softmax function activation
def activate_softmax(x):
    return numpy.exp(x) / numpy.sum(numpy.exp(x), axis=1, keepdims=True)


# ReLu function activation
def activate_relu(x):
    return numpy.maximum(x, 0)


# nn model class
class Model(object):
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


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=PORT, debug=False)
