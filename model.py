import numpy as np 
from sklearn.svm import SVC
import joblib
import time
import matplotlib.pyplot as plt

# Function: read_data
# Inputs:
#   filename: string of the file name to be parsed
# Outputs:
#   data: 2D matrix of the corresponding data for each
#       pixel value
#   labels: vector of corresponding labels for each example
# Description:
#   Takes the filename and parses it to create a data and 
#   label vector for the model. The data matrix is also 
#   normalized from [0, 1]
def read_data(filename):
    # read in test data
    test_data = open(filename, 'r')
    data = []
    labels = []
    line = test_data.readline() # read first line, only contains titles
    line = test_data.readline()
    while line:
        line = line.replace(",", " ").split()
        row = list(map(float, line))
        labels.append(row.pop(0))
        data.append(row)
        line = test_data.readline()
    data = np.asmatrix(data)
    data *= (1/data.max())  # normalize [0, 1]
    return data, labels

# get matrices
print("reading training data")
data_train, labels_train = read_data('./data/mnist_train.csv')
print("reading testing data")
data_test, labels_test = read_data('./data/mnist_test.csv')

# tuned parameters
k = 'rbf'
C = 10

# train SVM and save to file
filename = './data/rbf_model.joblib.pkl'
clf = SVC(kernel=k, C=C).fit(data_train, labels_train)
_ = joblib.dump(clf, filename, compress=9)





