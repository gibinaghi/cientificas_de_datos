import pandas as pd

def test_static():
    df = pd.read_csv("../data/spam.csv", encoding="latin-1")
    assert df is not None, "Error: DataFrame is not loaded"
    assert len(df.columns) == 2, "Error: DataFrame should have 2 columns"
    print ("listo")

# Prueba de la función test_static
test_static()
