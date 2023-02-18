def nn_objective(trial):
    layers = []
    hidden_layer_spec = (25,15,10)
    alpha = trial.suggest_float("alpha", 1e-5, 1e-1)
    activation = trial.suggest_categorical("activation", ["relu", "tanh", "logistic"])
    solver = trial.suggest_categorical("solver", ["adam", "sgd"])
    n_iter_no_change = trial.suggest_int("n_iter_no_change", 10, 50)
    learning_rate_init = trial.suggest_float("learning_rate_init", 1e-5, 1e0)
    max_iter = trial.suggest_int("max_iter", 10000, 20000)
    tol = trial.suggest_float("tol", 1e-5, 1e-3)
    model = MLPClassifier(
                hidden_layer_sizes = hidden_layer_spec, 
                activation = activation,
                solver = 'adam',
                alpha = alpha,
                learning_rate_init = learning_rate_init,
                tol = tol,
                n_iter_no_change= n_iter_no_change,
                max_iter = max_iter
            )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
study = optuna.create_study(direction="maximize")
study.optimize(nn_objective, n_trials=10)
