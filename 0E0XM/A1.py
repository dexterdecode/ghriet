"""
Created on Wed Apr 10 13:31:11 2019
@author: sunny

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 9, 2, 15, 10, 16, 11, 16])
y = np.array([95, 80, 10, 50, 45, 98, 38, 93])

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(x,y)
mn=np.min(x)
mx=np.max(x)
x1=np.linspace(mn,mx,500)
y1=slope*x1+intercept
plt.plot(x,y,'ob')
plt.plot(x1,y1,'-r')
plt.show()

x = x[:, None]
    
    
from sklearn.linear_model import LinearRegression

predictor = LinearRegression()
predictor.fit(x, y)
x_test = np.array([2])
x_test = x_test[:,None]
outcome = predictor.predict(x_test)
coefficients = predictor.coef_

print('Outcome : {}'.format(outcome))

#casual approach
from statistics import mean
import numpy as np

xs = np.array([10, 9, 2, 15, 10, 16, 11, 16], dtype=np.float64)
ys = np.array([95, 80, 10, 50, 45, 98, 38, 93], dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))
    return m

m = best_fit_slope(xs,ys)
print("Here's the need best_fit_slope",m)