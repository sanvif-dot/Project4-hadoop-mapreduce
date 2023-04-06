import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('hadoop-mapred/output/output_sales_mapred.csv', header=None, names=['Product', 'Price'])

# Sort the DataFrame in descending order based on the price column
df_sorted = df.sort_values(by='Price', ascending=False)

# Select the top 5 rows from the sorted DataFrame
df_top5 = df_sorted.head(5)

# Create a bar chart using matplotlib
plt.bar(df_top5['Product'], df_top5['Price'])

# Set the x-axis label
plt.xlabel('Product')

# Set the y-axis label
plt.ylabel('Price')

# Set the title
plt.title('Top 5 Products by Price')

# Save the chart as a PNG file in the output folder
plt.savefig('hadoop-mapred/output/top5_products.png')
