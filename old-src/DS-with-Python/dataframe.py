# creating a dataframe

import pandas as pd

data = {
    "calories": [210, 352, 752],
    "duration": [10, 30, 7]
}

df = pd.DataFrame(data)

print(df)