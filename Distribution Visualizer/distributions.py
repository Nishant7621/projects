import numpy as np
from scipy.stats import norm, binom, poisson, uniform

def normal_dist(mean, std):
    x = np.linspace(-10, 10, 100)
    y = norm.pdf(x, mean, std)
    return x, y

def binomial_dist(n, p):
    x = np.arange(0, n)
    y = binom.pmf(x, n, p)
    return x, y

def poisson_dist(lam):
    x = np.arange(0, 20)
    y = poisson.pmf(x, lam)
    return x, y

def uniform_dist(a, b):
    x = np.linspace(a, b, 100)
    y = uniform.pdf(x, a, b-a)
    return x, y