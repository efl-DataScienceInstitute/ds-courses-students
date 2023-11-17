# -*- coding: utf-8 -*-

#Importing required packages.
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree
from sklearn.metrics import mean_squared_error, r2_score, classification_report,accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", "is_categorical_dtype")
warnings.filterwarnings("ignore", "use_inf_as_na")

#%%##########################
##### Data Import ######
############################
# Import the data
wine = pd.read_csv('')


#%%##########################
##### Pre-Processing ######
###########################
#Let's check how the data is distributed
#Information about the data columns






#%%############################
#####Data Visualization######
#############################
# Use @code: for describing stats.

#%% Pairplot for an overview.






#%%Create a box plot consisting of quality and alcohol acid
# without outliers. 
# Add title, names to the axes and save the plot as pdf.
plt.figure()
sns.boxplot(x=, y=, data=)
plt.ylabel('Alcohol')
plt.xlabel('Quality')
plt.title('Boxplot Quality Alcohol')
plt.savefig('BoxPlotForWine.png')  # alternatively: BoxPlotForWine.pdf
plt.show()


#%% Create a Distplot for the fixed acidity in the data set. 
# What does the data distribution tell us? 
plt.figure()
sns.displot(a=)
plt.xlabel('Fixed Acidity')
plt.ylabel('Count')
plt.savefig('Distplot.png')  # alternatively: Distplot.pdf
plt.show()


#%% Create a heatmap with the correlation. Calculate the correlation with 
# numpy and use the mask option in the heatmap. Add also axis names and titles.
# For what is this plot useful? What insight?  
corr = wine.corr()
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
plt.figure()
sns.heatmap(corr, mask=mask, annot=True, cbar=True, fmt='.3f', cmap="RdBu_r")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('CorrelationHeatmap.pdf')
plt.show()
# Note: There is a bug in seaborn version 0.12.2 where annotations 
# (i.e., corr. values) are not plotted. Please use version 0.11 or 0.13!




#%%#########################################
#####Data Modeling: Data Preparation######
##########################################

# Now it is time to prepare our data for data-modeling
# We want to accomplish two tasks with our machine learning models: 
# 1. A prediction for how much alcohol will be in a wine of certain attributes.
# 2. We want to classify if a wine is good or bad for a given set of wine attributes.

# Let's have a look at the values for the first prediction:
alcohol = wine['alcohol'].value_counts()
print(alcohol)
# This data looks perfect for our regression task.

# Now for the second task: Let's see what values the quality column has.
quality = wine['quality'].value_counts()
print(quality)

#%% It appears that we only have values between 3 and 8, while 8 being the criterion
# for really good wine, and 3 being a really bad wine.

# Since we only want to distinguish between good and bad wines, we need to make
# bins of values to assign these values to either good or bad category.

# We make a binary classificaion for the quality variable.
# Doing this, we divide the set of quality measures as good as possible
# We do this with the important cut function.
# apply the cut function to the respective subset of wine to fill the
# wine['quality'] column with the new values.

bins = (0, 6.5, 8)
group_names = ['bad', 'good']
wine['quality_binary'] = pd.cut(...)


# Now take a look at the dataframe column quality. Looks better!

# Our model only needs 0 and 1 to classify whether the wine is good 
# or not. Thus, we must assign 0 for bad and 1 for good quality.
# We do this with the LabelEncoder.

#%%Now lets assign a label to our quality variable
label_quality = LabelEncoder()

#Bad becomes 0 and good becomes 1 
wine['quality_binary'] = label_quality.fit_transform(wine['quality_binary'])

# Count the values of the quality column of wine.
print(wine['quality_binary'].value_counts())

#%% Make a seaborn countplot for the values of the quality column of wine.
plt.figure()
sns.countplot(...)
plt.tight_layout()
plt.savefig('countplot_quality_binary.pdf')
plt.show()

#%%############################################
####Preparing the data for the first task####
#############################################

# Now seperate the dataset as response variable/ target variable.
# We do this by using the drop function for subset of independent variables
# and only adding the alcohol column to subset for the dependent/target variable.
x = wine.drop('alcohol', axis=1)
y = wine['alcohol']

#Train and Test splitting of data 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Explain the Train-Test split. Why did we split by the test_size?
# Please explain why we need a train and a test set.

#%% Applying Standard scaling:
# Standardization of a dataset is a common requirement for many 
# machine learning estimators: they might behave badly if the 
# individual features do not more or less look like standard 
# normally distributed data (e.g. Gaussian with 0 mean and unit variance).
# see: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


# Now you have all the data you need to train the model.
x_train # training sample (independent variables)
y_train # training sample (dependent variable)
x_test # testing sample (independent variables)
y_test # testing sample (dependent variable)

#%%#########################################
#####Data Modeling: Model Creation #######
##########################################

###########################
######Regression Tree######
###########################

# Please configure the regression tree as learned in the lecture.
# You should also describe, why you set certain parameters such as
# max_depth and what the effect of these parameters was.

# Configure model
regr = ...

#%% Fit regression model
regr.fit(..., ...)

#%% Predict
y_pred = ...

#%% evaluation
mse = mean_squared_error(..., ...)
r2 = r2_score(..., ...)
print('DT: mse = '+ str(mse) + ' r2 = '+ str(r2))
#%% plotting a tree with text

sTree = ...

#%% plot tree and save it to pdf
plt.figure(figsize=(16,9))
plot_tree(..., filled=True, feature_names=list(x.columns), fontsize=9)
plt.savefig('tree.pdf')
plt.show()

# What was the result of your Regression Tree?
# Can it efficiently predict the alcohol of the wines?
# If not, what could be the problem?



#%%######################
#####RandomForest######
#######################

##############################################
####Preparing the data for the second task####
##############################################

## Now to our most interesting prediction part: we want to know if we can
## classify good and bad wine. Thus, our target variable is the quality.

# We seperate the dataset as response variable/ target variable.
# We do this by using the drop function for subset of independent variables
# and only adding the quality column to subset for the dependent/target variable.
x = wine.drop(['quality_binary', 'quality'], axis=1)
y = wine['quality_binary']


#Train and Test splitting of data 
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)

# Explain the Train-Test split. Why did we split by the test_size?
# Please explain why we need a train and a test set.

#%% Applying Standard scaling:
# Standardization of a dataset is a common requirement for many 
# machine learning estimators: they might behave badly if the 
# individual features do not more or less look like standard 
# normally distributed data (e.g. Gaussian with 0 mean and unit variance).
# see: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
sc = StandardScaler()

x_train = sc.fit_transform(...)
x_test = sc.transform(...)


#%% Now we are able to make our classifier.

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200, random_state=1337)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)

print ("Train Accuracy: ", accuracy_score(y_train, rfc.predict(x_train)))
print ("Test Accuracy: ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['bad','good']))
print(rfc.score(x_test,y_test))

# What was the result of your Random Forest Classifier?
# Could it efficiently predict the quality of the wines?
# If not, what could be the problem?



#%%######################
#####Neural Nets ######
#######################

# Now we try to make a different classifier using a neural net.
# We use the same X and y for classification as before.

# This neural net structure is given. 
# Please fill out the missing Parameters in the model.
# Please explain the reason and the effect of the parameters.


import keras

#%% count number of features
no_features = x.shape[1]

#%% construct model
neural_net = keras.Sequential([
    keras.layers.Dense(units=..., activation=..., input_dim=...),
    keras.layers.Dense(units=..., activation=...)
])

#%% define loss function, optimizer and evaluation metric
neural_net.compile(
    optimizer='Adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

#%% inspect neural network model
print(neural_net.summary())

#%% train the model with defined batch size, epochs, etc.
train_results = neural_net.fit(
    x=..., y=..., validation_split=0.1, batch_size=..., epochs=...)
print(train_results.history)

#%% evaluate the model on test set
test_results = neural_net.evaluate(x=..., y=...)
print(test_results)

# Did the model perform better or worse than the Random Forest Classifier?
# Please provide reasons for the difference in performance:

    



