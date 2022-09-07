# matplotlib import
#from matplotlib import pyplot as plt


# https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4
import numpy as np
import matplotlib.pyplot as plt

# ensure your arr is sorted from lowest to highest values first!

interval = 2500
income_brackets = [num * interval for num in range(0, 42)]
income_count    = [13741,5769,6381,7767,10331,8119,9687,7787,9809,7245,8962,5738,9630,4392,8076,4344,7820,3581,5779,3689,7846,2934,4745,2541,5725,2372,3910,2009,3855,1817,3336,1620,3164,1410,2095,1208,2357,1073,1460,864,30928]

#income_brackets = [5, 10, 20]
#income_count    = [14, 17, 1100]

arr = []
for bracket, count in zip(income_brackets, income_count):
    temp_arr = [bracket] * count
    arr += temp_arr
    
print(income_brackets)
#arr.sort()

arr = np.array(arr)

def gini(arr):
    count = arr.size
    coefficient = 2 / count
    indexes = np.arange(1, count + 1)
    weighted_sum = (indexes * arr).sum()
    total = arr.sum()
    constant = (count + 1) / count
    return coefficient * weighted_sum / total - constant

def lorenz(arr):
    # this divides the prefix sum by the total sum
    # this ensures all the values are between 0 and 1.0
    scaled_prefix_sum = arr.cumsum() / arr.sum()
    # this prepends the 0 value (because 0% of all people have 0% of all wealth)
    return np.insert(scaled_prefix_sum, 0, 0)

# show the gini index!
print(gini(arr))

lorenz_curve = lorenz(arr)

# we need the X values to be between 0.0 to 1.0
plt.plot(np.linspace(0.0, 1.0, lorenz_curve.size), lorenz_curve)
# plot the straight line perfect equality curve
plt.plot([0,1], [0,1])
plt.show()