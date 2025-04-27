import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_total = {
    'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Revenue ($bn)': [0.3, 0.6, 1.4, 2.2, 2.5, 2.4, 3.0, 3.4, 3.7, 5.0, 4.4, 2.9, 2.5]
}

# Create DataFrame
df_total = pd.DataFrame(data_total)

# Set style
sns.set_style("whitegrid")

# Line Plot
plt.figure(figsize=(10,6))
sns.lineplot(data=df_total, x='Year', y='Revenue ($bn)', marker='o', color='royalblue')
plt.title('Twitter Total Revenue (2012-2024)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Revenue ($bn)')
plt.xticks(df_total['Year'], rotation=45)
plt.tight_layout()
plt.show()
