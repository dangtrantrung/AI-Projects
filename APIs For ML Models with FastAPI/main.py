import io
import pickle
import numpy as np
import urllib.request
from urllib.request import urlopen

from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
