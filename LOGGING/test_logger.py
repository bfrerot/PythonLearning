import logging

# Configuration du format de log
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

# Configuration du logging avec niveau DEBUG pour capturer tous les messages
logging.basicConfig(
    level=logging.DEBUG, 
    filename='user_activity.log', 
    filemode='a', 
    format=FORMAT
)

# Récupération du logger
logger = logging.getLogger('UserLogger')

def log_user_input(user_message):
    """
    Génère un log en fonction du message de l'utilisateur
    """
    logger.info(f"Message reçu de l'utilisateur: {user_message}")
    
    # Logique simple pour démonstration
    if len(user_message) == 0:
        logger.warning("Message vide détecté!")
    elif len(user_message) > 100:
        logger.warning(f"Message très long ({len(user_message)} caractères)")
    elif "erreur" in user_message.lower():
        logger.error(f"Mot-clé 'erreur' détecté: {user_message}")
    elif "critique" in user_message.lower():
        logger.critical(f"Situation critique signalée: {user_message}")
    else:
        logger.debug(f"Message normal traité: {user_message[:50]}...")

# Programme principal
if __name__ == "__main__":
    print("=== Système de logging simple ===")
    print("Tapez vos messages (tapez 'quit' pour quitter)\n")
    
    while True:
        user_input = input("Votre message: ")
        
        if user_input.lower() == 'quit':
            logger.info("Programme terminé par l'utilisateur")
            print("\nLogs enregistrés dans 'user_activity.log'")
            break
        
        log_user_input(user_input)
        print("✓ Message enregistré dans le log\n")
