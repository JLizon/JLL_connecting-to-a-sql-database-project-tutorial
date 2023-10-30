import pandas as pd
import sqlite3 as sq


url = "https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/master/assets/titanic_train.csv"
table_titanic = pd.read_csv(url, sep=",")

con = sq.connect("table_titanic.db")
table_titanic.to_sql("titanic", con, if_exists="replace")

# Cuántos supervivientes hay (columna Survived)

exercise_1 = con.execute("""SELECT name from titanic
                    WHERE survived = 1 """)

for row in exercise_1:
    print(row)

# De todos los pasajeros, cuántos hombres y mujeres hay (columna Sex)

exercise_2 = con.execute("""SELECT count(sex) AS NUMBER from titanic
                    WHERE Sex Like "male" """)
for row in exercise_2:
    print("Number of men:", row)

exercise_2_1 = con.execute("""SELECT count(sex) AS NUMBER from titanic
                    WHERE Sex Like "female" """)
for row in exercise_2_1:
    print("Number of women:", row)

# Cuál es el valor del ticket más caro que se compró (columna Fare)
exercise_3 = con.execute("""SELECT MAX(Fare) from titanic """)
for row in exercise_3:
    print("The Most Expensive ticket:", row)

con.close()

