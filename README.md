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
</body>
</html>
