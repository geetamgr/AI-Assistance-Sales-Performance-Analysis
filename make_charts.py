import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
COLOR = '#2E5B8C'
ACCENT = '#D97A3E'

def money_fmt(ax, axis='y'):
    fmt = mticker.FuncFormatter(lambda x, _: f'${x:,.0f}')
    (ax.yaxis if axis == 'y' else ax.xaxis).set_major_formatter(fmt)

# 1. Revenue by region (rolled up) + by rep
q1 = pd.read_csv('results/q1_revenue_by_region_rep.csv')
region_tot = q1.groupby('region')['total_revenue'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(region_tot.index, region_tot.values, color=COLOR)
ax.set_title('Net Revenue by Region')
ax.set_ylabel('Net Revenue')
money_fmt(ax)
for i, v in enumerate(region_tot.values):
    ax.text(i, v + 5000, f'${v:,.0f}', ha='center', fontsize=9)
plt.tight_layout()
plt.savefig('charts/01_revenue_by_region.png', dpi=150)
plt.close()

# 2. Monthly revenue trend, gross vs net
q2 = pd.read_csv('results/q2_monthly_revenue_trend.csv')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(q2['month'], q2['gross_revenue'], marker='o', label='Gross Revenue', color=COLOR)
ax.plot(q2['month'], q2['net_revenue'], marker='o', label='Net Revenue', color=ACCENT)
ax.set_title('Monthly Revenue Trend (Gross vs Net)')
ax.set_ylabel('Revenue')
money_fmt(ax)
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/02_monthly_revenue_trend.png', dpi=150)
plt.close()

# 3. Avg discount by category (rolled up from product level)
q3 = pd.read_csv('results/q3_margin_by_product.csv')
cat_disc = q3.groupby('category').apply(
    lambda g: (g['gross_revenue'] - g['net_revenue']).sum() / g['gross_revenue'].sum()
).sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(cat_disc.index, cat_disc.values * 100, color=COLOR)
ax.set_title('Effective Discount Rate by Category')
ax.set_ylabel('Discount Rate (%)')
for i, v in enumerate(cat_disc.values * 100):
    ax.text(i, v + 0.1, f'{v:.1f}%', ha='center', fontsize=9)
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig('charts/03_discount_by_category.png', dpi=150)
plt.close()

# 4. Channel comparison: revenue vs discount
q4 = pd.read_csv('results/q4_channel_comparison.csv')
fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(q4['channel'], q4['total_net_revenue'], color=COLOR, label='Net Revenue')
ax1.set_ylabel('Net Revenue', color=COLOR)
money_fmt(ax1)
ax2 = ax1.twinx()
ax2.plot(q4['channel'], q4['avg_discount'] * 100, color=ACCENT, marker='o', linewidth=2, label='Avg Discount %')
ax2.set_ylabel('Avg Discount (%)', color=ACCENT)
ax1.set_title('Channel Comparison: Revenue vs Avg Discount')
plt.tight_layout()
plt.savefig('charts/04_channel_comparison.png', dpi=150)
plt.close()

# 5. Return rate by category (rolled up)
q5 = pd.read_csv('results/q5_return_rate.csv')
cat_returns = q5.groupby('category').apply(
    lambda g: 100 * g['returned_orders'].sum() / g['total_orders'].sum()
).sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(cat_returns.index, cat_returns.values, color=ACCENT)
ax.set_title('Return Rate by Category')
ax.set_ylabel('Return Rate (%)')
for i, v in enumerate(cat_returns.values):
    ax.text(i, v + 0.1, f'{v:.1f}%', ha='center', fontsize=9)
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig('charts/05_return_rate_by_category.png', dpi=150)
plt.close()

print("charts written:")
import os
for f in sorted(os.listdir('charts')):
    print(' -', f)
