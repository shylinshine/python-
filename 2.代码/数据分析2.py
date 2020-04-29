import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(0,100).reshape((50,2)),columns=["A","B"])
print(data)
