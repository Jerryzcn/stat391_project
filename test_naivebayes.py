# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 16:39:18 2014

@author: Jerry
"""

import numpy as np
import data_processor as dp
from feature_selection import Features
from naive_bayes import NaiveBayes

def train_and_test():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    test_data = dp.read_data('dataset/test40.txt', 'dataset/ytest40.txt')
    feature = Features()
    training_set = feature.simple(training_data)
    test_set = feature.simple(test_data)
    
    
    #dp.remove_ambiguous_entry(training_set)    
    naive_bayes = NaiveBayes(training_set, 4, False)
    
    confusion_matrix = np.zeros([3,3])
    correct = 0.0
    total = 0.0
    for index in range(len(test_set)):
        feature_vector, correct_class = test_set[index]
        prediction = naive_bayes.predict(feature_vector)
        total += 1
        if prediction == correct_class:
            correct += 1
        if prediction == 0 and correct_class == 0:
            confusion_matrix[0,0] += 1
        if  prediction == 0 and correct_class == 1:
            confusion_matrix[0,1] += 1
        if  prediction == 0 and correct_class == 2:
            confusion_matrix[0,2] += 1
        if  prediction == 1 and correct_class == 0:
            confusion_matrix[1,0] += 1
        if  prediction == 1 and correct_class == 1:
            confusion_matrix[1,1] += 1
        if  prediction == 1 and correct_class == 2:
            confusion_matrix[1,2] += 1
        if  prediction == 2 and correct_class == 0:
            confusion_matrix[2,0] += 1
        if  prediction == 2 and correct_class == 1:
            confusion_matrix[2,1] += 1
        if  prediction == 2 and correct_class == 2:
            confusion_matrix[2,2] += 1   
    print confusion_matrix      
    print correct/total
    
if __name__ == '__main__':
    train_and_test()