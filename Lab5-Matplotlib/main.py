from matplotlib import pyplot as plt
import numpy as np

def main():
    # Exercise1
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [0, 1, 4, 9, 16, 25, 36]
    
    plt.plot(x, y)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Exercise1')
    plt.show()
    
    # Exercise2
    plt.plot(x, y, marker='o', color='green', linestyle='--')
    plt.grid(True)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Exercise2')
    plt.show()
    
    # Exercise3
    categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
    values = [10, 15, 7, 12, 5]
    
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Exercise3')
    plt.show()

    # Exercise4
    data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution
    
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Exercise4')
    plt.show()

    # Exercise5
    x = np.random.rand(50) # 50 random x-values between 0 and 1
    y = np.random.rand(50) # 50 random y-values between 0 and 1

    plt.scatter(x, y)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Exercise5')
    plt.show()
    
    # Exercise6
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [5, 7, 3, 8, 6]
    data = np.random.randn(1000)
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    
    plt.subplot(2, 2, 1)
    plt.plot(x, y)
    plt.title('Exercise6-line')
    
    plt.subplot(2, 2, 2)
    plt.bar(categories, values)
    plt.title('Exercise6-bar')
    
    plt.subplot(2, 2, 3)
    plt.hist(data, bins=20, edgecolor='black')
    plt.title('Exercise6-histogram')
    
    plt.subplot(2, 2, 4)
    plt.scatter(x_scatter, y_scatter)
    plt.title('Exercise6-scatter')
    
    plt.tight_layout()
    plt.show()

    # Exercise7
    categories = ['Marketing', 'Development', 'Sales', 'Support']
    values = [20, 35, 25, 20]
    
    plt.pie(values, labels=categories)
    plt.title('Exercise7')
    plt.legend(title='Categories')
    plt.show()
    
    # Exercise8
    categories = ['Group 1', 'Group 2', 'Group 3']
    value1 = [5, 7, 3]
    value2 = [6, 8, 4]
    value3 = [4, 3, 5]

    plt.bar(categories, value1, label='Value 1')
    plt.bar(categories, value2, bottom=value1, label='Value 2')
    plt.bar(categories, value3, bottom=[i+j for i,j in zip(value1, value2)], label='Value 3')

    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Stacked Bar Plot of Categories')
    plt.legend()
    plt.show()

    # Exercise9
    dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
    dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
    dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80

    plt.boxplot([dataset1, dataset2, dataset3], tick_labels=['Dataset 1', 'Dataset 2', 'Dataset 3'])
    plt.title('Boxplot of Datasets')
    plt.xlabel('Dataset')
    plt.ylabel('Value')
    plt.show()
    
    # Exercise10
    x = range(0, 20)
    y = [value ** 2 for value in x]
    
    plt.plot(x, y)
    max_y = max(y)
    min_y = min(y)
    max_x = y.index(max_y)
    min_x = y.index(min_y)

    plt.annotate('Highest', xy=(max_x, max_y))
    plt.annotate('Lowest', xy=(min_x, min_y))

    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Exercise10')
    plt.show()

if __name__ == '__main__':
    main()