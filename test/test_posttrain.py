#test de post-train
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Cargar los datos de entrenamiento
data_train = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
data_train = data_train[["class", "message"]]
x_train = data_train["message"]
y_train = data_train["class"]

# Crear el vectorizador
cv = CountVectorizer()
X_train = cv.fit_transform(x_train)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.33, random_state=42)

# Crear el clasificador y entrenarlo
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Cargar los datos de prueba
data_test = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding='latin-1')
data_test = data_test[["class", "message"]]
x_test = data_test["message"]
y_test = data_test["class"]

# Transformar los datos de prueba
X_test = cv.transform(x_test)

# Realizar la predicción en los datos de prueba
y_pred = clf.predict(X_test)

# Calcular y mostrar las métricas de evaluación
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='spam')
recall = recall_score(y_test, y_pred, pos_label='spam')
f1 = f1_score(y_test, y_pred, pos_label='spam')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")