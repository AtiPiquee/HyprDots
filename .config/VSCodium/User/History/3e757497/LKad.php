<?php
// Fonction pour créer un nom de dossier "URL-friendly"
function createSlug($text) {
    // Convertit les caractères accentués
    $text = iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $text);
    
    // Supprime les caractères non alphanumériques
    $text = preg_replace('/[^a-zA-Z0-9\s-]/', '', $text);
    
    // Remplace les espaces par des tirets
    $text = preg_replace('/\s+/', '-', $text);
    
    // Convertit en minuscules
    $text = strtolower(trim($text, '-'));
    
    return $text;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Nettoie et récupère les données du formulaire
    $nom = isset($_POST['nom']) ? trim($_POST['nom']) : '';
    $ingredients = isset($_POST['ingredients']) ? trim($_POST['ingredients']) : '';
    $etapes = isset($_POST['etapes']) ? trim($_POST['etapes']) : '';

    // Validation de base
    if (empty($nom)) {
        die("Le nom de la recette est obligatoire.");
    }

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
    if (!mkdir($recipeDir, 0777, true)) {
        die("Impossible de créer le dossier de la recette.");
    }

    // Gestion des images
    $images = [];
    if (!empty($_FILES['images']['name'][0])) {
        foreach ($_FILES['images']['name'] as $key => $name) {
            // Vérifie qu'un fichier a été uploadé sans erreur
            if (!empty($name) && $_FILES['images']['error'][$key] === UPLOAD_ERR_OK) {
                $tmpName = $_FILES['images']['tmp_name'][$key];
                
                // Nettoie le nom du fichier
                $cleanFileName = createSlug(pathinfo($name, PATHINFO_FILENAME));
                $imageExtension = strtolower(pathinfo($name, PATHINFO_EXTENSION));
                $imageFileName = $cleanFileName . '_' . uniqid() . '.' . $imageExtension;
                
                $uploadPath = $recipeDir . '/' . $imageFileName;
                
                // Vérifie et déplace le fichier uploadé
                if (is_uploaded_file($tmpName)) {
                    if (move_uploaded_file($tmpName, $uploadPath)) {
                        $images[] = $imageFileName;
                    } else {
                        error_log("Erreur de déplacement du fichier : " . $name);
                    }
                } else {
                    error_log("Fichier non uploadé correctement : " . $name);
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
    if (file_put_contents($jsonFile, json_encode($recipeData, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)) === false) {
        die("Impossible d'écrire le fichier JSON.");
    }

    // Redirection vers la page d'accueil
    header('Location: index.php');
    exit();
}
?>