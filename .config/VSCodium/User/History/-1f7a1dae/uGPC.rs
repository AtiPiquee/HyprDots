fn main() {
    let args: Vec<String> = env::args().collect();
    fun::file();  // Vérifier/créer le fichier

    if args.len() < 2 {
        fun::help();
        return;
    }

    match args[1].as_str() {
        "help" => fun::help(),
        "add" => {
            if args.len() < 3 {
                println!("Erreur: Veuillez spécifier une tâche à ajouter");
                return;
            }
            let task = &args[2];
            if let Err(e) = fun::add(task) {
                eprintln!("Erreur lors de l'ajout de la tâche: {}", e);
            }
        },
        "tasks" | "list" => {
            if let Err(e) = fun::tasks() {
                eprintln!("Erreur lors de l'affichage des tâches: {}", e);
            }
        },
        "done" => {
            if args.len() < 3 {
                println!("Erreur: Veuillez spécifier l'index de la tâche à marquer comme terminée");
                return;
            }
            let indices = args[2..].to_vec();
            if let Err(e) = fun::done(indices) {
                eprintln!("Erreur lors du marquage des tâches: {}", e);
            }
        },
        "rm" => {
            println!("Fonctionnalité de suppression non implémentée");
            // Vous pourriez implémenter cette fonction comme la fonction done()
        },
        _ => {
            println!("Commande inconnue: {}", args[1]);
            fun::help();
        }
    }
}