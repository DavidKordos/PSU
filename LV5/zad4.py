# =========================
# ZADATAK 4 (ISPRAVLJENO)
# =========================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =========================
# Učitavanje podataka (DODANO!)
# =========================
df = pd.read_csv("occupancy_processed.csv")

X = df[['S3_Temp', 'S5_CO2']]
y = df['Room_Occupancy_Count']

# =========================
# Podjela (DODANO!)
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# Skaliranje (BITNO!)
# =========================
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================
# Model logističke regresije
# =========================
log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

# Predikcija
y_pred_log = log_reg.predict(X_test_scaled)

# =========================
# Evaluacija
# =========================
print("Točnost logističke regresije:")
print(accuracy_score(y_test, y_pred_log))

print("\nKlasifikacijski izvještaj:")
print(classification_report(y_test, y_pred_log))

# =========================
# Objašnjenje rezultata
# =========================
print("\nOBJAŠNJENJE:")
print("""
Logistička regresija koristi linearnu granicu između klasa.

Ako su podaci:
- dobro linearno razdvojivi → model radi dobro
- nelinearni → performanse padaju

Skaliranje je važno jer model koristi koeficijente i optimizaciju.
""")