import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('./deeplearning.mplstyle')  # Not works
plt.style.use('ggplot')

# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
# print(f"x_train = {x_train}")
# print(f"y_train = {y_train}")

# m is the number of training examples
print(f"x_train.shape: {x_train.shape}")
# m = x_train.shape[0]
'''This shows that there is only two rows in 
the dataSet table and the m = 2 where m is 
number of training examples'''
# print(f"Number of training examples is: {m}")

# m is the number of training examples
# m = len(x_train)
# print(f"Number of training examples is: {m}")

i = 0 # Change this to 1 to see (x^1, y^1)
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# Plot the data points
plt.scatter(x_train, y_train, marker='.', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()

w = 200
b = 100
# print(f"w: {w}")
# print(f"b: {b}")


def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples
      w,b (scalar)    : model parameters
    Returns
      y (ndarray (m,)): target values
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
'''
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction') is a line of
code in the Python programming language that uses the plot function from the
matplotlib library to generate a graph of the data.

The plot function takes in two arguments, x_train and tmp_f_wb, which represent
the data that will be plotted on the x-axis and y-axis, respectively. The c argument
specifies the color of the line that will be plotted, and the label argument specifies 
a label that will be used to identify the plotted data in the legend of the graph.

This line of code will generate a graph with a single line plotted on it, using the 
data in x_train and tmp_f_wb as the x- and y-coordinates, respectively. The line will 
be plotted in blue and will be labeled "Our Prediction" in the legend of the graph.
'''
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
'''
The Scatter function only marks that points where the points exists and not 
drow the whole line like Plot() function.
'''
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
'''
The legend function is used to display a legend in the graph, 
which provides a key for interpreting the data that is plotted 
on the graph. The legend typically includes a label for each 
plotted dataset, along with a symbol or color that corresponds to that dataset.

In this case, plt.legend() will add a legend to the graph,
using the labels that have been specified for the plotted data 
using the label argument in the plot or scatter function. 
The legend will be placed at a default location on the graph, 
which is typically in the upper right corner of the plot area.
'''
plt.legend()
plt.show()

w = 200
b = 100

''' 
x_i is the input variable (size in 1000 square feet)
'''
x_i = 1.2
cost_of_1200_sqft = w * x_i + b
print(f"${cost_of_1200_sqft:.0f} thousand dollars")