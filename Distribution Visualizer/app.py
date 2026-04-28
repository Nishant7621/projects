import streamlit as st
import matplotlib.pyplot as plt
from utils.distributions import *

st.title("📊 Distribution Visualizer")

dist_type = st.selectbox(
    "Choose Distribution",
    ["Normal", "Binomial", "Poisson", "Uniform"]
)

fig, ax = plt.subplots()

if dist_type == "Normal":
    mean = st.slider("Mean", -10.0, 10.0, 0.0)
    std = st.slider("Std Dev", 0.1, 5.0, 1.0)
    x, y = normal_dist(mean, std)
    ax.plot(x, y)

elif dist_type == "Binomial":
    n = st.slider("Trials (n)", 1, 100, 10)
    p = st.slider("Probability (p)", 0.0, 1.0, 0.5)
    x, y = binomial_dist(n, p)
    ax.bar(x, y)

elif dist_type == "Poisson":
    lam = st.slider("Lambda", 1, 20, 5)
    x, y = poisson_dist(lam)
    ax.bar(x, y)

elif dist_type == "Uniform":
    a = st.slider("Start (a)", 0.0, 10.0, 0.0)
    b = st.slider("End (b)", 0.0, 20.0, 10.0)
    x, y = uniform_dist(a, b)
    ax.plot(x, y)

ax.set_title(f"{dist_type} Distribution")
st.pyplot(fig)