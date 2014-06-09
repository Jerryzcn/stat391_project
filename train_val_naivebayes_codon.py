# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 15:18:19 2014

@author: Jerry
"""
import data_processor as dp
from feature_selection import Features
from naive_bayes import NaiveBayes

def train_and_val():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    training_set_indices, validation_set_indices = dp.read_training_val_set('dataset/train.txt', 'dataset/val.txt')
    feature = Features()    
    features_labels_pair = feature.simple(training_data)
    training_set = []
    for index in training_set_indices:
        training_set.append(features_labels_pair[index])
    
    naive_bayes = NaiveBayes(training_set, 32, False, False)
    
    error_count = 0
    num_recalled1 = 0
    num_recalled2 = 0
    num_correct_prediction1 = 0
    num_correct_prediction2 = 0
    num_class2 = 0
    num_class1 = 0
    num_class1_prediction = 0
    num_class2_prediction = 0
    
    for index in validation_set_indices:
        feature_vector, correct_class = features_labels_pair[index]
        prediction = naive_bayes.predict(feature_vector)
        if  prediction != correct_class:
            error_count += 1
        if correct_class == 1:
            num_class1 += 1
            if prediction == 1:
                num_recalled1 += 1
        if correct_class == 2:
            num_class2 += 1
            if prediction == 2:
                num_recalled2 += 1
        if prediction == 1:
            num_class1_prediction += 1
            if correct_class == 1:
                num_correct_prediction1 += 1
        if prediction == 2:
            num_class2_prediction += 1
            if correct_class == 2:
                num_correct_prediction2 += 1
        #print prediction, correct_class
    error_rate = float(error_count)/len(validation_set_indices)
    print 'error rate:', error_rate
    print 'recall of class 1:', float(num_recalled1)/num_class1
    print 'recall of class 2:', float(num_recalled2)/num_class2  
    print 'precision of class 1:', float(num_correct_prediction1)/num_class1_prediction    
    print 'precision of class 2:', float(num_correct_prediction2)/num_class2_prediction    
    
if __name__ == '__main__':
    train_and_val()