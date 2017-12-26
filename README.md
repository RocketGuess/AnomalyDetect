# <a id="Recognition_of_sharp_outbursts_on_the_graph_0"></a>Recognition of sharp outbursts on the graph

Before recognition, the series undergoes preprocessing in the form of a Holt-Winters smoothing, and dividing each co- ordinate by a burst factor. Since the data are discrete, a formula for detecting strong oscillations on a graph, such as:

![](https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/burst_factor.png)

The time series is represented as a function of x (t), where t is the time of the coordinate, and in this case the index in the array, the time series is represented by the formula:

![](https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/time_function.png)

## <a id="Quick_start_0"></a>Quick start

    ./start.sh

## <a id="Dependencies_4"></a>Dependencies

##### <a id="For_server_5"></a>For server:

*   [flask](http://flask.pocoo.org/)
*   [numpy](http://www.numpy.org/)

    Install: pip3 install flask numpy

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
        "server": "Server start in 8000 port."
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
