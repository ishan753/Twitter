import pandas as pd
import matplotlib.pyplot as plt

# Data
data_age = {
    'Age Bracket': ['13-17', '18-24', '25-34', '35-49', '50+'],
    'Percentage': [2, 32.1, 37.5, 21.1, 7.3]
}

# Create DataFrame
df_age = pd.DataFrame(data_age)

# Pie Chart
plt.figure(figsize=(8,8))
plt.pie(df_age['Percentage'], labels=df_age['Age Bracket'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title('Twitter Users by Age Bracket')
plt.axis('equal')  # Equal aspect ratio ensures the pie is a circle.
plt.tight_layout()
plt.show()
