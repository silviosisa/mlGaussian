def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    from sklearn.naive_bayes import GaussianNB
    clf_pf = GaussianNB()
    clf_pf.partial_fit(features_train, labels_train, labels_train)
    return clf_pf

