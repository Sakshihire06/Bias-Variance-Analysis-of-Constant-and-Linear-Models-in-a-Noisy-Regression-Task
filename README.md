# Bias-Variance-Analysis-of-Constant-and-Linear-Models-in-a-Noisy-Regression-Task
This assignment analyzes how constant (H₀) and linear (H₁) models learn a noisy quadratic target function using small datasets. You will simulate data, estimate bias and variance, compute expected error, and compare which model class best predicts the underlying function.

******
Question
Suppose data is generated from a target function y = ((x − 2)2 + 4 + noise), where
the noise is defined as N (μ = 0, σ = 0.2) (Here, N is the normal distribution). You
can use the command np.random.normal() in Python for noise. One dataset of size
N = 3 can be obtained from this process by sampling uniformly over x ∈ [−10, 10]:
(x1, y1),(x2, y2) and (x3, y3). This data is to be fit using one of two model classes:
1. H0: The set of all constant functions h(x) = b.
2. H1: The set of all linear functions h(x) = ax + b.

Thus, a training set D has only 3 points, picked independently, and the learning algo-
rithm determines the hypothesis that minimizes the in-sample least squared error, MSE.

This process can be repeated for another three data points, and so on.
For each of the model classes H0 and H1 compute:
1. The hypothesis that best approximates f in the average sense.
2. Its bias and variance components.
3. The expected out-of-sample error.

What do you conclude about whether H0 or H1 is the more appropriate class for predic-
tion? Why?

Instructions
1. Simulate the above experiment in Python and plot appropriate graphs.
2. Submit your code with appropriate extensions (.py or .ipynb).

3. Submit a document with your code to provide a brief explanation of your observa-
tions and results.

4. Your file should be named in the following manner: course-code registration-number name
