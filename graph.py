import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output.csv")

total_hands_open = df['Hand Open'].sum()

total_hands_close = df['Hand Closed'].sum()

# print(total_hands_close)
# print(total_hands_open)

categories = ['Hands Open', 'Hands closed']
counts = [total_hands_open, total_hands_close]


plt.bar(categories, counts, color=['blue', 'red'])
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Number of People with Hands Open/Closed')

for i, count in enumerate(counts):
    plt.text(i, count + 1, str(count), ha='center')

plt.ylim(0, max(counts) + 10) 


plt.savefig('bar_graph.png')