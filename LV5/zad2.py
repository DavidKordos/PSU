
# =========================
# ZADATAK 2
# =========================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Učitavanje podataka
df = pd.read_csv("occupancy_processed.csv")

# Ulazi i izlaz
X = df[['S3_Temp', 'S5_CO2']]
y = df['Room_Occupancy_Count']

# =========================
# a) Podjela skupa (80-20, stratify)
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# b) Skaliranje (StandardScaler)
# =========================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
# c) KNN model
# =========================
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predikcija
y_pred = knn.predict(X_test_scaled)

# =========================
# d) Evaluacija
# =========================

# d.a Matrica zabune
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

# d.b Točnost
print("\nTočnost:")
print(accuracy_score(y_test, y_pred))

# d.c Preciznost i odziv
print("\nKlasifikacijski izvještaj:")
print(classification_report(y_test, y_pred))


# =========================
# e) Utjecaj broja susjeda
# =========================
print("\nUtjecaj različitih K vrijednosti:")
for k in [1, 3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, pred)
    print(f"K={k}, točnost={acc}")


# =========================
# f) Bez skaliranja
# =========================
knn_no_scale = KNeighborsClassifier(n_neighbors=3)
knn_no_scale.fit(X_train, y_train)
y_pred_no_scale = knn_no_scale.predict(X_test)

print("\nTočnost BEZ skaliranja:")
print(accuracy_score(y_test, y_pred_no_scale))




