# <a id="Recognition_of_sharp_outbursts_on_the_graph_0"></a>Recognition of sharp outbursts on the graph

Before recognition, the series undergoes preprocessing in the form of a Holt-Winters smoothing, and dividing each co- ordinate by a burst factor. Since the data are discrete, a formula for detecting strong oscillations on a graph, such as:

<div align="center">
  <img src="https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/burst_factor.png"><br><br>
</div>

The time series is represented as a function of x (t), where t is the time of the coordinate, and in this case the index in the array, the time series is represented by the formula:

<div align="center">
  <img src="https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/time_function.png"><br><br>
</div>

Neural network: a fully connected perceptron with three layers and architecture:
* x -> w1 -> relus -> w2 -> relu -> w3 -> softmax

1. Input size: 100
2. First hidden size: 55
3. Seconds hidden size: 1024
4. Output size: 2 (anomaly or not anomaly)

Loss function: [cross entropy for softmax](http://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html?highlight=cross#cross-entropy)

Loss function optimization: stochastic gradient descent of Adam
Network training: [Method of back propagation error](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%BE%D0%B3%D0%BE_%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8)

## <a id="Quick_start_0"></a>Quick start

    ./start.sh

## <a id="Dependencies_4"></a>Dependencies

##### <a id="For_server_5"></a>For server:

*   [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
*   [numpy](http://www.numpy.org/)

    Install: pip3 install aiohttp numpy

##### <a id="For_network_train_11"></a>For network train:

*   [numpy](http://www.numpy.org/)
*   [matplotlib](https://matplotlib.org/)

    Install: pip3 install numpy matplotlib

## <a id="Server_api_17"></a>Server api

* * *

##### <a id="GET__19"></a>GET /

Server test.  
RESPONSE:

    {
        "server": "Server start in 8080 port."
    }

* * *

##### <a id="GET_test_28"></a>GET /test

Get network weights, model load test.  
RESPONSE:

    {
        'w1': {
            'w1: [],
            'b1: []
        },
        'w2': {
            'w2: [],
            'b2: []
        },
        'w3': {
            'w3: [],
            'b3: []
        }
    }

* * *

##### <a id="POST_analyze_48"></a>POST /analyze

To analyze a segment or segments on the anomaly.  
REQYEST BODY:

    {
        "series": [
            {
                "value": 1,
                "timestamp": 1514238804
            },
            {
                "value": 1,
                "timestamp": 1514238804
            }
        ]
    }

RESPONSE:

    {
        "results": [
            {
                "anomaly": true,
                "start": 1514238804,
                "end": 1514238804
            },
            {
                "anomaly": false,
                "start": 1514238804,
                "end": 1514238804
            }
        ]
    }

* * *
