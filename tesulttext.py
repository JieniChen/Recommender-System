Python 3.6.1 |Anaconda 4.4.0 (x86_64)| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: /Users/chenjenny/Documents/Course/CS6001-Applied Spatial and Temporal Data Analysis)/HW4/RecommenderSysetm.py 

---------------SVD result-------------
Evaluating RMSE, MAE of algorithm SVD.

------------
Fold 1
RMSE: 0.9440
MAE:  0.7468
------------
Fold 2
RMSE: 0.9483
MAE:  0.7464
------------
Fold 3
RMSE: 0.9443
MAE:  0.7446
------------
------------
Mean RMSE: 0.9455
Mean MAE : 0.7460
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9440  0.9483  0.9443  0.9455  
MAE     0.7468  0.7464  0.7446  0.7460  

---------------PMF result--------------
Evaluating RMSE, MAE of algorithm SVD.

------------
Fold 1
RMSE: 0.9710
MAE:  0.7646
------------
Fold 2
RMSE: 0.9635
MAE:  0.7582
------------
Fold 3
RMSE: 0.9665
MAE:  0.7618
------------
------------
Mean RMSE: 0.9670
Mean MAE : 0.7615
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9710  0.9635  0.9665  0.9670  
MAE     0.7646  0.7582  0.7618  0.7615  

----------------NMF result--------------
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9849
MAE:  0.7796
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9918
MAE:  0.7819
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9885
MAE:  0.7821
------------
------------
Mean RMSE: 0.9884
Mean MAE : 0.7812
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9849  0.9918  0.9885  0.9884  
MAE     0.7796  0.7819  0.7821  0.7812  

User Based Collaborative Filtering algorithm result
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9842
MAE:  0.7799
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9891
MAE:  0.7822
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9859
MAE:  0.7824
------------
------------
Mean RMSE: 0.9864
Mean MAE : 0.7815
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9842  0.9891  0.9859  0.9864  
MAE     0.7799  0.7822  0.7824  0.7815  

Item Based Collaborative Filtering algorithm result
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9822
MAE:  0.7797
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9848
MAE:  0.7773
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9932
MAE:  0.7878
------------
------------
Mean RMSE: 0.9867
Mean MAE : 0.7816
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9822  0.9848  0.9932  0.9867  
MAE     0.7797  0.7773  0.7878  0.7816  

MSD----User Based Collaborative Filtering algorithm result
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9904
MAE:  0.7849
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9934
MAE:  0.7829
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9803
MAE:  0.7749
------------
------------
Mean RMSE: 0.9881
Mean MAE : 0.7809
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9904  0.9934  0.9803  0.9881  
MAE     0.7849  0.7829  0.7749  0.7809  

cosin----User Based Collaborative Filtering algorithm result
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the cosine similarity matrix...
Done computing similarity matrix.
RMSE: 1.0217
MAE:  0.8090
------------
Fold 2
Computing the cosine similarity matrix...
Done computing similarity matrix.
RMSE: 1.0169
MAE:  0.8045
------------
Fold 3
Computing the cosine similarity matrix...
Done computing similarity matrix.
RMSE: 1.0238
MAE:  0.8092
------------
------------
Mean RMSE: 1.0208
Mean MAE : 0.8076
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0217  1.0169  1.0238  1.0208  
MAE     0.8090  0.8045  0.8092  0.8076  

Person sim----User Based Collaborative Filtering algorithm result
Evaluating RMSE, MAE of algorithm KNNBasic.

------------
Fold 1
Computing the pearson similarity matrix...
Done computing similarity matrix.
RMSE: 1.0273
MAE:  0.8152
------------
Fold 2
Computing the pearson similarity matrix...
Done computing similarity matrix.
RMSE: 1.0190
MAE:  0.8094
------------
Fold 3
Computing the pearson similarity matrix...
Done computing similarity matrix.
RMSE: 1.0183
MAE:  0.8085
------------
------------
Mean RMSE: 1.0215
Mean MAE : 0.8110
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0273  1.0190  1.0183  1.0215  
MAE     0.8152  0.8094  0.8085  0.8110  

10--Neighboors--User Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0032
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9968
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0018
------------
------------
Mean RMSE: 1.0006
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0032  0.9968  1.0018  1.0006  

10---Neighboors---Item Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0233
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0268
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0245
------------
------------
Mean RMSE: 1.0249
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0233  1.0268  1.0245  1.0249  

15--Neighboors--User Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0056
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0008
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9976
------------
------------
Mean RMSE: 1.0013
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0056  1.0008  0.9976  1.0013  

15---Neighboors---Item Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0235
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0192
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0266
------------
------------
Mean RMSE: 1.0231
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0235  1.0192  1.0266  1.0231  

25--Neighboors--User Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9995
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0034
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9978
------------
------------
Mean RMSE: 1.0002
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    0.9995  1.0034  0.9978  1.0002  

25---Neighboors---Item Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0281
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0224
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0164
------------
------------
Mean RMSE: 1.0223
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0281  1.0224  1.0164  1.0223  

30--Neighboors--User Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0054
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0026
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 0.9999
------------
------------
Mean RMSE: 1.0026
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0054  1.0026  0.9999  1.0026  

30---Neighboors---Item Based Collaborative Filtering algorithm result
Evaluating RMSE of algorithm KNNBasic.

------------
Fold 1
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0241
------------
Fold 2
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0255
------------
Fold 3
Computing the msd similarity matrix...
Done computing similarity matrix.
RMSE: 1.0200
------------
------------
Mean RMSE: 1.0232
------------
------------
        Fold 1  Fold 2  Fold 3  Mean    
RMSE    1.0241  1.0255  1.0200  1.0232  
>>> 
