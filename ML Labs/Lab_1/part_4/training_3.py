import numpy
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import (
    brier_score_loss, precision_score, recall_score, f1_score)
import scikitplot as skplt
from sklearn import svm
import matplotlib.pyplot as plt

from common.plot_builder import *
from common.file_processor_svmdata import *

# SETUP
features_train, labels_train = return_features_labels(
    "./Lab_1/lab1_data/svmdata_c.txt")
features_test, labels_test = return_features_labels(
    "./Lab_1/lab1_data/svmdata_c_test.txt")

plot_builder = PlotBuilder()

for kern in ('linear', 'poly', 'rbf', 'sigmoid'):

    degree_start = 3
    degree_end = 4
    if (kern == 'poly'):
        degree_start = 1
        degree_end = 6

    for degree in range(degree_start, degree_end):
        # TRAIN
        lsvc = svm.SVC(kernel=kern, degree=degree)
        lsvc.fit(features_train, labels_train)

        # TEST
        labels_pred = lsvc.predict(features_test)
        
        # ANALYSE RESULTS
        print("Accuracy on Train with kernel = ", kern, " and score = ", lsvc.score(features_train, labels_train))
        print("Accuracy on Test with kernel = ", kern, " and score = ", lsvc.score(features_test, labels_test))
        fig, sub = plt.subplots(1, 2)
        ax = sub.flatten()
        plot_builder.plot_svm(ax[0], lsvc, features_test, labels_test)
        title = ['Kernel = ', kern, ' degree = ', degree]
        skplt.metrics.plot_confusion_matrix(
        labels_test, labels_pred, normalize=True, ax=ax[1], title=title)

plt.show()




