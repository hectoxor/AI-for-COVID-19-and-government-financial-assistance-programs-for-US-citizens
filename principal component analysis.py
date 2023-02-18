def make_pca(X_train, num_components): 
    pca = PCA(n_components = num_components)
    X_train_pca = pca.fit_transform(X_train)
    return pca, X_train_pca
pca_25, X_train_pca_25 = make_pca(X_train, num_components = 25)
X_test_pca_25 = pca_25.transform(X_test)
