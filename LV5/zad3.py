# =========================
# ZADATAK 3 (POTPUNO ISTO KAO ZADATAK 2, ali Decision Tree)
# =========================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt

# =========================
# a) Podjela podataka (80-20, stratify)
# =========================
df = pd.read_csv("occupancy_processed.csv")

X = df[['S3_Temp', 'S5_CO2']]
y = df['Room_Occupancy_Count']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# (b) Skaliranje NIJE potrebno za Decision Tree
# =========================
# NAMJERNO preskačemo scaler jer nema utjecaja

# =========================
# c) Model stabla odlučivanja
# =========================
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

y_pred = tree.predict(X_test)

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
# a) Vizualizacija stabla
# =========================
plt.figure(figsize=(10,6))
plot_tree(tree, feature_names=X.columns, class_names=True, filled=True)
plt.title("Decision Tree")
plt.show()


# =========================
# b) Utjecaj max_depth
# =========================
print("\nUtjecaj max_depth:")

for depth in [1, 2, 3, 5, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"max_depth={depth}, točnost={acc}")


# =========================
# c) Skaliranje (testiramo da nema razlike)
# =========================
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

tree_scaled = DecisionTreeClassifier(random_state=42)
tree_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = tree_scaled.predict(X_test_scaled)

print("\nTočnost SA skaliranjem:")
print(accuracy_score(y_test, y_pred_scaled))

print("Točnost BEZ skaliranja:")
print(accuracy_score(y_test, y_pred))