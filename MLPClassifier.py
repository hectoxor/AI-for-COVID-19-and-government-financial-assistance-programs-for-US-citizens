nn_clf = MLPClassifier(
    hidden_layer_sizes = (25,15,10), 
    activation = 'relu',
    solver = 'adam',
    alpha = 0.001,
    learning_rate_init = 0.001,
    tol = 0.0001,
    n_iter_no_change=10,
    max_iter = 10000
)
