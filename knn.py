# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 23:46:32 2014

K-Nearest Neighbors classifier.

@author: Jerry
"""

import numpy as np
import heapq

class KNN:
    def __init__(self, training_set, k):
        self.k = k
        self.instances = training_set
    
    def predict(self, features):
        