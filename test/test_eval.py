from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score

def evaluation(X_test, y_test, clf):
    y_pred = clf.predict(X_test)
    
    precision = precision_score(y_test, y_pred)
    expected_precision = 0.85
    assert precision == expected_precision, f"Error: Expected precision {expected_precision}, but got {precision}"
    
    accuracy = accuracy_score(y_test, y_pred)
    expected_accuracy = 0.92
    assert accuracy == expected_accuracy, f"Error: Expected accuracy {expected_accuracy}, but got {accuracy}"
    
    recall = recall_score(y_test, y_pred)
    expected_recall = 0.78
    assert recall == expected_recall, f"Error: Expected recall {expected_recall}, but got {recall}"
    
    f1 = f1_score(y_test, y_pred)
    expected_f1 = 0.81
    assert f1 == expected_f1, f"Error: Expected F1 score {expected_f1}, but got {f1}"
    
    print("Evaluation results:")
    print("Precision:", precision)
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("F1 score:", f1)