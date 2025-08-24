print('----kalkulator sederhana----')
print('----------------------------')
print('')

angka_1 = int(input('masukan angka pertama : '))
option = input('pilih opsi (+, -, *, /): ')
angka_2 = int(input('masukan angka kedua : '))

# opsi
opsi_plus = angka_1 + angka_2
opsi_min = angka_1 - angka_2
opsi_kali = angka_1 * angka_2
opsi_bagi = angka_1 / angka_2
print('------------------------')

if option == '+':
    print('Hasilnya adalah : ' + str(opsi_plus))
elif option == '-':
    print('Hasilnya adalah : ' + str(opsi_min))
elif option == '*':
    print('Hasilnya adalah : ' + str(opsi_kali))
elif option == '/':
    print('Hasilnya adalah: ' + str(opsi_bagi))
    print('dan jika dibulatkan, menjadi ' + str(round(opsi_bagi)))
else:
    print('Opsi tidak valid!')
