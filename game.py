import random

print("==============================")
print("     NORTON TEBAK ANGKA")
print("==============================")

angka_rahasia = random.randint(1, 10)

tebakan = int(input("Tebak angka 1-10: "))

if tebakan == angka_rahasia:
    print("🎉 BENAR!")
else:
    print("❌ SALAH!")
    print("Angka yang benar adalah:", angka_rahasia)
