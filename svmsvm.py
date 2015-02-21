import svmutil
import numpy

print('Reading...')
my_data = numpy.genfromtxt('mnist_49.csv', delimiter=',')
print('Training...')
xs = [list(row[:-1]) for row in my_data]
ys = [row[-1] for row in my_data]
m = svmutil.svm_train(ys, xs, '-t 1 -r 1')
print('Testing...')
p_label, p_acc, p_val = svmutil.svm_predict(ys, xs, m)
print('!')
