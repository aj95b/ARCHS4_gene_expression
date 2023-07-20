import h5py
import pandas as pd, numpy as np
from create_multi_hot_encoded_biosample_annotation import sample_labels

def read_expression_data():
  arch_exp = sys.argv[1]
  f = h5py.File(arch_exp,'r')
  x1 = f.get('data')
  x2 = x1.get('expression')
  exp_data = pd.DataFrame(data=x2)
  y1 = f.get('meta')
  y2 = y1.get('genes')
  gene_sym = y2.get('gene_symbol')
  gene_id = pd.DataFrame(data=gene_sym,columns=['gene_id'])
  gene_id=gene_id.iloc[:,0].apply(lambda s: s.decode('utf-8'))
  gene_id=pd.DataFrame(data=gene_id)
  y1 = f.get('meta')
  y3=y1.get('samples')
  geo_acc = y3.get('geo_accession')
  samp_id = pd.DataFrame(data=geo_acc,columns=['geo_acc'])
  samp_id = samp_id.iloc[:,0].apply(lambda s: s.decode('utf-8'))
  samp_id = pd.DataFrame(data=samp_id)
  exp_data.columns=list(samp_id.iloc[:,0])
  exp_data.index=list(gene_id.iloc[:,0]) 
  
  # Only keep the slice of expression data that has annotations of sample type available
  sample_anno = sample_labels()
  exp_data = exp_data[sample_anno.index]
  return exp_data
  
def main():
  exp_data=read_expression_data()
  
  
if __name__ == "__main__":
  main()
