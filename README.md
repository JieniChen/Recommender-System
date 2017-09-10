# Recommender-System
This code use the data of restaurant-rating data set
In ths code, we applied mutlipe algorithms to complete the preditive classification for the recommender systm
Also we compared each algorithm with RMSE and MAE score 

## RMSD
The root-mean-square deviation (RMSD) or root-mean-square error (RMSE) is a frequently used measure of the differences between values (sample and population values) predicted by a model or an estimator and the values actually observed. The RMSD represents the sample standard deviation of the differences between predicted values and observed values. These individual differences are called residuals when the calculations are performed over the data sample that was used for estimation, and are called prediction errors when computed out-of-sample. The RMSD serves to aggregate the magnitudes of the errors in predictions for various times into a single measure of predictive power. RMSD is a measure of accuracy, to compare forecasting errors of different models for a particular data and not between datasets, as it is scale-dependent.

## MAE

In statistics, mean absolute error (MAE) is a measure of difference between two continuous variables. Assume X and Y are variables of paired observations that express the same phenomenon. Examples of Y versus X include comparisons of predicted versus observed, subsequent time versus initial time, and one technique of measurement versus an alternative technique of measurement. Consider a scatter plot of n points, where point i has coordinates (xi, yi). Mean Absolute Error (MAE) is the average vertical distance between each point and the Y=X line, which is also known as the One-to-One line. MAE is also the average horizontal distance between each point and the Y=X line.

Where a prediction model is to be fitted using a selected performance measure, in the sense that the least squares approach is related to the mean squared error, the equivalent for mean absolute error is least absolute deviations.

# SVD
SVD algorithm: the singular value decomposition (SVD) is a factorization of a real or complex matrix. It is the generalization of the eigen-decomposition of a positive semidefinite normal matrix (for example, a symmetric matrix with positive eigenvalues) to any m × n matrix via an extension of polar decomposition. It has many useful applications in signal processing and statistics.
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-1.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/chart1-2.png)


# PMF
PMF algorithm: One of the most popular approaches to collaborative filtering is based on low-dimensional factor models. The idea behind such models is that attitudes or preferences of a user are determined by a small number of unobserved factors. In a linear factor model, a user’s preferences are modeled by linearly combining item factor vectors using user-specific coefficients. For example, for N users and M movies, the N × M preference matrix R is given by the product of an N × D user coefficient matrix U T and a D × M factor matrix V . Training such a model amounts to finding the best rank-D approximation to the observed N × M target matrix R under the given loss function.

The Probabilistic Matrix Factorization (PMF) model that models the user preference matrix as a product of two lower-rank user and movie matrices. The PMF algorithm’s code result is showing as below

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-3.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-4.png)

# NMF
Non-negative matrix factorization (NMF) has previously been shown to be a useful decomposition for multivariate data. Two different multi plicative algorithms for NMF are analyzed. They differ only slightly in the multiplicative factor used in the update rules. One algorithm can be shown to minimize the conventional least squares error while the other minimizes the generalized Kullback-Leibler divergence. The monotonic convergence of both algorithms can be proven using an auxiliary function analogous to that used for proving convergence of the Expectation- Maximization algorithm. The algorithms can also be interpreted as diagonally rescaled gradient descent, where the rescaling factor is optimally chosen to ensure convergence. The NMF algorithm result is showing as below:

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-5.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-6.png)


# Collaborative filtering (CF)
Collaborative filtering (CF) is a technique used by recommender systems. Collaborative filtering has two senses, a narrow one and a more general one.

In the newer, narrower sense, collaborative filtering is a method of making automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating). The underlying assumption of the collaborative filtering approach is that if a person A has the same opinion as a person B on an issue, A is more likely to have B's opinion on a different issue than that of a randomly chosen person. For example, a collaborative filtering recommendation system for television tastes could make predictions about which television show a user should like given a partial list of that user's tastes (likes or dislikes).

In the more general sense, collaborative filtering is the process of filtering for information or patterns using techniques involving collaboration among multiple agents, viewpoints, data sources, etc. Applications of collaborative filtering typically involve very large data sets. Collaborative filtering methods have been applied to many kinds of data including: sensing and monitoring data, such as in mineral exploration, environmental sensing over large areas or multiple sensors; financial data, such as financial service institutions that integrate many financial sources; or in electronic commerce and web applications where the focus is on user data, etc. The remainder of this discussion focuses on collaborative filtering for user data, although some of the methods and approaches may apply to the other major applications as well.

The result for User based Collaborative Filtering algorithm’s result is showing as below

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-7.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-8.png)

# Item based Collaborative Filtering 
Item based Collaborative Filtering algorithm is the same logic as the user based collaborative filtering algorithm, the only different is that they are relay on the different categories. The result of Item based Collaborative Filtering algorithm is showing as below: 


![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-9.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-10.png)

# Comparision of all the algorithms used above

## fold-2
Compare the performances of User-based collaborative filtering, item-based collaborative filtering, SVD, PMF, NMF on fold-2 with respect to RMSE and MAE. Please make sure you test the five algorithms on the same fold-2 so the results are comparable.

The below picture shows the running result for User-based collaborative filtering, item-based collaborative filtering, SVD, PMF, NMF on fold-2 with RMSE and MAE:

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-11.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-12.png)


We can see the comparison graph as below:

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-13.png)

We can see the SVD is most likely the algorithm to achieve the lowest RMSE and MAE value and the NMF, User-based CF and item-Based CF are achieve high RMSE and MAE value. 

## fold-3
Compare the performances of User-based collaborative filtering, item-based collaborative filtering, SVD, PMF, NMF on fold-3 with respect to RMSE and MAE:

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-14.png)


We can see the PMF is most likely the algorithm to achieve the lowest RMSE and MAE value and the NMF, User-based CF and item-Based CF are achieve high RMSE and MAE value. 

# Mean Value Comparision
Compare the average (mean) performances of User-based collaborative filtering, item-based collaborative filtering, SVD, PMF, NMF with respect to RMSE and MAE. 

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-15.png)

We can see the PMF is most likely the algorithm to achieve the lowest RMSE and MAE value and the NMF, User-based CF and item-Based CF are achieve high RMSE and MAE value. 


Low-rank approximations based on minimizing the sum-squared distance can be found using Singular Value Decomposition (SVD). SVD finds the matrix Rˆ = U T V of the given rank which minimizes the sum-squared distance to the target matrix R. Since most real-world datasets are sparse, most entries in R will be missing. In those cases, the sum-squared distance is computed only for the observed entries of the target matrix R, this seemingly minor modification results in a difficult non-convex optimization problem which cannot be solved using standard SVD implementations.

# Compare cosine, MSD, Person Similarities
Examine how the cosine, MSD (Mean Squared Difference), and Pearson similarities impact the performances of User based Collaborative Filtering and Item based Collaborative Filtering.
Here is the result of the code:

![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-16.png)

# How the number of neighbors impacts the performances
Examine how the number of neighbors impacts the performances of User based Collaborative Filtering or Item based Collaborative Filtering
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-17.png)
![alt text](https://github.com/JieniChen/Recommender-System/blob/master/result/Picture1-18.png)




# Reference
https://en.wikipedia.org/wiki/Root-mean-square_deviation
https://en.wikipedia.org/wiki/Mean_absolute_error
