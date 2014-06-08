# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 16:39:18 2014

@author: Jerry
"""

import data_processor as dp
from feature_selection import Features
from naive_bayes import NaiveBayes

def train_and_test():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    test_data = dp.read_data('dataset/test40.txt', 'dataset/ytest40.txt')
    feature = Features()
    training_set = feature.simple(training_data)
    test_set = feature.simple(test_data)
    
    naive_bayes = NaiveBayes(training_set, 4, False, False)
    
    error_count = 0
    for index in range(len(test_set)):
        feature_vector, correct_class = test_set[index]
        prediction = naive_bayes.predict(feature_vector, True)
        if  prediction != correct_class:
            error_count += 1
        print prediction, correct_class
    error_rate = float(error_count)/len(test_set)
    print 'error rate:', error_rate
    
if __name__ == '__main__':
    train_and_test()