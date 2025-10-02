import pandas as pd
import matplotlib.pyplot as plt

class RestaurantDataAnalyzer:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)

    def analyze_data(self):
        # Basic data analysis
        print(self.data.describe())

    def visualize_data(self):
        # Data visualization
        plt.figure(figsize=(12, 6))  # Increased figure size for better visibility
        plt.bar(self.data['Restaurant_Name'], self.data['Rating'], color='skyblue')
        plt.title('Restaurant Ratings', fontsize=16)
        plt.xlabel('Restaurant Name', fontsize=14)
        plt.ylabel('Rating', fontsize=14)
        plt.xticks(rotation=90, fontsize=10)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    analyzer = RestaurantDataAnalyzer('restaurant_data.csv')
    analyzer.analyze_data()
    analyzer.visualize_data()