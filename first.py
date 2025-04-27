import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Advertising': [1.9, 2.2, 2.1, 2.6, 2.9, 3.2, 4.5, 4.0, 2.3, 1.7],
    'Subscription & Data Licensing': [0.2, 0.2, 0.3, 0.4, 0.4, 0.5, 0.5, 0.4, 0.6, 0.8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# 1. Line plot for trends
plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Advertising'], marker='o', label='Advertising')
plt.plot(df['Year'], df['Subscription & Data Licensing'], marker='s', label='Subscription & Data Licensing')
plt.title('Twitter Revenue by Segment (2015-2024)')
plt.xlabel('Year')
plt.ylabel('Revenue ($bn)')
plt.legend()
plt.tight_layout()
plt.show()