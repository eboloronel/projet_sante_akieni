# =============================================================
# SEMAINE 2 - CHALLENGE : Rapport comparatif des 3 hôpitaux du Pool
# Auteur  : OMBOUMBOU EBOLO Ronel (Lenor)
# Date    : Juin 2026
# Mission : Rapport pour Dr. ELENGA Pascal, Directeur de la DSS
# =============================================================

# --- HÔPITAL DISTRICT DE KINKALA ---
budget_kinkala           = 12_500_000   # FCFA
consultations_kinkala    = 1_847
hospitalisations_kinkala = 312
deces_kinkala            = 8
lits_totaux_kinkala      = 45
lits_occupes_kinkala     = 41
medecins_kinkala         = 3
population_kinkala       = 85_000

# --- CMS DE VINDZA ---
budget_vindza            = 6_800_000    # FCFA
consultations_vindza     = 923
hospitalisations_vindza  = 87
deces_vindza             = 2
lits_totaux_vindza       = 20
lits_occupes_vindza      = 14
medecins_vindza          = 1
population_vindza        = 42_000

# --- HÔPITAL DE KINDAMBA ---
budget_kindamba           = 9_200_000   # FCFA
consultations_kindamba    = 1_234
hospitalisations_kindamba = 201
deces_kindamba            = 11
lits_totaux_kindamba      = 35
lits_occupes_kindamba     = 33
medecins_kindamba         = 2
population_kindamba       = 67_000

# =============================================================
# CALCUL DES KPIs
# =============================================================

# Coût moyen par patient = Budget / (Consultations + Hospitalisations)
cout_kinkala  = budget_kinkala  / (consultations_kinkala  + hospitalisations_kinkala)
cout_vindza   = budget_vindza   / (consultations_vindza   + hospitalisations_vindza)
cout_kindamba = budget_kindamba / (consultations_kindamba + hospitalisations_kindamba)

# Taux d'occupation = (Lits occupés / Lits totaux) * 100
taux_occupation_kinkala  = (lits_occupes_kinkala  / lits_totaux_kinkala)  * 100
taux_occupation_vindza   = (lits_occupes_vindza   / lits_totaux_vindza)   * 100
taux_occupation_kindamba = (lits_occupes_kindamba / lits_totaux_kindamba) * 100

# Densité médicale = Médecins / Population desservie
densite_kinkala  = medecins_kinkala  / population_kinkala
densite_vindza   = medecins_vindza   / population_vindza
densite_kindamba = medecins_kindamba / population_kindamba

# Taux de mortalité = (Décès / Hospitalisations) * 100
mortalite_kinkala  = (deces_kinkala  / hospitalisations_kinkala)  * 100
mortalite_vindza   = (deces_vindza   / hospitalisations_vindza)   * 100
mortalite_kindamba = (deces_kindamba / hospitalisations_kindamba) * 100

# =============================================================
# IDENTIFICATION DES HÔPITAUX EN SITUATION CRITIQUE
# Critère : taux mortalité > 2% OU densité médicale < 0.05
# =============================================================

critique_kinkala  = mortalite_kinkala  > 2 or densite_kinkala  < 0.05
critique_vindza   = mortalite_vindza   > 2 or densite_vindza   < 0.05
critique_kindamba = mortalite_kindamba > 2 or densite_kindamba < 0.05

statut_kinkala  = "CRITIQUE" if critique_kinkala  else "STABLE"
statut_vindza   = "CRITIQUE" if critique_vindza   else "STABLE"
statut_kindamba = "CRITIQUE" if critique_kindamba else "STABLE"

# =============================================================
# RAPPORT CONSOLIDÉ
# =============================================================

print("=" * 65)
print("  RAPPORT COMPARATIF - 3 HOPITAUX DU DEPARTEMENT DU POOL")
print("  Prepare pour : Dr. ELENGA Pascal, Directeur de la DSS")
print("=" * 65)

print(f"\n{'INDICATEUR':<30} {'KINKALA':>10} {'VINDZA':>8} {'KINDAMBA':>10}")
print("-" * 65)
print(f"{'Cout moyen/patient (FCFA)':<30} {cout_kinkala:>10.2f} {cout_vindza:>8.2f} {cout_kindamba:>10.2f}")
print(f"{'Taux occupation (%)':<30} {taux_occupation_kinkala:>10.2f} {taux_occupation_vindza:>8.2f} {taux_occupation_kindamba:>10.2f}")
print(f"{'Densite medicale':<30} {densite_kinkala:>10.5f} {densite_vindza:>8.5f} {densite_kindamba:>10.5f}")
print(f"{'Taux de mortalite (%)':<30} {mortalite_kinkala:>10.2f} {mortalite_vindza:>8.2f} {mortalite_kindamba:>10.2f}")
print("-" * 65)
print(f"{'Statut':<30} {statut_kinkala:>10} {statut_vindza:>8} {statut_kindamba:>10}")
print("=" * 65)

# --- Alertes ---
print("\nALERTES - HOPITAUX EN SITUATION CRITIQUE")
print("=" * 65)

if critique_kinkala:
    print(f"[!] Hopital District Kinkala : mortalite={mortalite_kinkala:.2f}%, densite={densite_kinkala:.5f}")
if critique_vindza:
    print(f"[!] CMS de Vindza            : mortalite={mortalite_vindza:.2f}%, densite={densite_vindza:.5f}")
if critique_kindamba:
    print(f"[!] Hopital de Kindamba      : mortalite={mortalite_kindamba:.2f}%, densite={densite_kindamba:.5f}")

# =============================================================
# BONUS : Le budget total suffit-il pour 5 médecins par hôpital ?
# Coût d'un médecin : 1 200 000 FCFA/trimestre
# =============================================================

cout_medecin      = 1_200_000
medecins_cibles   = 5
budget_total      = budget_kinkala + budget_vindza + budget_kindamba
budget_necessaire = 3 * medecins_cibles * cout_medecin

print("\n" + "=" * 65)
print("BONUS - ANALYSE BUDGETAIRE : 5 MEDECINS PAR HOPITAL")
print("=" * 65)
print(f"Budget total des 3 hopitaux : {budget_total:>15,.0f} FCFA")
print(f"Budget necessaire           : {budget_necessaire:>15,.0f} FCFA")

if budget_total >= budget_necessaire:
    reste = budget_total - budget_necessaire
    print(f"[OK] Budget SUFFISANT - Excedent : {reste:,.0f} FCFA")
else:
    deficit = budget_necessaire - budget_total
    print(f"[X] Budget INSUFFISANT - Deficit : {deficit:,.0f} FCFA")

print("=" * 65)