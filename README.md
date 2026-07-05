# Pi Estimation using Monte Carlo Simulation

This Python project estimates the value of Pi ($\pi$) using the Monte Carlo method, which is a mathematical technique based on random sampling.

## 🧠 How It Works
The program generates random points within a square bounding box $[0,1] \times [0,1]$. It then checks how many of these points fall inside a quarter circle of radius $r = 1$. 

The ratio of points inside the circle to the total number of points allows us to approximate the value of $\pi$ using the formula:
$$\pi \approx 4 \times \frac{\text{Points Inside Circle}}{\text{Total Points}}$$


## 🚀 Features
* Uses Python's built-in `random` module for generating data points.
* Compares the estimated value against the highly accurate `math.pi`.
* Calculates the exact difference/error rate of the simulation.

## 🛠️ Technologies Used
* **Python 3**
* **Math & Random** (Standard Libraries)
