import csv
import html
import os
import random
import re
import sys

# Codes couleurs ANSI pour le terminal
CYAN = "\033[96m"
VERT = "\033[92m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
GRAS = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def nettoyer_html(texte: str) -> str:
    """Convertit les balises HTML d'Anki en texte lisible dans le terminal."""
    texte = texte.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    texte = re.sub(r"<code>(.*?)</code>", f"{JAUNE}\\1{RESET}", texte, flags=re.DOTALL)
    texte = re.sub(r"<b>(.*?)</b>", f"{GRAS}\\1{RESET}", texte, flags=re.DOTALL)
    texte = re.sub(r"<[^>]+>", "", texte)
    return html.unescape(texte).strip()


def charger_flashcards(chemin_csv: str) -> list[dict]:
    """Charge les flashcards depuis le fichier CSV Anki."""
    if not os.path.exists(chemin_csv):
        print(f"{ROUGE}Erreur : Le fichier '{chemin_csv}' est introuvable.{RESET}")
        print("Assure-toi que quiz_cli.py et 30_flashcards_anki.csv sont dans le même dossier.")
        sys.exit(1)

    cartes = []
    with open(chemin_csv, mode="r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        for ligne in lecteur:
            if len(ligne) >= 3:
                tags = ligne[2].split()
                theme = tags[0] if tags else "General"
                type_carte = tags[1] if len(tags) > 1 else ""
                cartes.append({
                    "question": nettoyer_html(ligne[0]),
                    "reponse": nettoyer_html(ligne[1]),
                    "theme": theme,
                    "type": type_carte,
                })
    return cartes


def effacer_ecran():
    os.system("cls" if os.name == "nt" else "clear")


def choisir_mode(cartes: list[dict]) -> list[dict]:
    """Affiche le menu des thèmes et retourne les cartes sélectionnées."""
    themes = sorted(list({c["theme"] for c in cartes}))

    print(f"{CYAN}{GRAS}=== 🧠 ENTRAÎNEMENT FLASHCARDS ALGORITHMIQUES ==={RESET}\n")
    print("Choisis ton mode de révision :\n")
    print(f"  {GRAS}0.{RESET} Tout mélanger ({len(cartes)} cartes)")

    for idx, theme in enumerate(themes, start=1):
        nb = sum(1 for c in cartes if c["theme"] == theme)
        nom_propre = theme.replace("_", " ")
        print(f"  {GRAS}{idx}.{RESET} {nom_propre} ({nb} cartes)")

    print(f"\n  {DIM}q. Quitter{RESET}")

    while True:
        choix = input(f"\n{CYAN}Ton choix : {RESET}").strip().lower()
        if choix == "q":
            sys.exit(0)
        if choix == "0":
            selection = list(cartes)
            random.shuffle(selection)
            return selection
        if choix.isdigit() and 1 <= int(choix) <= len(themes):
            theme_choisi = themes[int(choix) - 1]
            selection = [c for c in cartes if c["theme"] == theme_choisi]
            random.shuffle(selection)
            return selection
        print(f"{ROUGE}Choix invalide. Entre un numéro entre 0 et {len(themes)}.{RESET}")


def lancer_session(cartes: list[dict]):
    """Exécute une session de révision avec relance des cartes ratées."""
    a_reviser = list(cartes)
    tour = 1

    while a_reviser:
        effacer_ecran()
        print(f"{CYAN}{GRAS}--- TOUR {tour} ({len(a_reviser)} carte(s) restante(s)) ---{RESET}\n")
        ratees = []

        for idx, carte in enumerate(a_reviser, start=1):
            badge = f"[{carte['theme'].replace('_', ' ')} | {carte['type']}]"
            print(f"{DIM}Carte {idx}/{len(a_reviser)} {badge}{RESET}")
            print(f"\n{GRAS}❓ QUESTION :{RESET}\n{carte['question']}\n")

            cmd = input(f"{DIM}[Appuie sur Entrée pour voir la réponse, ou 'q' pour quitter]{RESET} ").strip().lower()
            if cmd == "q":
                return

            print(f"\n{VERT}{GRAS}💡 RÉPONSE :{RESET}\n{carte['reponse']}\n")
            print("-" * 50)

            while True:
                eval_user = input(f"As-tu trouvé la bonne réponse ? ({VERT}o{RESET}/{ROUGE}n{RESET}) : ").strip().lower()
                if eval_user in ("o", "oui", "y", "yes"):
                    break
                if eval_user in ("n", "non", "no"):
                    ratees.append(carte)
                    break
                print("Réponds par 'o' (oui) ou 'n' (non).")

            print("\n" + "=" * 50 + "\n")

        if ratees:
            print(f"{JAUNE}Tu as raté {len(ratees)} carte(s). On les rejoue au tour suivant !{RESET}")
            input(f"{DIM}[Appuie sur Entrée pour continuer]{RESET}")
            a_reviser = ratees
            random.shuffle(a_reviser)
            tour += 1
        else:
            print(f"{VERT}{GRAS}🎉 Félicitations ! Tu as validé 100 % des cartes de cette session !{RESET}\n")
            break


def main():
    dossier_script = os.path.dirname(os.path.abspath(__file__))
    chemin_csv = os.path.join(dossier_script, "30_flashcards_anki.csv")
    cartes = charger_flashcards(chemin_csv)

    while True:
        effacer_ecran()
        selection = choisir_mode(cartes)
        lancer_session(selection)
        rejouer = input("Veux-tu faire une autre session ? (o/n) : ").strip().lower()
        if rejouer not in ("o", "oui", "y", "yes"):
            print("À bientôt et bon code !")
            break


if __name__ == "__main__":
    main()
