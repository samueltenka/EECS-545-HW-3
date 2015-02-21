import random
import math

from numpy import array, identity, dot, transpose, multiply
from numpy.linalg import inv
from numpy.random import multivariate_normal

alpha = 1.0 ## prior variances of weights
beta = 1.0/0.04 ## precision (i.e. 1/variance from noise)

'''
t_ = array([-.8, -.7, -.1]) ## data
x_ = array([[1, -.5],
            [1, 0],
            [1, .5]])
'''

t_ = array([(i-450)/1000.0 for i in range(900)])
x_ = array([[1, (i-450)/1000.0] for i in range(900)])
for x,t in zip(x_, t_):
    pass

wcov = alpha*identity(2) + beta*dot(transpose(x_), x_)
wmean = dot(inv(wcov), beta*dot(transpose(x_), t_))
print(wcov)
print(wmean)

xs = array([[1.0, (i-100)/100.0]
            for i in range(201)])
ycov = array([[dot(dot(transpose(x1), wcov), x2) for x2 in xs] for x1 in xs])
ymean = array([dot(transpose(x), wmean) for x in xs])

esums = array([0.0 for x in xs])
vsums = array([0.0 for x in xs])
for j in range(100):
    if j%100==0:
        print(j)
    ys = multivariate_normal(ymean, ycov)
    esums += ys
    vsums += multiply(ys, ys)
esums = esums/100
vsums = vsums/100 - multiply(esums, esums)
ssums = [v**0.5 for v in vsums]

xss = []; yss = []
for i in range(201):
    xss += [xs[i], xs[i]]
    yss += [esums[i]+2*ssums[i], esums[i]-2*ssums[i]]
import Plot
Plot.sam_plot(xss, yss, 'probable region')
Plot.save_plot('x', 'y', 'probable envelope', 'SD.png')
