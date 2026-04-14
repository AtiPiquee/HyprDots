<?php
// Fonction pour créer un nom de dossier "URL-friendly"
function createSlug($text) {
    // Convertit les caractères accentués
    $text = iconv('UTF-8', 'ASCII//TRANSLIT', $text);
    
    // Supprime les caractères non alphanumériques
    $text = preg_replace('/[^a-zA-Z0-9\s]/', '', $text);
    
    // Remplace les espaces par des tirets
    $text = str_replace(' ', '-', $text);
    
    // Convertit en minuscules
    $text = strtolower($text);
    
    return $text;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom = $_POST['nom'];
    $ingredients = $_POST['ingredients'];
    $etapes = $_POST['etapes'];

    // Création du dossier pour la recette
    $recipeSlug = createSlug($nom);
    $recipeDir = 'recipes/' . $nom;
    
    // Vérifie si le dossier n'existe pas déjà
    $counter = 1;
    while (file_exists($recipeDir)) {
        $recipeDir = 'recipes/' . $nom . '-' . $counter;
        $recipeSlug = createSlug($nom . '-' . $counter);
        $counter++;
    }
    
    // Crée le dossier de la recette
    mkdir($recipeDir, 0777, true);

    // Gestion des images
    $images = [];
    if (!empty($_FILES['images']['name'][0])) {
        foreach ($_FILES['images']['name'] as $key => $name) {
            if ($_FILES['images']['error'][$key] === UPLOAD_ERR_OK) {
                $tmpName = $_FILES['images']['tmp_name'][$key];
                $imageFileName = uniqid() . '_' . $name;
                $uploadPath = $recipeDir . '/' . $imageFileName;
                
                if (move_uploaded_file($tmpName, $uploadPath)) {
                    $images[] = $imageFileName;
                }
            }
        }
    }

    // Prépare les données de la recette
    $recipeData = [
        'nom' => $nom,
        'ingredients' => $ingredients,
        'etapes' => $etapes,
        'images' => $images,
        'date_creation' => date('Y-m-d H:i:s')
    ];

    // Enregistre les données dans un fichier JSON
    $jsonFile = $recipeDir . '/recipe.json';
    file_put_contents($jsonFile, json_encode($recipeData, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

    // Redirection vers la page d'accueil
    header('Location: index.php');
    exit();
}
?>