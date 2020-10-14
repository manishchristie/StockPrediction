# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:10:37 2020

@author: W133043
"""

import numpy as np
from datetime import datetime
import smtplib
import time
from selenium import webdriver
#For Prediction
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn import preprocessing, svm
#For Stock Data
from iexfinance.stocks import Stock,get_historical_data
