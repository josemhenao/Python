from sklearn.datasets import load_digits
digits = load_digits()
import numpy as np 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)


from sklearn.linear_model import LogisticRegression
# all parameters not specified are set to their defaults

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)

plt.imshow(np.reshape(x_test[0], (8,8)), cmap=plt.cm.gray)
plt.show()
print(logisticRegr.predict(x_test[0].reshape(1,-1)))