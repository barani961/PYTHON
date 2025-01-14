
import pandas as pd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df = pd.DataFrame({'numbers': numbers})
filtereval = df.eval('numbers > 5')
filterquery = df.query('numbers > 5')
print("Filtered using eval():")
print(df[filtereval])
print("\nFiltered using query():")
print(filterquery)
