import matplotlib.pyplot as plt
def CountFrequency(my_list):
     
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        item = round(item, 7)
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    # for key, value in freq.items():
    #     print ((key, value))

    most_frequent_number = max(freq, key=freq.get)
    print("\n\nMost Frequent Number:", most_frequent_number)
    print("Frequency:", freq[most_frequent_number])

def logistic_map(x_n, r, upper_limit = 50, lower_limit = 0):
    x,y = [], []
    last_slope = None

    for i in range(upper_limit):

        # Logistic Equation
        x_n_1 = r*x_n*(1-x_n)

        if i >= lower_limit:
            # Check Slope
            current_slope = x_n_1 - x_n                
            x.append(i+1)
            y.append(x_n_1)
            last_slope = current_slope

        x_n = x_n_1
    # CountFrequency(y)
    return [r, y]
    
    # plt.plot(x, y)
    # plt.show()

def bifurcation(arr):
    for single_r in arr:
        x = [single_r[0]]*len(single_r[1])
        plt.plot(x, single_r[1], marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="green")
    plt.show()
