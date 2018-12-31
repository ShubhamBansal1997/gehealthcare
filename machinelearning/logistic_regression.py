"""Performs Logistic Regression to find the probability of occurrence of diseases"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score, confusion_matrix, roc_curve, auc, \
    roc_auc_score
from sklearn.preprocessing import StandardScaler
import pickle
import sys
import os
lib_path = os.path.abspath(os.path.join('../', 'lib'))
sys.path.append(lib_path)
from icd9 import ICD9

# Parameters
diag_to_desc = {}
penalty = 'l2'
C = 1.0
max_iter = 100
size = 1391  # Size of each sequence vector
name = 'LR_pen_' + penalty + '_C_' + str(C) + '_iter_' + \
       str(max_iter) + '_size_' + str(size)  # name of ROC Plot


def generate_icd9_lookup():
    """Generate description from ICD9 code"""
    tree = ICD9('../lib/icd9/codes.json')

    for ud in uniq_diag:
        try:
            diag_to_desc[ud] = tree.find(ud[2:]).description
        except:
            if ud[2:] == "008":
                diag_to_desc[ud] = "Intestinal infections due to other organisms"
            elif ud[2:] == "280":
                diag_to_desc[ud] = "Iron deficiency anemias"
            elif ud[2:] == "284":
                diag_to_desc[ud] = "Aplastic anemia and other bone marrow failure syndrome"
            elif ud[2:] == "285":
                diag_to_desc[ud] = "Other and unspecified anemias"
            elif ud[2:] == "286":
                diag_to_desc[ud] = "Coagulation defects"
            elif ud[2:] == "287":
                diag_to_desc[ud] = "Purpura and other hemorrhagic conditions"
            elif ud[2:] == "288":
                diag_to_desc[ud] = "Diseases of white blood cells"
            else:
                diag_to_desc[ud] = "Not Found"


# Read the CSV file and get the inputs and outputs
df = pd.read_csv('../Data/mimic_diagnosis_tfidf/diagnosis_tfidf_5645_pat.csv', header=None)
X = df.iloc[6:, 1:1392].values
Y = {}

# Get the 80 most common diagnosis from the vocab file
with open('../Data/patient_sequences/vocab') as f:
    uniq_diag = np.array(f.read().split('\n')[1].split(' '))

# Get the diagnosis results for each patient
for d, i in zip(uniq_diag, range(1392, len(uniq_diag) + 1392)):
    Y[d] = df[i].values[1:]

# Perform binary classification for each of the 80 common diagnosis
Prediction_acc = {}
# Figure for ROC
plt.figure(figsize=(17, 17), dpi=400)
for c, d in enumerate(uniq_diag):
    y = Y[d].astype(np.float32)
    y = y[5:]  # First 5 patients are used during training and testing
    y = y.reshape(-1, 1)
    # Get the training and te testing vectors
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    print("--------------------Training {} --------------------".format(d))

    # Standardize the data
    sc = StandardScaler()
    sc.fit(X_train)

    # Save the Standardizer
    #joblib.dump(sc, 'Saved_Models/Logistic_Regression_Tfidf/standard.pkl')
    import pickle
    pickle_out=open("/home/ashima/Desktop/DiagnosisPredictor-master/Predictor_Tfidf/Saved_Models/standard.pickle","wb")
    pickle.dump(sc, pickle_out)
    pickle_out.close()

    X_train_sd = sc.transform(X_train)
    X_test_sd = sc.transform(X_test)

    lr = LogisticRegression(penalty='l2', C=C, max_iter=max_iter, n_jobs=-1)
    lr.fit(X_train_sd, Y_train)

    # Save the logistic regression model
    pickle_xyz=open("/home/ashima/Desktop/DiagnosisPredictor-master/Predictor_Tfidf/Saved_Models/lr_model.pickle","wb")
    pickle.dump(sc, pickle_xyz)
    pickle_xyz.close()

    Y_pred_lr = lr.predict(X_test_sd)

    errors = (Y_pred_lr != Y_test).sum()
    acc = accuracy_score(Y_pred_lr, Y_test) * 100
    ps = precision_score(Y_pred_lr, Y_test) * 100
    rs = recall_score(Y_pred_lr, Y_test) * 100
    f1 = f1_score(Y_pred_lr, Y_test) * 100
    confmat = confusion_matrix(y_true=Y_test, y_pred=Y_pred_lr)
    Prediction_acc[d] = acc * 100
    print("Errors for %s    : %.f" % (d, errors))
    print("Accuracy for %s  : %.2f%%" % (d, acc))
    print("Precision for %s : %.2f%%" % (d, ps))
    print("Recall for %s    : %.2f%%" % (d, rs))
    print("F1 Score for %s  : %.2f%%" % (d, f1))
    print("Confusion Matrix for %s :" % d)
    print(confmat)

    
