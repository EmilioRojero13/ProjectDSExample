import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def preprocedata(self, data):
        pass
    
    def load_data(self):
        data = pd.read_csv(self.path)
        return data