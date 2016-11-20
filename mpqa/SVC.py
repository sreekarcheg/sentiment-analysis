import pandas as pd
import numpy as np
import mpqa
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem

def evaluate_cross_validation(clf, X, y, K):
    # create a k-fold croos validation iterator
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # by default the score used is the one returned by score 
    # method of the estimator (accuracy)
    scores = cross_val_score(clf, X, y, cv=cv)
    print scores
    print ("Mean score: {0:.3f} (+/-{1:.3f})").format(
            np.mean(scores), sem(scores))

def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
	global metrics
    clf.fit(X_train, y_train)
    print "Accuracy on training set:"
    print clf.score(X_train, y_train)
    print "Accuracy on testing set:"
    print clf.score(X_test, y_test)
    
    y_pred = clf.predict(X_test)
    
    print "Classification Report:"
    print metrics.classification_report(y_test, y_pred)
    print "Confusion Matrix:"
    print metrics.confusion_matrix(y_test, y_pred)


data = pd.read_pickle('data.pkl')
data = data.to_dense()
labels = pd.read_pickle('labels.pkl')
X = data.values
y = labels['c_pol'].map(lambda k: 0 if k < 0 else 1).values

print 'X.shape, y.shape'
print X.shape, y.shape

svc_1 = SVC(kernel='linear')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)



evaluate_cross_validation(svc_1, X_train, y_train, 5)
train_and_evaluate(svc_1, X_train, X_test, y_train, y_test)

