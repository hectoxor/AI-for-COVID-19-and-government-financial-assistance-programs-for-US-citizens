import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from google.colab import drive
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
!pip install optuna
import optuna
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
drive.mount('/content/gdrive')
df = pd.read_csv('/content/gdrive/My Drive/Census-Income.csv')
