"""Exercise week 5"""
"""Part 1"""
# Example using TransactonEncoder, and the aprirori
# Read the comments which attempt to explain the code
# http://rasbt.github.io/mlxtend/user_guide/preprocessing/TransactionEncoder/
# http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/
from csv import reader
import pandas as pd
import numpy as np

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

pd.set_option('display.max_columns',20)
# pd.set_option('display.max_rows',30)
pd.set_option('display.max_rows',None)  # print all the rows
pd.set_option('display.width',None)   # allow long lines to get rid of ...


## Use this to read data from the csv file on local system.
# df = pd.read_csv('./retailDataset.csv', sep=',')

# data represented as  list of lists
theData = [
['milk','onion','egg','bread','chili'],
['milk','egg','bread','chili'],
['milk','garlic','beans','chili'],
['milk','egg','beans','chili'],
['milk','onion','egg','bread'],
['milk','onion','egg'],
['garlic','onion','beans'],
['garlic','onion','beans'],
['garlic','onion','beans'],
['garlic','onion','beans'],
['chili','garlic','onion','beans'],
['chili','garlic','onion','beans'],
['garlic','onion','milk'],
['garlic','onion'],
['garlic','chili'],
['garlic','chili'],
['milk','onion','egg'],
['milk','onion','egg'],
['milk','onion','egg','bread'],
['milk','onion','chili','bread'],
]

# theData = []
# with open('exercise5b_input.csv.txt', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     for row in csv_reader:
#         theData.append(row)
    
print(theData)
print(len(theData))

# use transaction encoder to transform into an 1-hot boolean encoded numpy arrayk
te = TransactionEncoder()
te_ary = te.fit(theData).transform(theData)
print("\n\nte_ary returned from TransactionEncoder.fit().transform():")
print(te_ary)

# convert into a data fram for convience and to pass into apriori
df2 = pd.DataFrame(te_ary,columns = te.columns_)

print("\n\nDataFrame version:")
print(df2.head(25))



# Call apriori to find frequent itemsets with min_support = 30%
freq_items = apriori(df2,min_support=0.3,use_colnames=True)
print("\n\nfreq_items:")
print(freq_items)


#for index, row in freq_items.iterrows():
#	print(str(row[0]) + ' ' + str(row[1]) )


# add a column to freq_items that contains the number of items in the itemset
freq_items['length'] = freq_items['itemsets'].apply(lambda x: len(x))
print(type(freq_items))
print( freq_items.columns)
print(freq_items)


# examples of how to filter your itemsets further, for illustration only, not actually used below
# NOTE: Do not assign back to freq_items because may remove rows need by association_rules() function below
reducedFreqItems = freq_items[(  ((freq_items['length'] == 2) &  (freq_items['support'] >= 0.40)) |
	((freq_items['length'] >= 3) &  (freq_items['support'] >= 0.30)) )]
# reducedFreqItems = freq_items[ (freq_items['length'] >= 2) &  (freq_items['support'] >= 0.35) ]
print("\n\nReduced freq_items (length == 2 & support >= 40%) | (length >=3 & support >= 30%) ")
print(reducedFreqItems)

# now mine the rules by calling association_rules
print("\n\nThe rules:")
rules = association_rules(freq_items, metric="confidence", min_threshold=0.7)
print(type(rules))

# rename columns "antecedents support" to "antsup" and "consequents support" to "consup" so print nicer table
rules.columns = [ 'antecedents', 'consequents', 'antsup', 'consup', 'support', 'confidence', 'lift', 'leverage', 'conviction']
print(rules.columns)
# print( rules[ ["antecedents","consequents","support","confidence","lift"] ] )
# print( rules[ ["antecedents","antsup","consequents","consup","support","confidence","lift"] ] )
print( rules[ ["antecedents","consequents","antsup","consup","support","confidence","lift"] ] )

# print("rules.head(20):")
# print( rules.head(20) )

"""1) Using the values already set in the code
(i.e. apriori min_support = 0.3, association_rule min_threshold = 0.7) look at the result an answer: """

"""a) which 1-itemset has the greatest support? """
# Onion: support = 75% 
"""b) which 3-itemsets have suupport >= 0.3? """
# (garlic, beans, onion) and (egg, milk, onion)
"""c) why do the two rules (milk->egg and egg->milk) have different confidence values? """
# Milk is more popular than egg, so it appears more in the data set. The support for milk is 55% while the support for egg is 45%.
"""d) Which rules are not "interesting"?  Why do you say that? """
# beans -> onion: lift = 1
# egg -> onion: lift = 1
# egg, milk -> onion: lift = 1
"""e) two rules have a lift value < 1.0  (garlic->onion and milk->onion).  Why are these especially useless rules? """
# These are the top three most popular items and onion is the most popular item in the list. The confidence 

"""Part 2"""

theData = []
with open('exercise5b_input.csv.txt', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        theData.append(row)
    
print(theData[29])
# checkpd = pd.DataFrame(theData)
# print(checkpd)

"""1) Using the values already set in the code"""
"""(i.e. apriori min_support = 0.3, association_rule min_threshold = 0.7) look at the result an answer: """
# use transaction encoder to transform into an 1-hot boolean encoded numpy arrayk
te = TransactionEncoder()
te_ary = te.fit(theData).transform(theData)

print("\n\nte_ary returned from TransactionEncoder.fit().transform():")
print(te_ary)

# convert into a data fram for convience and to pass into apriori
df2 = pd.DataFrame(te_ary,columns = te.columns_)
print("\n\nDataFrame version:")
print(df2['jaggery'][36])
# print(df2.head(75))
print(len(te.columns_))

# Call apriori to find frequent itemsets with min_support = 30%
freq_items = apriori(df2,min_support=0.03,use_colnames=True)
print("\n\nfreq_items:")
print(freq_items)

# now mine the rules by calling association_rules
print("\n\nThe rules:")
rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)
print(type(rules))

# rename columns "antecedents support" to "antsup" and "consequents support" to "consup" so print nicer table
rules.columns = [ 'antecedents', 'consequents', 'antsup', 'consup', 'support', 'confidence', 'lift', 'leverage', 'conviction']
print(rules.columns)
# print( rules[ ["antecedents","consequents","support","confidence","lift"] ] )
# print( rules[ ["antecedents","antsup","consequents","consup","support","confidence","lift"] ] )
print( rules[ ["antecedents","consequents","antsup","consup","support","confidence","lift"] ] )


"""a) Which are the three most common ingredients? (i.e most common 1-itemsets) """
# garam masala: support = .105882
# ginger: support = .113725
# sugar: support = .188235
"""b) What is the most common pair of ingreditents? (i.e most common 2-itemset) """
#  (ghee, sugar): support = 0.062745
"""c) What are your 3-5 most "interesting" rules? """
#
