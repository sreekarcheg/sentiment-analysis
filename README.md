# IITH-CS6270 course project

## Description

Implementation of "Recognising contextual polarity in Phrase Level Sentiment Analysis", Wilson et al.  

## Setting up
Download and place dataset.pqa.2.0 and place it in this directory.  

To extract the features:  
`python mpqa.py mkfeat --mpqa <dataset_folder_name> --subclues subjclues.tff --intensifiers intensifiers.tff --doclist doclist.combinedUnique --output feats.pkl`  
  
To extract labels:  
`python mpqa/mpqa.py mkdata --featdf feats.pkl --data data1.pkl --labels labels1.pkl --maps map.json`  
  
To trains models and generate results:  
`python run.py`  
  
##Results: 
  
**STATS of SVC:---------------- * *
Accuracy on training set:  
0.896449704142  
  
Accuracy on testing set:  
0.886094674556  
  
Classification Report:  

             precision    recall  f1-score   support

         -1       0.00      0.00      0.00        29
          0       0.89      1.00      0.94      1797
          1       0.00      0.00      0.00       202
  
avg / total       0.79      0.89      0.83      2028    
  
Confusion Matrix:  
[[   0   29    0]  
 [   0 1797    0]  
 [   0  202    0]]  

  
**STATS of Adaboost------------  **
Accuracy on training set:  
0.861604207758  
  
Accuracy on testing set:  
0.848126232742  
  
Classification Report:  
             precision    recall  f1-score   support

         -1       0.00      0.00      0.00        29
          0       0.89      0.95      0.92      1797
          1       0.11      0.05      0.07       202

avg / total       0.80      0.85      0.82      2028  
  
Confusion Matrix:  
[[   0   28    1]  
 [   3 1709   85]  
 [   0  191   11]]  

  
**STATS of Random Classifier---  **
Accuracy on training set:  
0.977317554241  
  
Accuracy on testing set:  
0.883629191321  
  
Classification Report:  
             precision    recall  f1-score   support

         -1       0.00      0.00      0.00        29
          0       0.89      1.00      0.94      1797
          1       0.17      0.00      0.01       202

avg / total       0.80      0.88      0.83      2028  
  
Confusion Matrix:  
[[   0   29    0]  
 [   1 1791    5]  
 [   0  201    1]]  


**Neural network  **
Epoch 1/10  
6084/6084 [==============================] - 1s - loss: 0.6291 - acc: 0.8891        
Epoch 2/10  
6084/6084 [==============================] - 1s - loss: 0.3973 - acc: 0.8964       
Epoch 3/10  
6084/6084 [==============================] - 1s - loss: 0.3719 - acc: 0.8964         
Epoch 4/10  
6084/6084 [==============================] - 1s - loss: 0.3612 - acc: 0.8964       
Epoch 5/10  
6084/6084 [==============================] - 1s - loss: 0.3551 - acc: 0.8964       
Epoch 6/10  
6084/6084 [==============================] - 1s - loss: 0.3511 - acc: 0.8964        
Epoch 7/10  
6084/6084 [==============================] - 1s - loss: 0.3479 - acc: 0.8964       
Epoch 8/10  
6084/6084 [==============================] - 1s - loss: 0.3453 - acc: 0.8964       
Epoch 9/10  
6084/6084 [==============================] - 1s - loss: 0.3429 - acc: 0.8964        
Epoch 10/10  
6084/6084 [==============================] - 1s - loss: 0.3408 - acc: 0.8964     

**STATS of NEURAL NETWORK:**

             precision    recall  f1-score   support

          0       0.00      0.00      0.00         0
          1       0.00      0.00      0.00         0
          2       1.00      0.89      0.94      2028

avg / total       1.00      0.89      0.94      2028

## Code   
The individual bunch of features can be seen above. All of these features have been put together in mpqa.py.     
The dataset parser of MPQA has been taken from @ms8r  

## REQUIREMENTS
numpy  
scikit-learn  
pandas    
spacy  

## Project contributors:
* Akshita Mittel
* Keyur Joshi
* Sreekar Reddy
* Surya Teja
