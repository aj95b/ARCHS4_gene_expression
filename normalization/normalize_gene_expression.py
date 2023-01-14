import h5py
import pandas as pd, numpy as np, matplotlib.pyplot as plt, gunzip
from gtfparse import read_gtf
import csv
import gunzip
import qnorm
from normalization.gen_len_normalization import find_gene_length, gene_length_normalization

def normalize(exp_data):
  # Biosample normalization, column wise to make all biosamples have similar distribution
  exp_data = qnorm.quantile_normalize(np.log2(1+exp_data),axis=1)  
  # Row-wise or gene length normalization
  gene_len_info = find_gene_length(exp_data)
  exp_data = gene_length_normalization(exp_data,gene_len_info)
  return exp_data
