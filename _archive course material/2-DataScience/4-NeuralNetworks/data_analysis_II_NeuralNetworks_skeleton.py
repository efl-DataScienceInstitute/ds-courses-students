import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

#%%
# (1) ---- Import data ----
# Load data
data_raw = pd.read_csv('bank_marketing_balanced.csv')  # Source: https://archive.ics.uci.edu/ml/datasets/bank+marketing#
# Read info in txt file!

#%% get first impression of the data
print(data_raw.head(5))  # optional: examine frame using variable explorer

#%% get detailed impression of the data
for c in data_raw.columns:
    print(c)
    print(data_raw.loc[:, c].unique())  # Show unique values per column

#%%
# (2) ---- Data pre-processing ----
data_pp = data_raw.copy()  # make a copy
# Transform categorical to numeric features
categoricals = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                'contact', 'month', 'day_of_week', 'poutcome', 'y']
df_dummies = pd.get_dummies(
    data_pp.loc[:, categoricals], drop_first=True, dtype=int,
    )
print(df_dummies.info())

#%% Drop categorical columns
print(data_pp)
data_pp = data_pp.drop(categoricals, axis=1)

#%% Insert dummies representing the categoricals
data_pp = pd.concat([data_pp, df_dummies], axis=1)
print(data_pp)

#%% Rename y_yes back to y
data_pp.rename(columns={'y_yes': 'y'}, inplace=True)

#%% Show output
print(data_raw.tail(5))
print(data_pp.tail(5))

#%% What about class imbalance?
print(data_pp['y'].value_counts())  # show absolute number of observations per value of y
print(sum(data_pp['y'] == 1) / data_pp.shape[0])  # share of observations where y=1


#%% Split in x and y
x = data_pp.drop('y', axis=1)
y = data_pp.loc[:, 'y']

#%% Split in train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

#%% Split in train and valid
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.15)
print(x_train.shape, y_train.shape)
print(x_val.shape, y_val.shape)
# Hint: to get precise split of 70-15-15 (train-test-valid), do test_size=0.15 and then test_size=0.15/0.85

#%% Rescale features with minmax scaling
# Neural networks perform pretty well on features ranging between 0 and 1
minmax = MinMaxScaler()
print(x_train)  # before scaling
x_train = minmax.fit_transform(x_train)
print(x_train)  # after scaling

#%% Transform valid. & test data with min & max parameter of training data
x_val = minmax.transform(x_val)
x_test = minmax.transform(x_test)


#%%
# (3) ---- Build, train and evaluate ANN ----
# Construct the model (define layers, their units and activation functions)
no_inputs = x_train.shape[1]

#%%
# Define the (hyper)parameters of the model and its training 
number_epochs = 5
batch_size = 32

mynn = MLPClassifier(
    hidden_layer_sizes=(5, ), activation='relu', batch_size=batch_size
)

#%% Train the model to optimize all weights

# simple training loop lacking validation:
# train_results_sl = mynn.fit(x_train, y_train)

# detailed training loop, including validation
for epoch in range(1, number_epochs + 1):
    train_loss = []  # list to collect train loss for each batch
    for b_idx in range(batch_size, len(y_train), batch_size):
        idx_start = b_idx - batch_size
        idx_end = b_idx
        x_batch = x_train[idx_start:idx_end]
        y_batch = y_train[idx_start:idx_end]
        mynn.partial_fit(x_batch, y_batch, classes=[0, 1])
        train_loss.append(mynn.loss_)

    print(f'Loss after {epoch} epochs: {np.mean(train_loss)}')
    print(f'Validation accuracy after {epoch} epochs: {mynn.score(x_val, y_val)}')

#%%
# Evaluate the performance of the model on (unseen) test data
test_results = mynn.score(x_test, y_test)
print(f'Final test accuracy {np.round(test_results *100, 2)}%!')

#%% Delete model and experiment with different setups
del mynn

#%% TODO: HYPERPARAMETER OPTIMIZATION

#%% TODO 1: 
# Experiment with different number of units and mini batch sizes
mini_batch_sizes = [1, 32, 128]
no_units = [5, 50, 500]
results = {}

#%% TODO 2:
# Try to achieve the highest accuracy at the test set in the class room!
# Don't forget to store the results of the individual runs!
