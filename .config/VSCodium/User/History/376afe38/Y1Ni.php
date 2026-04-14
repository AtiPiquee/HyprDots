<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>MyRecipies - Nouvelle Recette</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>
        <div class="logo">MyRecipies</div>
        <a href="index.php" class="btn-retour">Retour aux recettes</a>
    </nav>

    <div class="container">
        <h1>Ajouter une nouvelle recette</h1>
        
        <form action="ajouter-recette.php" method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label for="nom">Nom de la recette</label>
                <input type="text" id="nom" name="nom" required>
            </div>

            <div class="form-group">
                <label for="ingredients">Ingrédients</label>
                <textarea id="ingredients" name="ingredients" required></textarea>
            </div>

            <div class="form-group">
                <label for="etapes">Étapes de préparation</label>
                <textarea id="etapes" name="etapes" required></textarea>
            </div>

            <div class="form-group">
                <label for="images">Photos de la recette (plusieurs possibles)</label>
                <input type="file" id="images" name="images[]" accept="image/*" multiple>
            </div>

            <button type="submit" class="btn-submit">Ajouter la recette</button>
        </form>
    </div>
</body>
</html>