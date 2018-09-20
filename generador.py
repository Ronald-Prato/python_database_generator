import random
import pandas as pd
import sys
names = pd.read_csv("names_csv.csv")
lastnames = pd.read_csv("lastnames_csv.csv")
dn = pd.DataFrame(names)
dl = pd.DataFrame(lastnames)
db = open("db.txt", "w")


if __name__ == '__main__':

    if len(sys.argv) > 1:
        db = {}
        subdata = []
        finalData = []

        if int(sys.argv[1]) == 1:

            indices = ["Nombre", "Apellido", "E-mail", "Telefono"]

            for i in range(int(sys.argv[2])):

                random_name = dn['names'][random.randint(0, 5000)]
                random_lastname = dl['lastnames'][random.randint(0, 5000)]

                # print("\n\n", random_name, "\n\n")
                # print("\n\n", random_lastname, "\n\n")
                # input("Presione")
                del subdata[:]
                subdata.append(random_name)
                subdata.append(random_lastname)
                subdata.append((random_name + random_lastname).lower() + "@gmail.com")
                subdata.append("350 - " + ("%d" %random.randint(1, 9999999)))

                for k in range(len(indices)):
                    db[indices[k]] = subdata[k]
                finalData.append(db.copy())

            # ···································· Creacion de la base de datos ······················································
            with open('db.txt', 'w') as f:
                for item in finalData:
                    f.write("%s\n" % item)
            df = pd.DataFrame(finalData, columns=indices)
            print(df)


        elif int(sys.argv[1]) == 2:
            indices = ["Nombre", "Tipo", "Latitud", "Longitud"]
            tipo_nombre = ["Restaurante", "Chamba", "Quiosco"]

            for i in range(int(sys.argv[2])):
                random_name = dn['names'][random.randint(0, 5000)]
                random_type = random.choice(tipo_nombre)
                random_store_name = (random_type + " " + random_name)
                random_type_name = (random_type)

                lat = (random.uniform(4.63409, 4.63849) + random.uniform(4.63564, 4.63742)) / 2
                lng = (random.uniform(-74.08444, -74.08192) + random.uniform(-74.08545, -74.08134)) / 2

                del subdata[:]
                subdata.append(random_store_name)
                subdata.append(random_type_name)
                subdata.append(lat)
                subdata.append(lng)

                for k in range(len(indices)):
                    db[indices[k]] = subdata[k]
                finalData.append(db.copy())

            # ···································· Creacion de la base de datos ······················································
            with open('db.txt', 'w') as f:
                for item in finalData:
                    f.write("%s\n" % item)

            df = pd.DataFrame(finalData, columns=indices)
            print(df)




        # for i in range(len(indices)):
    else:
        print("""Ingrese los valores en este orden de argumentos:
                Argumento 1. 
                    {
                        (teclear '1') Modelo A: Nombre - Apellido - Email - Telefono
                        (teclear '2') Modelo B: Nombre - Tipo - Latitud - Longitud
                    }
                Argumento 2. Numero de filas       
        """)