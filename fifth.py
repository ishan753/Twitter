import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_users = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Users (MM)': [40, 85, 151, 218, 271, 304, 313, 310, 298, 312, 347, 362, 401, 421, 388]
}

# Create DataFrame
df_users = pd.DataFrame(data_users)

# Set style
sns.set_style("whitegrid")

# Line Plot
plt.figure(figsize=(12,6))
sns.lineplot(data=df_users, x='Year', y='Users (MM)', marker='o', color='teal')
plt.title('Twitter Users (2010-2024)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Users (in Millions)')
plt.xticks(df_users['Year'], rotation=45)
plt.tight_layout()
plt.show()
