# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 00:29:30 2014

Naive Bayes classifer

@author: Jerry
"""

import numpy as np

class NaiveBayes:
    
    def __init__(self, training_set, num_feature_type, smoothing, ingore_ambiguity):
        self.features_size = len(training_set[0][0])
        self.num_feature_type = num_feature_type
        self.prior = [0, 0, 0]
        observation = np.empty([3, self.features_size, num_feature_type])
        self.conditional_likelihood = np.empty([3, self.features_size, num_feature_type])
        # conditional_likelihood[i,j,k] = P(Fj = k | i)
        self.training_example_size = len(training_set)
        print 'Counting evidences'
        for features, label in training_set:
            counter = 0
            self.prior[label] += 1
            for feature in features:
                if ingore_ambiguity and feature > 3:
                    counter += 1
                    continue
                if feature == 4:
                   observation[label, counter, 0] += 1.0/3
                   observation[label, counter, 1] += 1.0/3
                   observation[label, counter, 2] += 1.0/3
                elif feature == 5:
                    observation[label, counter, 0] += 0.25
                    observation[label, counter, 1] += 0.25
                    observation[label, counter, 2] += 0.25
                    observation[label, counter, 3] += 0.25
                elif feature == 6:
                    observation[label, counter, 2] += 0.5
                    observation[label, counter, 3] += 0.5
                elif feature == 7:
                    observation[label, counter, 0] += 0.5
                    observation[label, counter, 2] += 0.5
                else:
                    observation[label, counter, feature] += 1
            
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
            
            
    def predict(self, features, prior):
        loglikelihood = [0.0, 0.0, 0.0]
        for i in range(3):
            for j in range(self.features_size):
                k = features[j]
                if k > 3:
                    continue
                loglikelihood[i] += np.log(self.conditional_likelihood[i,j,k])
        if prior:
            loglikelihood[0] += np.log(self.prior[0])
            loglikelihood[1] += np.log(self.prior[1])
            loglikelihood[2] += np.log(self.prior[2])
            
        #print 'log-likelyhood', loglikelihood
            
        return np.argmax(loglikelihood)