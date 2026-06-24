# ============================================================
# AKIENI ACADEMY - Projet Sante Publique
# Semaine 2 - Exercice 1 : Fiche Patient CHU Brazzaville
# Noms = OMBOUMBOU EBOLO Ronel
# Date = 20/06/2026
# ============================================================

# --- SECTION 1 : VARIABLES PATIENT ---
nom_patient         = 'MAVOUNGOU Celestine'
age_patient         = 42
sexe_patient        = 'F'
departement_patient = 'Brazzaville'
couverture_sociale  = 'CNSS'

# --- SECTION 2 : VARIABLES CONSULTATION ---
type_consultation      = 'Urgences'
cout_consultation_fcfa = 15000.0
nb_consultations       = 1
remise_cnss_pct        = 30.0
diagnostic_principal   = 'Paludisme grave'

# --- SECTION 3 : VARIABLES HOPITAL ---
nom_hopital        = 'CHU de Brazzaville'
ville_hopital      = 'Brazzaville'
nb_lits_total      = 320
nb_lits_occupes    = 284
nb_medecins_actifs = 47

# --- SECTION 4 : CALCULS ---
cout_total_fcfa             = cout_consultation_fcfa * nb_consultations * (1 - remise_cnss_pct / 100)
taux_occupation_pct         = round(nb_lits_occupes / nb_lits_total * 100, 1)
nb_consultations_hopital    = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)

# --- SECTION 5 : AFFICHAGE ---
print('=' * 60)
print(f'  FICHE PATIENT - {nom_patient}')
print('=' * 60)
print(f'  Age            : {age_patient} ans')
print(f'  Sexe           : {sexe_patient}')
print(f'  Departement    : {departement_patient}')
print(f'  Couverture     : {couverture_sociale}')
print('-' * 60)
print(f'  CONSULTATION')
print(f'  Type           : {type_consultation}')
print(f'  Diagnostic     : {diagnostic_principal}')
print(f'  Cout unitaire  : 15 000 FCFA')
print(f'  Remise CNSS    : {remise_cnss_pct}%')
print(f'  COUT TOTAL     : {cout_total_fcfa} FCFA')
print('-' * 60)
print(f'  HOPITAL : {nom_hopital}')
print(f'  Ville          : {ville_hopital}')
print(f'  Lits occupes   : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)')
print(f'  Medecins actifs: {nb_medecins_actifs}')
print(f'  Ratio consult. : {ratio_consultations_medecin} consultations / medecin ce matin')
print('=' * 60)
print(f'  STATUT : Prise en charge validee')
print('=' * 60)