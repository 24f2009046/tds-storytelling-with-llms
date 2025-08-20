import matplotlib.pyplot as plt

# Quarterly MRR Growth Data (2024)
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [7.51, 9.85, 7.32, 10.63]
industry_target = 15
average_growth = sum(mrr_growth) / len(mrr_growth)

# Print summary to console
print("Quarterly MRR Growth:", mrr_growth)
print("Average MRR Growth:", round(average_growth, 2))

# Visualization
plt.figure(figsize=(8, 5))
plt.plot(quarters, mrr_growth, marker="o", linestyle="-", label="Company MRR Growth")
plt.axhline(y=industry_target, color="r", linestyle="--", label=f"Industry Target ({industry_target})")
plt.title("Quarterly_MRR_Growth_vs_Industry_Benchmark_(2024)")
plt.xlabel("Quarter_")
plt.ylabel("MRR_Growth_(%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig("mrr_growth_trend.png")
plt.show()

