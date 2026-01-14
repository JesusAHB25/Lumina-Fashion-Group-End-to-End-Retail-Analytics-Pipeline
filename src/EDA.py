# TASK 1: DATA PREPARATION

master_df['date'] = pd.to_datetime(master_df['date'])
master_df['month'] = master_df['date'].dt.month      
master_df['year'] = master_df['date'].dt.year        
master_df['day_name'] = master_df['date'].dt.day_name()

# TASK 2: SEASONAL TREND ANALYSIS

# TASK 2.1: Seasonal Trends Analysis:

yearly_monthly_trend = master_df['net_revenue'].groupby([master_df['year'], master_df['month']]).sum().reset_index()

sns.set_style('whitegrid')
sns.lineplot(data=yearly_monthly_trend, x='month', y='net_revenue', 
             hue='year', marker='o', palette='YlGnBu') 

plt.title('Total Revenue per Month')
plt.xlabel('Month')
plt.ylabel('Total Net Revenue')

plt.legend(title='Years', loc='upper left')
plt.xticks(ticks=range(1,13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.yticks(ticks=plt.yticks()[0], labels=[f'${int(y/1e3)}K' for y in plt.yticks()[0]])

plt.show()

# TASK 2.2: Seasonal Sales Count Analysis:

seasonal_trend = master_df.groupby(['month', 'season']).size().reset_index(name='sales_count')

sns.barplot(data=seasonal_trend, x='month', y='sales_count', hue='season', palette='BuPu')

plt.title('Sales Count per Month & Season')
plt.xlabel('Month')
plt.ylabel('Sales Count')

plt.legend(title='Season', loc='lower right')
plt.xticks(ticks=range(0,12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.show()

# TASK 3: Performance by Region & Store:

region_performance = master_df['net_revenue'].groupby(master_df['region']).sum().reset_index().sort_values(by='net_revenue', ascending=False)

sns.barplot(data=region_performance, x='net_revenue', y='region', hue = 'region', orient='h', palette='BuPu')

plt.title('Total Revenue by Region')
plt.xlabel('Total Net Revenue')
plt.ylabel('Region')

plt.xticks(ticks=plt.xticks()[0], labels=[f'${int(x):,}' for x in plt.xticks()[0]], size=8)

plt.show()

# TASK 4.1: Attributes Analysis.

attribute_performance = pd.crosstab(master_df['category'], master_df['color'])

sns.heatmap(data=attribute_performance, cmap = 'YlGnBu')
plt.xlabel('Color')
plt.ylabel('Category')
plt.title('Sales Count by Category and Color')
plt.show()

# Task 4.2: Discount Impact Analysis.

discount_analysis = master_df.groupby('discount_pct').agg({'quantity': 'median', 'net_revenue': 'sum'}).reset_index()
discount_analysis.columns = ['discount_pct', 'median_quantity', 'total_net_revenue']

sns.barplot(data=discount_analysis, x='discount_pct', y='total_net_revenue', hue='discount_pct', palette='YlGnBu')

plt.title('Total Net Revenue by Discount Percentage')
plt.xlabel('Discount Percentage')
plt.ylabel('Total Net Revenue')

plt.xticks(ticks=plt.xticks()[0], labels=[f'{int(x*10)}%' for x in plt.xticks()[0]])
plt.yticks(ticks=plt.yticks()[0], labels=[f'${int(y/1e6)}M' for y in plt.yticks()[0]])
plt.legend(title='Discount Percentage', loc='upper right')

plt.show()
