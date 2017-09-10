from surprise import KNNBasic
from surprise import Dataset
from surprise import Reader
import os
from surprise import NMF

#------------------------load data from a file
file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)



from surprise import SVD
from surprise import evaluate, print_perf
import os


#########---------------SVD
print('')
print('---------------SVD result-------------')
data.split(n_folds=3)
algo = SVD()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)


#########---------------PMF
print('')
print('---------------PMF result--------------')
data.split(n_folds=3)
algo = SVD(biased=False)
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)

##########--------------NMF
print('')
print('----------------NMF result--------------')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'user_based':True})
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)


##########--------------User Based Collaborative Filtering algorithm
print('')
print('User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'user_based': False })
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)




##########--------------Item Based Collaborative Filtering algorithm
print('')
print('Item Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'user_based': False})
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)


##########--------MSD------User Based Collaborative Filtering algorithm
print('')
print('MSD----User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'name':'MSD','user_based': True})
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)


##########--------cosin------User Based Collaborative Filtering algorithm
print('')
print('cosin----User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'name':'cosine','user_based': True})
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)

##########--------person------User Based Collaborative Filtering algorithm
print('')
print('Person sim----User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(sim_options = {'name':'pearson','user_based': True})
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)


##########--------MSD------User Based Collaborative Filtering algorithm
print('')
print('10--Neighboors--User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':True })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------cosin------User Based Collaborative Filtering algorithm
print('')
print('10---Neighboors---Item Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':False })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------MSD------User Based Collaborative Filtering algorithm
print('')
print('15--Neighboors--User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':True })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------cosin------User Based Collaborative Filtering algorithm
print('')
print('15---Neighboors---Item Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':False })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------MSD------User Based Collaborative Filtering algorithm
print('')
print('25--Neighboors--User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':True })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------cosin------User Based Collaborative Filtering algorithm
print('')
print('25---Neighboors---Item Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':False })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)



##########--------MSD------User Based Collaborative Filtering algorithm
print('')
print('30--Neighboors--User Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':True })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)


##########--------cosin------User Based Collaborative Filtering algorithm
print('')
print('30---Neighboors---Item Based Collaborative Filtering algorithm result')
data.split(n_folds=3)
algo = KNNBasic(k=10, sim_options = {'name':'MSD', 'user_based':False })
perf = evaluate(algo, data, measures=['RMSE'])
print_perf(perf)




