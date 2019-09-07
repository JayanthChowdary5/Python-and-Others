import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns  # Seaborn is built upon matplotlib and makes the plots more artistic
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Reading Data
housing_data = pd.read_csv(r'PATH')

# As a rule of thumb in sklearn interfaces, X should be a 2D array and Y should be a 1D array
# .reshape(len(a), 1) or .reshape(-1, 1) turns 1D array to a 2D array by turning
#  each of its elements into an array of its own
space = np.array(housing_data['sqft_living']).reshape(-1, 1)
prices = np.array(housing_data['price'])

# Splitting data into train and test data sets
space_train, space_test, prices_train, prices_test = train_test_split(space, prices, test_size=0.25)

# Training the data
regressor = LinearRegression()
regressor.fit(space_train, prices_train)

# Now that the regressor learnt training data & formed a model, we will see how accurately it can predict the test data
prices_pred = regressor.predict(space_test)

sns.set()  # Overwriting default Matplotlib settings with Seaborn for plots to look more elegant

# Regression line of training data set
plt.scatter(space_train, prices_train, color='blue')
plt.plot(space_train, regressor.predict(space_train), color='red')
plt.title('Regression Analysis - Training Data')
plt.xlabel('Living Space')
plt.ylabel('Price')
plt.show()

# Visualizing Test Data set
plt.scatter(space_test, prices_test, color='blue')
plt.plot(space_train, regressor.predict(space_train), color='orange') # We plot training data here too because our model 
# is trained with that data
plt.title('Regression Analysis - Test Data')
plt.xlabel('Living Space')
plt.ylabel('Price')
plt.show()

