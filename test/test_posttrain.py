import joblib

def test_post_train():
    NB_spam_model = open('../model/spam_clf_v1.pkl', 'rb')
    clf = joblib.load(NB_spam_model)
    assert clf is not None, "Error: Model is not loaded"
    print ("listo")

test_post_train()


