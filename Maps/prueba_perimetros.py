import random

for i in range(5):
    arriba_abajo_lat = random.uniform(4.63409, 4.63849)
    arriba_abajo_lng = random.uniform(-74.08444, -74.08192)
    izquierda_derecha_lat = random.uniform(4.63564, 4.63742)
    izquierda_derecha_lng = random.uniform(-74.08545, -74.08134)
    lat = (arriba_abajo_lat + izquierda_derecha_lat) / 2
    lng = (arriba_abajo_lng + izquierda_derecha_lng) / 2
    print("%.6f," % lat, "%.6f" % lng)
