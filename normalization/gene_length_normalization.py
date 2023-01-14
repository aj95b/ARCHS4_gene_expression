import h5py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sys, os
from scipy import stats
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
import random
from scipy.stats import norm
from gtfparse import read_gtf
import qnorm


def find_gene_length(exp_data):
    gencode=read_gtf("../../genome_25kb/data/gencode.v41.annotation.gtf") ## Replace with path to latest gencode GTF file
    gene_len_info=pd.DataFrame()
    k = 0 #index to use for intersection of genes
    intersection_genes=set(gencode.gene_name).intersection(set(exp_data.index))
    #for i in exp_data.index:
    for i in intersection_genes:
        #if i in gencode.gene_name:
            gene_len_info.loc[k,'gene_name']=i
            transcript_lengths=[]
            all_transcripts=np.where((gencode.gene_name==i)&(gencode.feature=='transcript'))[0]
            M = len(all_transcripts)
            max_transcript=0
            for j in range(M):
                current_transcript_length=gencode.end[all_transcripts[j]]-gencode.start[all_transcripts[j]]
                if current_transcript_length > max_transcript:
                    max_transcript = current_transcript_length
            gene_len_info.loc[k,'length'] = max_transcript
            k = k+1
    return gene_len_info
  
 def gene_length_normalization(df_input,gene_len_info):
    gene_list = list(set(gencode.gene_name).intersection(set(df_input.index)))
    df_input = df_input.loc[gene_list,:]
    for gene in df_input.index:
        df_input.loc[gene,:] = df_input.loc[gene,:]/gene_len_info.length[np.where(gene_len_info.gene_name==gene)[0][0]]
    return df_input
