import pandas as pd
import pickle

# fungsi untuk load dataset
def load_dataset(filename):
    dataFrame = pd.read_csv(filename, header = -1)
    dataArray = dataFrame.values
    return dataArray