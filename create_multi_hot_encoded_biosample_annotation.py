import h5py
import pandas as pd, numpy as np, matplotlib.pyplot as plt, gunzip
import seaborn as sns
import sys, os
from scipy import stats
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
import random
from scipy.stats import norm
from gtfparse import read_gtf
import csv
import gunzip

def sample_labels():
  
  #Gather annotation labels as provided by ARCHS4 website by running the corresponding R scripts for various biosample annotations
  annotations1 = next(os.walk('../data/cell_lines/'))[1]
  annotations2 = next(os.walk('../data/tissue_types/'))[1]
  all_annotations = annotations1 + annotations2
  
  sample_annotations = {}
  for i in range(len(all_annotations)):
    if os.path.isdir('../data/cell_lines/'+all_annotations[i]):
        path = '../data/cell_lines/'+all_annotations[i]+'/'
        files = os.listdir(path)
        samples = []
        for j in files:
            if not j.startswith('.'):
                x = pd.read_csv(path+j,sep='\t')
                x = x.drop('Unnamed: 0',axis=1)
                for k in x.columns:
                    samples.append(k)
        sample_annotations[all_annotations[i]] = samples
    else:
        path = '../data/tissue_types/'+all_annotations[i]+'/'
        files = os.listdir(path)
        samples = []
        for j in files:
            if not j.startswith('.'):
                x = pd.read_csv(path+j,sep='\t')
                x = x.drop('Unnamed: 0',axis=1)
                for k in x.columns:
                    samples.append(k)
        sample_annotations[all_annotations[i]] = samples  
  
  # Gather all annotations for a data frame
  x=[]
  for i in range(len(sample_annotations)):
    a=list(sample_annotations.values())[i]
    for j in range(len(a)):
      x.append(a[j])  
  
  comm_dict = {}
  for samp in x:
    comm_dict[samp] = [i for i in sample_annotations if samp in sample_annotations[i] ]
    
  sample_annotations_multi_hot = pd.DataFrame(columns=[all_annotations])
  for i in x:
    sample_annotations_multi_hot.loc[i,:]=0
    sample_annotations_multi_hot.loc[i,comm_dict[i]] = 1
    
  return sample_annotations_multi_hot
 
