# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 00:29:30 2014

Naive Bayes classifer

@author: Jerry
"""

import numpy as np

class NaiveBayes:
    
    def __init__(self, training_set, num_feature_type, smoothing):
        self.features_size = len(training_set[0][0])
        self.num_feature_type = num_feature_type
        self.prior = [0, 0, 0]
        observation = np.zeros([3, self.features_size, num_feature_type])
        self.conditional_likelihood = np.empty([3, self.features_size, num_feature_type])
        # conditional_likelihood[i,j,k] = P(Fj = k | i)
        self.training_example_size = len(training_set)
        print 'Counting evidences'
        for features, label in training_set:
            counter = 0
            self.prior[label] += 1
            for feature in features:
                for letter in feature:
                    observation[label, counter, letter] += 1.0/len(feature)                        
                counter += 1
        self._learn_model(observation, smoothing)
        
    def _learn_model(self, observation, smoothing):
        #print observation
        for i in range(3):
            for j in range(self.features_size):
                for k in range(self.num_feature_type):
                    if smoothing:
                        #laplace smoothing
                        self.conditional_likelihood[i,j,k] = (observation[i,j,k]+1)/(self.prior[i]+self.num_feature_type)
                    else:
                        self.conditional_likelihood[i,j,k] = observation[i,j,k]/self.prior[i]
        
        self.prior[0] = float(self.prior[0])/self.training_example_size
        self.prior[1] = float(self.prior[1])/self.training_example_size
        self.prior[2] = float(self.prior[2])/self.training_example_size
        print 'prior' ,self.prior
            
            
    def predict(self, features):
        loglikelihood = [0.0, 0.0, 0.0]
        for i in range(3):
            for j in range(self.features_size):
                k = features[j][0]
                if len(features[j]) != 1:
                    continue
                loglikelihood[i] += np.log(self.conditional_likelihood[i,j,k])

        loglikelihood[0] += np.log(self.prior[0])
        loglikelihood[1] += np.log(self.prior[1])
        loglikelihood[2] += np.log(self.prior[2])
            
        #print 'log-likelyhood', loglikelihood
            
        return np.argmax(loglikelihood)