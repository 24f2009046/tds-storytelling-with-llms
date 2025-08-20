# Email: 24f2009046@ds.study.iitm.ac.in 

import pandas as pd
import matplotlib.pyplot as plt

# Monthly Recurring Revenue (MRR) Growth - 2024 Quarterly Data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'MRR_Growth': [7.51, 9.85, 7.32, 10.63]
}
df = pd.DataFrame(data)

# Calculate the average MRR growth
average_mrr = df['MRR_Growth'].mean()
print(f"Average MRR Growth: {average_mrr:.2f}")

# Industry benchmark
industry_target = 15

# Create a bar plot to visualize the trend and benchmark comparison
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Quarter'], df['MRR_Growth'], color='skyblue', label='Quarterly MRR Growth')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target}%)')
plt.axhline(y=average_mrr, color='g', linestyle='-.', label=f'Average MRR ({average_mrr:.2f}%)')

# Add values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.title('2024 Quarterly MRR Growth vs. Industry Target')
plt.xlabel('Quarter')
plt.ylabel('MRR Growth (%)')
plt.ylim(0, 18)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Save the plot
plt.savefig('mrr_growth_visualization.png')
