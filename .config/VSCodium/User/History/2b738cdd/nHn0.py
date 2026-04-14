def create_graph(statistics):
    """
    Crée et affiche un graphique à barres basé sur les statistiques.
    
    Args:
        statistics (List[Tuple[int, int, float]]): Liste de tuples (valeur, occurrences, pourcentage)
    
    Returns:
        None
    """
    try:
        import matplotlib.pyplot as plt
        
        # Extraire les données
        values = [stat[0] for stat in statistics]
        occurrences = [stat[1] for stat in statistics]
        percentages = [stat[2] for stat in statistics]
        
        # Créer le graphique à barres
        plt.figure(figsize=(10, 6))
        bars = plt.bar(values, occurrences, color='skyblue')
        
        # Ajouter les étiquettes et le titre
        plt.xlabel('Valeurs')
        plt.ylabel('Nombre d\'occurrences')
        plt.title('Distribution des valeurs générées')
        
        # Ajouter les pourcentages au-dessus des barres
        for bar, pct in zip(bars, percentages):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                    f'{pct}%', ha='center', va='bottom')
        
        # Ajuster les ticks de l'axe X pour montrer toutes les valeurs
        plt.xticks(values)
        
        # Afficher le graphique
        plt.tight_layout()
        plt.show()
    except ImportError:
        print("Pour générer des graphiques, vous devez installer matplotlib:")
        print("pip install matplotlib")