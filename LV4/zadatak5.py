import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error


# ucitavanje podataka
podaci = pd.read_csv('cars_processed.csv')


# ========================
# 1. makni nepotrebne stupce
# ========================
podaci = podaci.drop(['name'], axis=1)


# ========================
# 2. uzmi samo numeričke podatke
# ========================
numericki = podaci.select_dtypes(include=['int64', 'float64'])


# ========================
# 3. podjela na ulaz i izlaz
# ========================
X = numerički.drop('selling_price', axis=1)
y = numerički['selling_price']


# ========================
# 4. train/test split (80/20)
# ========================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# ========================
# 5. skaliranje podataka
# ========================
skaliranje = StandardScaler()

X_train = skaliranje.fit_transform(X_train)
X_test = skaliranje.transform(X_test)


# ========================
# 6. treniranje modela
# ========================
model = LinearRegression()
model.fit(X_train, y_train)


# ========================
# 7. predikcija
# ========================
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)


# ========================
# 8. evaluacija modela
# ========================
print("REZULTATI NA TRAIN SKUPU:")
print("MAE:", mean_absolute_error(y_train, y_pred_train))
print("MSE:", mean_squared_error(y_train, y_pred_train))
print("R2:", r2_score(y_train, y_pred_train))
print("Max error:", max_error(y_train, y_pred_train))


print("\nREZULTATI NA TEST SKUPU:")
print("MAE:", mean_absolute_error(y_test, y_pred_test))
print("MSE:", mean_squared_error(y_test, y_pred_test))
print("R2:", r2_score(y_test, y_pred_test))
print("Max error:", max_error(y_test, y_pred_test))
