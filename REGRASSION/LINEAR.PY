import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
x=np.array([100,150,200,250]).reshape(-1,1)
y=np.array([140,200,250,300])
# plt.scatter(x,y)
# plt.show()
# plt.plot(x,y)
# plt.show()
model=LinearRegression()
model.fit(x,y)
pred=model.predict(x)
mse=mean_squared_error(y,pred)
print(mse)
# plt.plot(x,pred)
# plt.show()
k=model.predict([[50]])
print("\nAT 50",k)
print('slope',model.coef_,'\nintercept',model.intercept_)
