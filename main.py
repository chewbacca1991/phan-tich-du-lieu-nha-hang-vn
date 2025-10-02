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
        plt.figure(figsize=(10, 5))
        plt.bar(self.data['Restaurant_Name'], self.data['Rating'])
        plt.title('Restaurant Ratings')
        plt.xlabel('Restaurant Name')
        plt.ylabel('Rating')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    analyzer = RestaurantDataAnalyzer('restaurant_data.csv')
    analyzer.analyze_data()
    analyzer.visualize_data()