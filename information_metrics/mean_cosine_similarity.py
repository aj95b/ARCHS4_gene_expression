import h5py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import seaborn as sns
import sys, os
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances 
from scipy.spatial import distance
from read_data import read_expression_data
from normalization.normalize_gene_expression import normalize

def mean_cosine_similarity_v3(p,q):
  #p and q are the start and end indices of the biosamples in the sorted expression for a gene; these would be around 95%ile
    exp_data = read_expression_data()
    exp_data = normalize(exp_data)
    N = len(exp_data)
    M = len(exp_data.columns)
    for i in range(N):
        k = np.count_nonzero(exp_data.iloc[i,:]) #Find out if gene has no readouts for any samples and skip the iteration
        if k==0: 
            print(np.nan)
            continue
        elif k==1: #Find out if gene has readouts in just one sample and so make the metric zero and skip
            print(0)
            continue
        signal_sample_ind = exp_data.iloc[i,:].sort_values().index[p:q]
        num_signals = len(signal_sample_ind)
        sum_similarity=np.sum(cosine_similarity(np.transpose(exp_data.iloc[:,signal_sample_ind])))
        mean_similarity=sum_similarity/((num_signals*(num_signals-1))/2)
        print(mean_similarity)
        
        
def main():
    #Rank of 95 percentile value given no. of biosamples in ARCHS4
    rank=0.95*(620824+1)
    p=int(rank)-50
    q=int(rank)+50
    mean_cosine_similarity_v3(p,q)

	 	
if __name__ == "__main__":
	main()
