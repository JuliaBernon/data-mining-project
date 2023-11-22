# use this file to test the apriori algorithm on a simple example

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules

# create a list of transactions
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]
# print(dataset)

# create a dataframe from the list of transactions
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
# print(df)

# apply the apriori algorithm
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)

# print the association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print(rules)

frequent_itemsets.plot(kind='bar', x='itemsets', y='support')
plt.xlabel('Merchandise types')
plt.show()

rules.plot(kind='bar', x='antecedents', y='confidence')
plt.xlabel('Merchandise types')
plt.show()

frequent_itemsets.to_csv("./frequent_itemsets_test.csv")
rules.to_csv("./association_rules_test.csv")
