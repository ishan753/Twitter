import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_users = {
    'Network': ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'WeChat', 'TikTok', 'FB Messenger',
                'Telegram', 'Snapchat', 'Douyin', 'Kuaishou', 'X (Twitter)', 'Sina Weibo', 'QQ', 'Pinterest'],
    'Active Users (MM)': [3030, 2491, 2000, 2000, 1327, 1218, 1036, 800, 750, 743, 673, 666, 599, 571, 465]
}

# Create DataFrame
df_users = pd.DataFrame(data_users)

# Sort by Active Users
df_users = df_users.sort_values(by='Active Users (MM)', ascending=True)

# Set style
sns.set_style("whitegrid")

# Horizontal Bar Plot
plt.figure(figsize=(10,8))
sns.barplot(x='Active Users (MM)', y='Network', data=df_users, palette='viridis')
plt.title('Active Users by Social Network (in Millions)', fontsize=16)
plt.xlabel('Active Users (MM)')
plt.ylabel('Network')
plt.tight_layout()
plt.show()
