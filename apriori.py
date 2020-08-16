"""
Apriori

Step 1 - Set minimum support and confidence
         There are too many combinations generated and it's not possible to compute them all
Step 2 - Take all subsets with a higher support than the minimum support
Step 3 - Take all the rules of the subset with a higher confidence than the minimum confidence
Step 4 - Sort rules in descending order of their lifts 

Support(M) =  number of users that watched M
              ------------------------------              (chanced of people watching M)
                  total number of users

Confidence(M1 --> M2) =  number of users that watched M1 and M2
                         --------------------------------------       (chances of people watching M2 after M1)
                           number of users that watched M1

Lift(M1 --> M2) =  Confidence(M1 --> M2)
                   ---------------------    (chances of people watching M2 after M1
                        Support(M2)                    compared to the chances of people watching M2 directly)
"""
# Importing libraries
import pandas as pd


# Importing datasets
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)  # The data has no heading
# Converting dataframe into a list
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions,          # the data(as list)
                min_support = 0.003,   # items bought more frequently will be included
                min_confidence = 0.2,  # rules with a confidence less than 0.2 are ignored
                min_lift = 3,          # lift - relevance of the rules
                min_length = 2)        # minimum number of items in a rule
#min_support = x * 7/total number of transactions
#we want the support for products purchased at least x times a day


# Displaying the first results coming directly from the output of the apriori function
results = list(rules)
results

# Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = 
                                  ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

# Displaying the results non sorted
resultsinDataFrame

# Displaying the results sorted by descending lifts
resultsinDataFrame.nlargest(n = 10, columns = 'Lift')
