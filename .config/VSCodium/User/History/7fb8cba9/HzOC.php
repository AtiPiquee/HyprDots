<?php
// Fonction pour récupérer toutes les recettes
function getAllRecipes() {
    $recipes = [];
    $recipesDir = 'recipes/';
    
    if (is_dir($recipesDir)) {
        $recipesFolders = array_diff(scandir($recipesDir), ['..', '.']);
        
        foreach ($recipesFolders as $folder) {
            $jsonPath = $recipesDir . $folder . '/recipe.json';
            
            if (file_exists($jsonPath)) {
                $recipeData = json_decode(file_get_contents($jsonPath), true);
                $recipeData['folder'] = $folder;
                $recipes[] = $recipeData;
            }
        }
    }
    
    // Trie les recettes par date de création (les plus récentes en premier)
    usort($recipes, function($a, $b) {
        return strtotime($b['date_creation']) - strtotime($a['date_creation']);
    });
    
    return $recipes;
}

$recettes = getAllRecipes();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>MyRecipies - Mes Recettes</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>
        <div class="logo">MyRecipies</div>
        <a href="nouvelle-recette.php" class="btn-nouvelle-recette">Nouvelle Recette</a>
    </nav>

    <div class="container">
        <h1>Mes Recettes</h1>
        
        <div class="recettes-grid">
            <?php foreach ($recettes as $recette): ?>
                <div class="recette-card">
                    <?php if (!empty($recette['images'])): ?>
                        <img src="recipes/<?= htmlspecialchars($recette['folder']) ?>/<?= htmlspecialchars($recette['images'][0]) ?>" 
                             alt="<?= htmlspecialchars($recette['nom']) ?>">
                    <?php else: ?>
                        <img src="css/placeholder.jpg" alt="Pas d'image">
                    <?php endif; ?>
                    <h2><?= htmlspecialchars($recette['nom']) ?></h2>
                    <a href="details-recette.php?recipe=<?= urlencode($recette['folder']) ?>" class="btn-details">Voir la recette</a>
                </div>
            <?php endforeach; ?>
        </div>
    </div>
</body>
</html>