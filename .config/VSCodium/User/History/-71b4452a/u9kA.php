<?php
// Vérifie que le paramètre de recette est présent
if (!isset($_GET['recipe'])) {
    header('Location: index.php');
    exit();
}

$recipeFolder = 'recipes/' . urldecode($_GET['recipe']);
$jsonPath = $recipeFolder . '/recipe.json';

// Vérifie l'existence du fichier JSON
if (!file_exists($jsonPath)) {
    header('Location: index.php');
    exit();
}

// Charge les données de la recette
$recette = json_decode(file_get_contents($jsonPath), true);
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>MyRecipies - <?= htmlspecialchars($recette['nom']) ?></title>
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <nav>
        <div class="logo">MyRecipies</div>
        <a href="index.php" class="btn-retour">Retour aux recettes</a>
    </nav>

    <div class="container">
        <h1><?= htmlspecialchars($recette['nom']) ?></h1>
        
        <div class="recette-details">
            <div class="recette-images">
                <?php foreach ($recette['images'] as $image): ?>
                    <img src="recipes/<?= urlencode($_GET['recipe']) ?>/<?= htmlspecialchars($image) ?>" 
                         alt="Photo de la recette">
                <?php endforeach; ?>
            </div>

            <div class="recette-infos">
                <h2>Ingrédients</h2>
                <pre><?= htmlspecialchars($recette['ingredients']) ?></pre>

                <h2>Étapes de préparation</h2>
                <pre><?= htmlspecialchars($recette['etapes']) ?></pre>
            </div>
        </div>
    </div>
</body>
</html>