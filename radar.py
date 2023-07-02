# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 18:17:53 2023

@author: ASUS
"""


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from soccerplots.radar_chart import Radar
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import math
from yellowbrick.cluster import KElbowVisualizer
import warnings
warnings.filterwarnings('ignore')

   ind = df[df['Player'] == player_list[0][0]].index[0]
   df['Similarity Score'] = ''
   #Assign similarity score 0 for player in question
   df['Similarity Score'][ind] = 0