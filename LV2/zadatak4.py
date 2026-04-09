import numpy as np
import matplotlib.pyplot as plt

def generiraj_sahovnicu(velicina_kvadrata, broj_redaka, broj_stupaca):
    # Kreiramo osnovni crni i bijeli kvadrat
    # Množimo s 255 jer imshow koristi vmin=0, vmax=255
    crni = np.zeros((velicina_kvadrata, velicina_kvadrata))
    bijeli = np.ones((velicina_kvadrata, velicina_kvadrata)) * 255
    
    retci_liste = []
    
    for i in range(broj_redaka):
        blokovi_u_retku = []
        for j in range(broj_stupaca):
            # Ako je zbroj indeksa paran, stavi bijeli, inače crni (ili obrnuto)
            # Na ovaj način dobivamo naizmjenični uzorak
            if (i + j) % 2 == 0:
                blokovi_u_retku.append(bijeli)
            else:
                blokovi_u_retku.append(crni)
        
        # Spajamo kvadrate u jedan vodoravni red (horizontal stack)
        cijeli_redak = np.hstack(blokovi_u_retku)
        retci_liste.append(cijeli_redak)
    
    # Spajamo sve retke vertikalno (vertical stack)
    konacna_slika = np.vstack(retci_liste)
    
    return konacna_slika

# --- Testiranje funkcije ---

# Postavke prema primjeru sa slike (kvadrati su 50x50, 4x5 mreža)
velicina = 50
n_visina = 4
n_sirina = 5

img = generiraj_sahovnicu(velicina, n_visina, n_sirina)

# Prikaz slike prema uputi iz zadatka
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
