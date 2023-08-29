import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
x1=np.array([100,150,200,250]).reshape(-1,1)
y=np.array([140,200,250,300])
z1=np.array([10,20,30,10]).reshape(-1,1)
z2=np.array([15,25,35,55]).reshape(-1,1)
x2=np.column_stack((x1,z1))
x=np.column_stack((x2,z2))
# plt.scatter(x,y)
# plt.show()
# plt.plot(x,y)
# plt.show()
model=LinearRegression()
model.fit(x,y)
xp=model.predict(x)
mse=mean_squared_error(y,xp)
print(mse)
plt.plot(x,xp)
plt.show()
k=model.predict([[50,100,105]])
print(k)
print('Slope',model.coef_,'\nIntercept',model.intercept_)
