from luas.segitiga import luas_segitiga
from luas import lingkaran, persegi
from volume.kubus import volume_kubus
import volume.bola
from volume.prisma import *

print("Luas Segitiga:", luas_segitiga(10, 5))
print("Luas Lingkaran:", lingkaran.luas_lingkaran(21))
print("Luas Persegi:", persegi.luas_persegi(4))
print("Volume Kubus:", volume_kubus(8))
print("Volume Bola:", volume.bola.volume_bola(8))
print("Volume Prisma:", volume_prisma(6, 9, 20))