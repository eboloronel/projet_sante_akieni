# =============================================================
# MODULE FONDATEUR - Projet Sante Publique / Akieni Academy
# Auteur  : OMBOUMBOU EBOLO Ronel 
# Date    : Juin 2026
# =============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS =========

TAUX_EUR_FCFA               = 655.957       # taux de change EUR -> FCFA
TAUX_USD_FCFA               = 600.0         # taux de change USD -> FCFA
SEUIL_OMS_DENSITE_MEDICALE  = 2.3           # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0          # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE      = 2.0           # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS   = 30            # jours minimum de stock

DEPARTEMENTS_CONGO = {
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
}                                            # 12 departements officiels

# === SECTION B : VARIABLES DES 5 HOPITAUX ====================

# Hopital 1 - CHU de Brazzaville
h1_nom             = 'CHU de Brazzaville'
h1_ville           = 'Brazzaville'
h1_departement     = 'Brazzaville'
h1_type            = 'CHU'
h1_nb_lits         = 320
h1_nb_lits_occupes = 284
h1_nb_medecins     = 47
h1_nb_infirmiers   = 123
h1_population_zone = 1_800_000

# Hopital 2 - Hopital General de Pointe-Noire
h2_nom             = 'Hopital General de Pointe-Noire'
h2_ville           = 'Pointe-Noire'
h2_departement     = 'Kouilou'
h2_type            = 'Hopital General'
h2_nb_lits         = 250
h2_nb_lits_occupes = 198
h2_nb_medecins     = 32
h2_nb_infirmiers   = 87
h2_population_zone = 800_000

# Hopital 3 - Hopital de Dolisie
h3_nom             = 'Hopital de Dolisie'
h3_ville           = 'Dolisie'
h3_departement     = 'Niari'
h3_type            = 'Hopital General'
h3_nb_lits         = 120
h3_nb_lits_occupes = 89
h3_nb_medecins     = 12
h3_nb_infirmiers   = 34
h3_population_zone = 180_000

# Hopital 4 - Hopital de District Owando
h4_nom             = 'Hopital de District Owando'
h4_ville           = 'Owando'
h4_departement     = 'Cuvette'
h4_type            = 'Hopital de District'
h4_nb_lits         = 60
h4_nb_lits_occupes = 41
h4_nb_medecins     = 5
h4_nb_infirmiers   = 18
h4_population_zone = 75_000

# Hopital 5 - Centre de Sante de Impfondo
h5_nom             = 'Centre de Sante de Impfondo'
h5_ville           = 'Impfondo'
h5_departement     = 'Likouala'
h5_type            = 'Centre de Sante'
h5_nb_lits         = 30
h5_nb_lits_occupes = 22
h5_nb_medecins     = 2
h5_nb_infirmiers   = 8
h5_population_zone = 45_000

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ESSENTIELS ======

# Medicament 1 - Artemether-Lumefantrine (antipaludeen)
med1_nom            = 'Artemether-Lumefantrine'
med1_quantite       = 5000               # comprimes disponibles
med1_seuil_rupture  = 500                # seuil d'alerte rupture
med1_cout_unitaire  = 850.0              # FCFA par comprime

# Medicament 2 - Amoxicilline (antibiotique)
med2_nom            = 'Amoxicilline'
med2_quantite       = 12000
med2_seuil_rupture  = 1000
med2_cout_unitaire  = 120.0              # FCFA par gelule

# Medicament 3 - Paracetamol (analgesique)
med3_nom            = 'Paracetamol'
med3_quantite       = 25000
med3_seuil_rupture  = 2000
med3_cout_unitaire  = 50.0               # FCFA par comprime

# Medicament 4 - SRO (Sels de Rehydratation Orale)
med4_nom            = 'SRO'
med4_quantite       = 8000
med4_seuil_rupture  = 800
med4_cout_unitaire  = 200.0              # FCFA par sachet

# Medicament 5 - Vaccin Antipaludeen
med5_nom            = 'Vaccin Antipaludeen'
med5_quantite       = 3000
med5_seuil_rupture  = 300
med5_cout_unitaire  = 2500.0             # FCFA par dose

# === SECTION D : CALCULS D'INITIALISATION ====================

# Total medecins et population des 5 hopitaux
total_medecins   = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

# Densite medicale nationale (medecins pour 1000 habitants)
densite_medicale_nationale = (total_medecins / total_population) * 1000

# Taux d'occupation moyen des 5 hopitaux (%)
taux_occ_h1 = (h1_nb_lits_occupes / h1_nb_lits) * 100
taux_occ_h2 = (h2_nb_lits_occupes / h2_nb_lits) * 100
taux_occ_h3 = (h3_nb_lits_occupes / h3_nb_lits) * 100
taux_occ_h4 = (h4_nb_lits_occupes / h4_nb_lits) * 100
taux_occ_h5 = (h5_nb_lits_occupes / h5_nb_lits) * 100

taux_occupation_moyen = (taux_occ_h1 + taux_occ_h2 + taux_occ_h3 + taux_occ_h4 + taux_occ_h5) / 5

# Valeur totale du stock de medicaments (FCFA)
valeur_stock_total = (
    med1_quantite * med1_cout_unitaire +
    med2_quantite * med2_cout_unitaire +
    med3_quantite * med3_cout_unitaire +
    med4_quantite * med4_cout_unitaire +
    med5_quantite * med5_cout_unitaire
)

# === SECTION E : RAPPORT D'INVENTAIRE ========================

print("=" * 65)
print("   RAPPORT INITIAL - SYSTEME DE SANTE / AKIENI ACADEMY")
print("=" * 65)

print("\n--- HOPITAUX ENREGISTRES ---")
print(f"  1. {h1_nom:<35} ({h1_departement})")
print(f"  2. {h2_nom:<35} ({h2_departement})")
print(f"  3. {h3_nom:<35} ({h3_departement})")
print(f"  4. {h4_nom:<35} ({h4_departement})")
print(f"  5. {h5_nom:<35} ({h5_departement})")

print("\n--- KPIs GLOBAUX INITIAUX ---")
print(f"  Total medecins            : {total_medecins} medecins")
print(f"  Population totale couverte: {total_population:,} habitants")
print(f"  Densite medicale nationale: {densite_medicale_nationale:.4f} medecins/1000 hab")
print(f"  Seuil OMS densite         : {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab")

if densite_medicale_nationale < SEUIL_OMS_DENSITE_MEDICALE:
    print(f"  [!] ALERTE : Densite sous le seuil OMS !")
else:
    print(f"  [OK] Densite conforme aux normes OMS")

print(f"\n  Taux d'occupation moyen   : {taux_occupation_moyen:.2f}%")

print("\n--- STOCK DE MEDICAMENTS ---")
print(f"  {med1_nom:<30} : {med1_quantite:>6} unites")
print(f"  {med2_nom:<30} : {med2_quantite:>6} unites")
print(f"  {med3_nom:<30} : {med3_quantite:>6} unites")
print(f"  {med4_nom:<30} : {med4_quantite:>6} unites")
print(f"  {med5_nom:<30} : {med5_quantite:>6} unites")
print(f"\n  Valeur totale du stock    : {valeur_stock_total:,.0f} FCFA")
print(f"                            = {valeur_stock_total / TAUX_EUR_FCFA:,.2f} EUR")
print(f"                            = {valeur_stock_total / TAUX_USD_FCFA:,.2f} USD")

print("\n" + "=" * 65)
print("  Module sante_variables.py charge avec succes.")
print("=" * 65)