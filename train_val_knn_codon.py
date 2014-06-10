# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 17:54:23 2014

@author: Jerry
"""


import data_processor as dp
from feature_selection import Features
from knn import KNN

def train_and_val():
    training_data = dp.read_data('dataset/splice-Xtrain.dat', 'dataset/splice-Ytrain.dat')
    training_set_indices, validation_set_indices = dp.read_training_val_set('dataset/train.txt', 'dataset/val.txt')
    feature = Features()    
    features_labels_pair = feature.simple(training_data)
    training_set = []
    for index in training_set_indices:
        training_set.append(features_labels_pair[index])
    
    dp.remove_ambiguous_entry(training_set)
    k_nn = KNN(training_set, 19, KNN.quadratic_weight)
    
    error_count = 0
    num_recalled1 = 0
    num_recalled2 = 0
    num_correct_prediction1 = 0
    num_correct_prediction2 = 0
    num_class2 = 0
    num_class1 = 0
    num_class1_prediction = 0
    num_class2_prediction = 0
    
    validation_set = []
    for index in validation_set_indices:
        validation_set.append(features_labels_pair[index])
    
    dp.remove_ambiguous_entry(validation_set)
    for feature_vector, correct_class in validation_set: 
        prediction = k_nn.predict_diff_bases(feature_vector)
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
    
def generate_train_val():
    training_data = dp.read_data('dataset/splice-Xtrain.dat','dataset/splice-Ytrain.dat')
    dp.generate_training_val_set(len(training_data), 'dataset/train.txt', 'dataset/val.txt')
    

if __name__ == '__main__':
    #generate_train_val()
    train_and_val()
