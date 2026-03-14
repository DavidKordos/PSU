#osnovni program
sati = float(input("Radni sati: "))
placa_po_satu = float(input("Eura/h: "))

ukupno = sati * placa_po_satu

print("Ukupno:", ukupno, "eura")


#Program s funkcijom total_euro
def total_euro(sati, placa_po_satu):
    return sati * placa_po_satu


sati = float(input("Radni sati: "))
placa_po_satu = float(input("Eura/h: "))

ukupno = total_euro(sati, placa_po_satu)

print("Ukupno:", ukupno, "eura")
