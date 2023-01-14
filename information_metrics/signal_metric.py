import h5py
import pandas as pd, numpy as np, matplotlib.pyplot as plt, gunzip
import seaborn as sns
import sys, os
from scipy import stats
from read_data import read_expression_data
from normalization.gene_expression_normalization import normalize

def top_p_percentile_signal(p):
    exp_data = read_expression_data()
    exp_data = normalize(exp_data)
    N=len(exp_data)
    M=len(exp_data.columns)
    top_signal=[]
    for i in range(N):
        exp_data_i = 1 + exp_data.iloc[i,:]
        row_mean = np.mean(exp_data_i)
        signal = np.percentile((exp_data_i)/row_mean,p)
        top_signal.append(signal)
    return top_signal
  
  
def main():
    sig95=top_p_percentile_signal(95)
   
if __name__ == "__main__":
    main()
