
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
train_data = pd.read_csv('DailyDelhiClimateTrain.csv')
test_data = pd.read_csv('DailyDelhiClimateTest.csv')

# Merge the train and test datasets
full_data = pd.concat([train_data, test_data])

# Convert 'date' to datetime and extract year and month
full_data['date'] = pd.to_datetime(full_data['date'])
full_data['year'] = full_data['date'].dt.year
full_data['month'] = full_data['date'].dt.month

# Categorize years based on average temperature
temp_categories = pd.cut(full_data.groupby('year')['meantemp'].mean(), bins=3, labels=['Low', 'Medium', 'High'])
temp_distribution = temp_categories.value_counts()

# Set up the matplotlib figure for dashboard-style plot
plt.figure(figsize=(15, 10))
plt.suptitle("Diverse Climate Insights of Delhi (2013-2022) - Muhammad Junaid Hashmi 22057665", fontsize=16, fontweight='bold')

# Yearly Average Temperature Distribution (Pie Chart)
plt.subplot(2, 2, 1)
temp_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'salmon'])
plt.title('1. Yearly Avg. Temp. Distribution', fontsize=14)
plt.ylabel('')

# Monthly Humidity Trends (Box Plot)
plt.subplot(2, 2, 2)
sns.boxplot(x='month', y='humidity', data=full_data, palette="coolwarm")
plt.title('2. Monthly Humidity Trends', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Humidity (%)')

# Wind Speed Histogram
plt.subplot(2, 2, 3)
plt.hist(full_data['wind_speed'], bins=15, color='purple', alpha=0.7)
plt.title('3. Wind Speed Histogram', fontsize=14)
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Frequency')

# Pressure vs. Temperature Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(x='meantemp', y='meanpressure', data=full_data, color='orange')
plt.title('4. Pressure vs. Temp. Scatter Plot', fontsize=14)
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Average Pressure')

# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
