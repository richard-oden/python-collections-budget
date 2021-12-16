import matplotlib.pyplot as plt
import collections
from . import Expense

# create expenses.list based on csv data:
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

# get top 5 spending categories:
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common()

# create bar chart:
categories, count = zip(*top5)
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()