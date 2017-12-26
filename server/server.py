#!/usr/bin/env python3
import math
import network
import numpy
import aiohttp
import aiohttp.web


# Split array to chunks
def split_array(array, length=100):
    array = array[0:(100 * len(array) // 100)]
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


# Server default url
async def index(request):
    return aiohttp.web.json_response({
        'server': 'Server start in 8080 port.'
    })


# Test load weights
async def test_load_weights(request):
    nn = network.Network()
    return aiohttp.web.json_response({
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


# Analyze time series
async def analyze(request):
    try:
        # Create nn model
        nn = network.Network()

        # Get time series from request
        data = await request.json()
        series = data['series']

        # Check series for instance
        if not isinstance(series, list):
            return aiohttp.web.json_response({'error': 'Not list'}, status=400)

        # Analyze series
        result = list()
        for index, part in enumerate(split_array(series)):
            series_array = [item['value'] for item in part]
            prods = nn.analyze(numpy.array([prepare_series(series_array)]))
            result.append({
                'start': part[0]['timestamp'],
                'end': part[-1]['timestamp'],
                'anomaly': bool(prods)
            })
        return aiohttp.web.json_response({'result': result}, status=200)
    except KeyError:
        return aiohttp.web.json_response({'error': 'Key error'}, status=400)


# Start application
def init():
    app = aiohttp.web.Application()
    app.router.add_route(method='GET', handler=index, path='/')
    app.router.add_route(method='GET', handler=test_load_weights, path='/test')
    app.router.add_route(method='POST', handler=analyze, path='/analyze')
    return app


if __name__ == '__main__':
    aiohttp.web.run_app(init())
