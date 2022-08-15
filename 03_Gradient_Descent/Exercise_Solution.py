import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression


def reg_model(df):
    reg = LinearRegression()
    reg.fit(df[['math']], df['cs'])
    print('Using Sklearn Coefficient: {}, Intercept: {}'.format(
        reg.coef_, reg.intercept_))


def gradient_descent(x, y):
    n = len(x)
    m_curr = b_curr = 0
    iterations = 10000000
    learning_rate = 0.0002
    cost_prev = 0
    for i in range(iterations):
        y_predicted = m_curr*x+b_curr
        cost = (1/n)*sum((y-y_predicted)**2)
        pdm = -(2/n)*sum(x*(y-y_predicted))
        pdb = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr-learning_rate*pdm
        b_curr = b_curr-learning_rate*pdb
        print('m: {}, b:{}, cost:{}, iteration: {}'.format(
            m_curr, b_curr, cost, i))
        check = math.isclose(cost, cost_prev, rel_tol=1e-20)
        if check == True:
            break
        cost_prev = cost
    print('Using Gradient Descent Coefficient: {}, Intercept: {}'.format(
        m_curr, b_curr))


if __name__ == '__main__':
    df = pd.read_csv(
        'D:\\Programming\\Python\\py-master\\ML\\3_gradient_descent\\Exercise\\test_scores.csv')
    x = np.array(df['math'])
    y = np.array(df['cs'])
    gradient_descent(x, y)
    reg_model(df)
