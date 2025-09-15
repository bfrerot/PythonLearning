import csv
import re
import pdfplumber
from datetime import datetime
import os
import glob

class ReleveBancaireParser:
    def __init__(self):
        self.transactions = []
        
    def lister_fichiers_pdf(self):
        """Liste tous les fichiers PDF du répertoire courant"""
        fichiers_pdf = glob.glob("*.pdf")
        return fichiers_pdf
    
    def choisir_fichier(self):
        """Interface interactive pour choisir un fichier PDF"""
        print("=" * 50)
        print("🏦 EXTRACTEUR DE RELEVÉ BANCAIRE PDF → CSV")
        print("=" * 50)
        
        fichiers_pdf = self.lister_fichiers_pdf()
        
        if not fichiers_pdf:
            print("❌ Aucun fichier PDF trouvé dans le répertoire courant.")
            print("💡 Placez votre relevé bancaire PDF dans le même dossier que ce script.")
            input("Appuyez sur Entrée pour quitter...")
            return None
        
        print(f"\n📁 Fichiers PDF trouvés dans le répertoire :")
        print("-" * 40)
        
        for i, fichier in enumerate(fichiers_pdf, 1):
            taille = os.path.getsize(fichier) / 1024
            print(f"{i}. {fichier} ({taille:.1f} KB)")
        
        print("\n" + "-" * 40)
        
        while True:
            try:
                choix = input(f"Choisissez un fichier (1-{len(fichiers_pdf)}) ou 'q' pour quitter : ").strip()
                
                if choix.lower() == 'q':
                    print("👋 Au revoir !")
                    return None
                
                numero = int(choix)
                if 1 <= numero <= len(fichiers_pdf):
                    fichier_choisi = fichiers_pdf[numero - 1]
                    print(f"\n✅ Fichier sélectionné : {fichier_choisi}")
                    return fichier_choisi
                else:
                    print(f"❌ Veuillez choisir un nombre entre 1 et {len(fichiers_pdf)}")
                    
            except ValueError:
                print("❌ Veuillez entrer un nombre valide ou 'q' pour quitter")
    
    def extraire_pdf(self, fichier_pdf):
        """Extrait le texte d'un fichier PDF"""
        try:
            print(f"\n📖 Extraction du fichier : {fichier_pdf}")
            with pdfplumber.open(fichier_pdf) as pdf:
                texte_complet = ""
                for i, page in enumerate(pdf.pages, 1):
                    print(f"   📄 Page {i}...")
                    texte_complet += page.extract_text() + "\n"
                print(f"✅ Extraction terminée ({len(pdf.pages)} pages)")
                return texte_complet
        except Exception as e:
            print(f"❌ Erreur lors de la lecture du PDF : {e}")
            return None
    
    def debug_contenu(self, texte):
        """Affiche le contenu pour debug"""
        print("\n🔍 CONTENU EXTRAIT (DEBUG)")
        print("=" * 50)
        lignes = texte.split('\n')
        for i, ligne in enumerate(lignes[:20]):  # Première 20 lignes
            if ligne.strip():
                print(f"{i+1:2d}: {ligne}")
        print("=" * 50)
        
        reponse = input("Voulez-vous voir tout le contenu ? (o/n) : ").strip().lower()
        if reponse in ['o', 'oui', 'y', 'yes']:
            print("\n📄 CONTENU COMPLET:")
            print("-" * 80)
            for i, ligne in enumerate(lignes):
                if ligne.strip():
                    print(f"{i+1:3d}: {ligne}")
            print("-" * 80)
    
    def parser_releve_sg(self, texte):
        """Parse un relevé Société Générale - Version adaptative"""
        lignes = texte.split('\n')
        transactions_trouvees = 0
        
        print("\n🔍 Recherche des transactions...")
        
        # Patterns multiples pour différents formats de relevé SG
        patterns = [
            # Format 1: 25/07 25/07 150,00- CARTE 250720 AUCHAN
            r'(\d{2}/\d{2})\s+(\d{2}/\d{2})\s+([\d,]+)([+-]?)\s+(.+)',
            # Format 2: 25/07 25/07    150,00 - CARTE 250720 AUCHAN
            r'(\d{2}/\d{2})\s+(\d{2}/\d{2})\s+([\d,]+)\s*([+-])\s*(.+)',
            # Format 3: avec espaces dans le montant
            r'(\d{2}/\d{2})\s+(\d{2}/\d{2})\s+([\d\s,]+)([+-]?)\s+(.+)',
            # Format 4: plus flexible
            r'(\d{1,2}/\d{1,2})\s+(\d{1,2}/\d{1,2})\s+([\d\s,.-]+)\s+(.+)'
        ]
        
        # Debug: montrer quelques lignes candidates
        print("📋 Lignes qui pourraient être des transactions:")
        lignes_candidates = []
        for i, ligne in enumerate(lignes):
            ligne = ligne.strip()
            if re.search(r'\d{2}/\d{2}', ligne) and len(ligne) > 15:
                lignes_candidates.append((i+1, ligne))
                if len(lignes_candidates) <= 5:  # Montrer les 5 premières
                    print(f"  {i+1:3d}: {ligne}")
        
        if not lignes_candidates:
            print("❌ Aucune ligne avec format date trouvée")
            self.debug_contenu(texte)
            return False
        
        # Essayer de parser avec chaque pattern
        for pattern_idx, pattern in enumerate(patterns):
            print(f"\n🔄 Test du pattern {pattern_idx + 1}...")
            transactions_temp = []
            
            for num_ligne, ligne in lignes_candidates:
                match = re.search(pattern, ligne)
                if match:
                    try:
                        if len(match.groups()) == 4:  # Pattern sans signe séparé
                            date_comptable = match.group(1)
                            date_valeur = match.group(2)
                            montant_str = match.group(3)
                            operation = match.group(4)
                            
                            # Détecter le signe dans le montant
                            if montant_str.endswith('-'):
                                montant_str = montant_str[:-1]
                                signe = '-'
                            elif montant_str.endswith('+'):
                                montant_str = montant_str[:-1]
                                signe = '+'
                            else:
                                signe = '+'
                        
                        elif len(match.groups()) == 5:  # Pattern avec signe séparé
                            date_comptable = match.group(1)
                            date_valeur = match.group(2)
                            montant_str = match.group(3)
                            signe = match.group(4) if match.group(4) else '+'
                            operation = match.group(5)
                        else:
                            continue
                        
                        # Nettoyer le montant
                        montant_str = montant_str.replace(' ', '').replace(',', '.')
                        
                        # Vérifier que c'est un nombre valide
                        if not re.match(r'^\d+\.?\d*$', montant_str):
                            continue
                        
                        montant = float(montant_str)
                        
                        # Appliquer le signe
                        if signe == '-':
                            montant_debit = montant
                            montant_credit = 0
                            montant_net = -montant
                        else:
                            montant_debit = 0
                            montant_credit = montant
                            montant_net = montant
                        
                        # Ajouter l'année courante aux dates
                        annee_courante = datetime.now().year
                        date_comptable_complete = f"{date_comptable}/{annee_courante}"
                        date_valeur_complete = f"{date_valeur}/{annee_courante}"
                        
                        # Catégoriser l'opération
                        categorie = self.categoriser_operation(operation)
                        
                        transaction = {
                            'date_comptable': date_comptable_complete,
                            'date_valeur': date_valeur_complete,
                            'operation': operation.strip(),
                            'montant_debit': montant_debit,
                            'montant_credit': montant_credit,
                            'montant_net': montant_net,
                            'categorie': categorie
                        }
                        
                        transactions_temp.append(transaction)
                        
                        if len(transactions_temp) <= 3:  # Debug: montrer les premières
                            print(f"   ✅ Ligne {num_ligne}: {date_comptable} | {montant_net:>8.2f}€ | {operation[:30]}...")
                    
                    except (ValueError, IndexError) as e:
                        continue
            
            if transactions_temp:
                print(f"✅ Pattern {pattern_idx + 1} a trouvé {len(transactions_temp)} transactions")
                self.transactions = transactions_temp
                transactions_trouvees = len(transactions_temp)
                break
            else:
                print(f"❌ Pattern {pattern_idx + 1} : aucune transaction trouvée")
        
        if transactions