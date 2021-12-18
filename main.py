import re

import pandas as pd

df = pd.read_excel(r"C:\Users\Lucas Manzotti\Desktop\provaxlsx.xlsx", sheet_name='Plan1')
df['Nome Programa / Emissora'] = df['Nome Programa / Emissora'].str.lower()
df['Rat#'] =  [re.sub('[^0-9]','', str(x)) for x in df['Rat#']]
df.to_excel(r"C:\Users\Lucas Manzotti\Desktop\provaxlsx.xlsx", index = False)
print(df)
