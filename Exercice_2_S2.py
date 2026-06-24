# ============================================================
# AKIENI ACADEMY - Projet Sante Publique
# Semaine 2 - Exercice 2 : Fiche Patient CHU Brazzaville
# Noms = OMBOUMBOU EBOLO Ronel
# Date = 20/06/2026
# ============================================================

# --- DONNEES BRUTES ---
budget_fcfa           = 87_450_000
nb_consultations_ext  = 4823
nb_hospitalisations   = 1247
nb_deces              = 18
nb_lits_total         = 180
nb_lits_occupes       = 143
nb_medecins           = 22
nb_infirmiers         = 58
population_dept       = 128_000
taux_eur_fcfa         = 655.957
taux_usd_fcfa         = 600.0

# 1. Conversions devises
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)

# 2. Indicateurs OMS
densite_medicale = round((nb_medecins / population_dept) * 1000, 2)
taux_mortalite   = round((nb_deces / nb_hospitalisations) * 100, 2)
taux_occupation  = round((nb_lits_occupes / nb_lits_total) * 100, 1)

# 3. Division entiere et modulo
budget_medicaments   = int(budget_fcfa * 0.35)
cout_journalier_meds = 450_000
jours_stock          = budget_medicaments // cout_journalier_meds
jours_restants       = budget_medicaments % cout_journalier_meds

# 4. Puissance N+2
budget_n_plus_2 = round(budget_fcfa * (1.08 ** 2), 2)

# --- AFFICHAGE ---
print('=' * 60)
print(f'  RAPPORT Q4 2025 - Hopital General Pointe-Noire')
print('=' * 60)
print(f'  BUDGET')
print(f'  Total FCFA     : {budget_fcfa} FCFA')
print(f'  Equivalent EUR : {budget_eur} EUR')
print(f'  Equivalent USD : {budget_usd} USD')
print(f'  Projection N+2 : {budget_n_plus_2} FCFA')
print('-' * 60)
print(f'  INDICATEURS OMS')
print(f'  Densite med.   : {densite_medicale} medecins / 1000 hab.')
print(f'  Taux mortalite : {taux_mortalite}%')
print(f'  Taux occupation: {taux_occupation}%')
print('-' * 60)
print(f'  MEDICAMENTS')
print(f'  Budget meds    : {budget_medicaments} FCFA')
print(f'  Jours de stock : {jours_stock} jours')
print(f'  Reste           : {jours_restants} FCFA')
print('-' * 60)
nb_pair_impair = 'PAIR' if nb_consultations_ext % 2 == 0 else 'IMPAIR'
print(f'  Consultations  : {nb_consultations_ext} ({nb_pair_impair})')
print('=' * 60)