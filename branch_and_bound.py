import time

def welsh_powell_borne(matrice_adj, n):
    """
    Calcule une borne supérieure initiale en utilisant l'algorithme Welsh-Powell.
    """
    degres = sorted(range(n), key=lambda v: sum(matrice_adj[v]), reverse=True)
    couleurs = [-1] * n
    nb_couleurs = 0
    
    for sommet in degres:
        if couleurs[sommet] == -1:
            couleur = nb_couleurs
            couleurs[sommet] = couleur
            
            for autre in degres:
                if couleurs[autre] == -1:
                    if all(not matrice_adj[autre][voisin] or couleurs[voisin] != couleur 
                          for voisin in range(n)):
                        couleurs[autre] = couleur
            nb_couleurs += 1

    return nb_couleurs, couleurs

def generer_couleurs_valides(matrice_adj, sommet, coloration, borne_sup):
    """
    Génère uniquement les couleurs valides pour un sommet donné.
    """
    couleurs_voisins = {coloration[v] for v in range(len(matrice_adj)) 
                       if matrice_adj[sommet][v] and coloration[v] != -1}
    return [c for c in range(borne_sup) if c not in couleurs_voisins]

def evaluer_coloration(matrice_adj, coloration, niveau, nb_couleurs_actuelles):
    """
    Évalue la coloration partielle pour déterminer la borne inférieure.
    Intègre une logique similaire à la fonction Eval de la deuxième solution.
    """
    n = len(matrice_adj)
    increment = False
    
    # Vérifier les sommets non encore colorés
    for v in range(niveau + 1, n):
        # Compter les couleurs différentes des voisins
        couleurs_voisins = set()
        for u in range(n):
            if matrice_adj[v][u] and coloration[u] != -1:
                couleurs_voisins.add(coloration[u])
                
        # Si un sommet est adjacent à toutes les couleurs utilisées
        if len(couleurs_voisins) >= nb_couleurs_actuelles:
            increment = True
            # Vérifier les interactions entre voisins non colorés
            for j in range(v + 1, n):
                if matrice_adj[v][j]:
                    voisins_j = set()
                    for u in range(n):
                        if matrice_adj[j][u] and coloration[u] != -1:
                            voisins_j.add(coloration[u])
                    if len(voisins_j) >= nb_couleurs_actuelles:
                        return nb_couleurs_actuelles + 2
    
    return nb_couleurs_actuelles + 1 if increment else nb_couleurs_actuelles

def branch_and_bound_coloration(matrice_adj):
    """
    Algorithme Branch and Bound 
    """
    temps_debut = time.time()
    n = len(matrice_adj)

    # Initialisation avec Welsh-Powell
    borne_sup, solution_initiale = welsh_powell_borne(matrice_adj, n)
    print("\nwelsh_powell_borne:", borne_sup)
    meilleure_solution = solution_initiale.copy()

    # Pile pour le parcours avec contexte enrichi
    pile = [(0, [-1] * n, 0)]  # (niveau, coloration, nb_couleurs_utilisées)
    
  

    while pile:
        iteration += 1
  
        niveau, coloration, nb_couleurs = pile.pop()
        
        # Solution complète trouvée
        if niveau == n:
            if nb_couleurs < borne_sup:
                borne_sup = nb_couleurs
                meilleure_solution = coloration.copy()
            continue
        
        # Évaluation améliorée
        evaluation = evaluer_coloration(matrice_adj, coloration, niveau, nb_couleurs)
        if evaluation >= borne_sup:
            continue

        # Générer uniquement les couleurs valides
        couleurs_possibles = generer_couleurs_valides(matrice_adj, niveau, coloration, borne_sup)
        
        # Parcourir les couleurs en ordre inverse pour trouver d'abord les solutions avec moins de couleurs
        for couleur in reversed(couleurs_possibles):
            nouvelle_coloration = coloration.copy()
            nouvelle_coloration[niveau] = couleur
            
            # Mettre à jour le nombre de couleurs utilisées
            nouveau_nb_couleurs = max(nb_couleurs, couleur + 1)
            
            if nouveau_nb_couleurs < borne_sup:
                pile.append((niveau + 1, nouvelle_coloration, nouveau_nb_couleurs))
    
    temps_execution = time.time() - temps_debut
    return meilleure_solution, borne_sup, temps_execution