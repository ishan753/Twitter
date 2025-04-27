import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_revenue = {
    'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Revenue ($bn)': [0.3, 0.6, 1.4, 2.2, 2.5, 2.4, 3.0, 3.4, 3.7, 5.0, 4.4, 2.9, 2.5]
}

# Create DataFrame
df_revenue = pd.DataFrame(data_revenue)

# Set style
sns.set_style("whitegrid")

# Bar Plot
plt.figure(figsize=(12,6))
sns.barplot(x='Year', y='Revenue ($bn)', data=df_revenue, color='skyblue')
plt.title('Twitter Total Revenue (2012-2024)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Revenue ($bn)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
