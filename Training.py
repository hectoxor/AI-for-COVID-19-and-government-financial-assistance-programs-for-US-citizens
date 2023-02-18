orig_train_start_time = time.time() 
nn_clf.fit(X_train, y_train)
orig_train_total_time = time.time() - orig_train_start_time

orig_test_start_time = time.time()
orig_score = nn_clf.score(X_test, y_test)
orig_test_total_time = time.time() - orig_test_start_time
