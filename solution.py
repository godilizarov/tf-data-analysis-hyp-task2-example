import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 419801345 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.07
    statistic, p_value = ks_2samp(x, y) 
    return p_value < alpha
