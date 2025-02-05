# =================================================================
# Class_Ex1:
#  Use the following dataframe as the sample data.
# Find the conditional probability of Char given the Occurrence.
# ----------------------------------------------------------------
print(20 * '-' + 'Begin Q1' + 20 * '-')
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'Char': ['f', 'b', 'f', 'b', 'f', 'b', 'f', 'f'], 'Occurance': ['o1', 'o1', 'o2', 'o3', 'o2', 'o2', 'o1', 'o3'],
     'C': np.random.randn(8), 'D': np.random.randn(8)})

# Calculate the joint probability of Char and Occurrence and reset the index
joint_prob = df.groupby(['Char', 'Occurance']).size().reset_index(name='JointProbability')

# Calculate the marginal probability of Occurrence and reset the index
marginal_prob_occurrence = df['Occurance'].value_counts().reset_index()
marginal_prob_occurrence.columns = ['Occurance', 'MarginalProbability']

# Merge the two DataFrames to match Occurrence and calculate the conditional probability
result = pd.merge(joint_prob, marginal_prob_occurrence, on='Occurance')
result['ConditionalProbability'] = result['JointProbability'] / result['MarginalProbability']

print("Conditional Probability of Char given Occurrence:")
print(result)



print(20 * '-' + 'End Q1' + 20 * '-')

# =================================================================
# Class_Ex2:
# Use the following dataframe as the sample data.
# Find the conditional probability occurrence of thw word given a sentiment.
# ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q2' + 20 * '-')
import pandas as pd

# Create the DataFrame
import pandas as pd

# Create the DataFrame
df1 = pd.DataFrame({'Word': ['Good', 'Bad', 'Awesome', 'Beautiful', 'Terrible', 'Horrible'],
                    'Occurrence': ['One', 'Two', 'One', 'Three', 'One', 'Two'],
                    'sentiment': ['P', 'N', 'P', 'P', 'N', 'N']})

# Calculate the joint probability of Word and sentiment and reset the index
joint_prob = df1.groupby(['Word', 'sentiment']).size().reset_index(name='JointProbability')

# Calculate the marginal probability of sentiment and reset the index
marginal_prob_sentiment = df1['sentiment'].value_counts().reset_index()
marginal_prob_sentiment.columns = ['sentiment', 'MarginalProbability']

# Merge the two DataFrames to match sentiment and calculate the conditional probability
result = pd.merge(joint_prob, marginal_prob_sentiment, on='sentiment')
result['ConditionalProbability'] = result['JointProbability'] / result['MarginalProbability']

print("Conditional Probability of Word given Sentiment:")
print(result)

#
# print(20 * '-' + 'End Q2' + 20 * '-')
# # =================================================================
# # Class_Ex3:
# # Read the data.csv file.
# # Answer the following question
# # 1- In this dataset we have a lot of responses in text and each response has a label.
# # 2- Our goal is to correctly model the texts into its label.
# # Hint: you need to read the text responses and perform preprocessing on it.
# # such as normalization, legitimation, cleaning, stopwords removal and POS tagging.
# # then use any methods you learned in the lecture to convert each response into meaningful numbers.
# # 3- Apply Naive bayes and look at appropriate evaluation metric.
# # 4- Explain your results very carefully.
# # ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q3' + 20 * '-')
#
# print(20 * '-' + 'End Q3' + 20 * '-')
# # =================================================================
# # Class_Ex4:
# # Use Naive bayes classifier for this problem,
# # Write a text classification pipeline to classify movie reviews as either positive or negative.
# # Find a good set of parameters using grid search. hint: grid search on n gram
# # Evaluate the performance on a held out test set.
# # hint1: use nltk movie reviews dataset
# # from nltk.corpus import movie_reviews
#
# # ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q4' + 20 * '-')
#
# print(20 * '-' + 'End Q4' + 20 * '-')
# # =================================================================
# # Class_Ex5:
# # Calculate accuracy percentage between two lists
# # calculate a confusion matrix
# # Write your own code - No packages
# # ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q5' + 20 * '-')
#
# print(20 * '-' + 'End Q5' + 20 * '-')
# # =================================================================
# # Class_Ex6:
# # Read the data.csv file.
# # Answer the following question
# # 1- In this dataset we have a lot of responses in text and each response has a label.
# # 2- Our goal is to correctly model the texts into its label.
# # Hint: you need to read the text responses and perform preprocessing on it.
# # such as normalization, legitimation, cleaning, stopwords removal and POS tagging.
# # then use any methods you learned in the lecture to convert each response into meaningful numbers.
# # 3- Apply Logistic Regression  and look at appropriate evaluation metric.
# # 4- Apply LSA method and compare results.
# # 5- Explain your results very carefully.
#
# # ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q6' + 20 * '-')
#
# print(20 * '-' + 'End Q6' + 20 * '-')
#
# # =================================================================
# # Class_Ex7:
# # Use logistic regression classifier for this problem,
# # Write a text classification pipeline to classify movie reviews as either positive or negative.
# # Find a good set of parameters using grid search. hint: grid search on n-gram
# # Evaluate the performance on a held out test set.
# # hint1: use nltk movie reviews dataset
# # from nltk.corpus import movie_reviews
# # ----------------------------------------------------------------
# print(20 * '-' + 'Begin Q7' + 20 * '-')
#
# print(20 * '-' + 'End Q7' + 20 * '-')
