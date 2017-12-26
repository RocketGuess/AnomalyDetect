<!DOCTYPE html>
<html>
<body id="preview">
    <h1><a id="Recognition_of_sharp_outbursts_on_the_graph_0"></a>Recognition of sharp outbursts on the graph</h1>
    <p>Before recognition, the series undergoes preprocessing in the form of a Holt-Winters smoothing, and dividing each co- ordinate by a burst factor. Since the data are discrete, a formula for detecting strong oscillations on a graph, such as: </p>
    <p align="center">
        <img src="https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/burst_factor.png">
    </p>
    <p>The time series is represented as a function of x (t), where t is the time of the coordinate, and in this case the index in the array, the time series is represented by the formula:</p>
    <p align="center">
        <img src="https://github.com/fenics1/AnomalyDetect/blob/master/git_statics/time_function.png">
    </p>
    <h2><a id="Quick_start_0"></a>Quick start</h2>
    <pre><code class="language-bash">./start.sh
</code></pre>
    <h2><a id="Dependencies_4"></a>Dependencies</h2>
    <h5><a id="For_server_5"></a>For server:</h5>
    <ul>
        <li><a href="http://flask.pocoo.org/">flask</a></li>
        <li><a href="http://www.numpy.org/">numpy</a></li>
    </ul>
    <pre><code class="language-bash">Install: pip3 install flask numpy
</code></pre>
    <h5><a id="For_network_train_11"></a>For network train:</h5>
    <ul>
        <li><a href="http://www.numpy.org/">numpy</a></li>
        <li><a href="https://matplotlib.org/">matplotlib</a></li>
    </ul>
    <pre><code class="language-bash">Install: pip3 install numpy matplotlib
</code></pre>
    <h2><a id="Server_api_17"></a>Server api</h2>
    <hr>
    <h5><a id="GET__19"></a>GET /</h5>
    <p>Server test.
        <br> RESPONSE:
    </p>
    <pre><code class="language-json">{
    "<span class="hljs-attribute">server</span>": <span class="hljs-value"><span class="hljs-string">"Server start in 8000 port."</span>
</span>}
</code></pre>
    <hr>
    <h5><a id="GET_test_28"></a>GET /test</h5>
    <p>Get network weights, model load test.
        <br> RESPONSE:
    </p>
    <pre><code class="language-json">{
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
</code></pre>
    <hr>
    <h5><a id="POST_analyze_48"></a>POST /analyze</h5>
    <p>To analyze a segment or segments on the anomaly.
        <br> REQYEST BODY:</p>
    <pre><code class="language-json">{
    "<span class="hljs-attribute">series</span>": <span class="hljs-value">[
        {
            "<span class="hljs-attribute">value</span>": <span class="hljs-value"><span class="hljs-number">1</span></span>,
            "<span class="hljs-attribute">timestamp</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span>
        </span>},
        {
            "<span class="hljs-attribute">value</span>": <span class="hljs-value"><span class="hljs-number">1</span></span>,
            "<span class="hljs-attribute">timestamp</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span>
        </span>}
    ]
</span>}
</code></pre>
    <p>RESPONSE:</p>
    <pre><code class="language-json">{
    "<span class="hljs-attribute">results</span>": <span class="hljs-value">[
        {
            "<span class="hljs-attribute">anomaly</span>": <span class="hljs-value"><span class="hljs-literal">true</span></span>,
            "<span class="hljs-attribute">start</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span></span>,
            "<span class="hljs-attribute">end</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span>
        </span>},
        {
            "<span class="hljs-attribute">anomaly</span>": <span class="hljs-value"><span class="hljs-literal">false</span></span>,
            "<span class="hljs-attribute">start</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span></span>,
            "<span class="hljs-attribute">end</span>": <span class="hljs-value"><span class="hljs-number">1514238804</span>
        </span>}
    ]
</span>}
</code></pre>
    <hr>

</body>

</html>
