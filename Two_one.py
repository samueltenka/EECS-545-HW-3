import random

def get_y(x):
    epsilon = random.gauss(0.0, 0.04)
    w0 = random.gauss(0.0, 1.0)
    w1 = random.gauss(0.0, 1.0)
    return epsilon + w0 + w1*x

print('Bayesian way...')
es, vs = [], []
xs = [(i-100)/100.0 for i in range(201)]
for x in xs:
    ys = [get_y(x) for i in range(10000)]
    expected = sum(ys)/len(ys)
    variance = sum((y-expected)**2 for y in ys)/len(ys)
    es.append(expected); vs.append(variance)

print('Gaussian way...')
esums = [0.0 for x in xs]
vsums = [0.0 for x in xs]
for i in range(10000):
    epsilon = random.gauss(0.0, 0.04)
    w0 = random.gauss(0.0, 1.0)
    w1 = random.gauss(0.0, 1.0)
    for i in range(201):
        y = epsilon+w0+w1*xs[i]
        esums[i] += y
        vsums[i] += y*y
esums = [e/10000 for e in esums]
vsums = [v/10000-e*e for v,e in zip(vsums, esums)]

for v, vsum in zip(vs, vsums):
    print(v-1.04, vsum-1.04)
