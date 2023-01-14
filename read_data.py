import h5py
import pandas as pd, numpy as np

def read_expression_data():
  arch_exp = sys.argv[1]
  f = h5py.File(arch_exp,'r')
  x1 = f.get('data')
  x2 = x1.get('expression')
  exp_data = pd.DataFrame(data=x2)
  retrun exp_data
  
def main()
  exp_data=read_expression_data()
  
if __name__ == "__main__":
  main()
