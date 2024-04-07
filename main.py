import time as t


def brut_force(longueur_max, mdp_actuel, mdp_cible, compteur=[0]):
    caracteres_autorises = ''.join(chr(i) for i in range(33, 127))
    if longueur_max == 0:
        compteur[0] += 1
        print(f"Test {compteur[0]} :", mdp_actuel)
        if mdp_actuel == mdp_cible:
            print("Mot de passe trouvé :", mdp_cible)
            return True
        else:
            return False
    else:
        for caractere in caracteres_autorises:
            if brut_force(longueur_max - 1, mdp_actuel + caractere, mdp_cible, compteur):
                return True
        return False

def main():
    mdp = input("Entrez votre mot de passe (max 8 caractères): ")
    if len(mdp) > 8:
        print("Le mot de passe est trop long (max 8 caractères).")
        t.sleep(1)
        return main()
    if brut_force(len(mdp), "", mdp):
        print("Mot de passe trouvé!")
    else:
        print("Mot de passe non trouvé.")

main()
