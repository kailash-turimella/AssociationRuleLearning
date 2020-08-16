"""
Eclat

   Set a minimum support and the minimum number of items in a set(M)
   The algorithm checks how many times that set has occured in the dataset
   Arranges in descending order of their support
"""
# Importing the libraries
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Training the Eclat model on the dataset
from apyori import apriori
rules = apriori(transactions,          # the data(as list)
                min_support = 0.003,   # items bought more frequently will be included
                min_confidence = 0.2,  # rules with a confidence less than 0.2 are ignored
                min_lift = 3,          # lift - relevance of the rules
                min_length = 2,        # minimum number of items in a rule
                max_length = 3)        # maximum number of items in a rule
#min_support = x * 7/total number of transactions
#we want the support for products purchased at least x times a day

# Visualising the results

## Displaying the first results coming directly from the output of the apriori function
results = list(rules)
results

## Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

## Displaying the results sorted by descending supports
resultsinDataFrame.nlargest(n = 10, columns = 'Support')
