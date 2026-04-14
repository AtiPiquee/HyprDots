pub fn done(tasks: Vec<String>) -> io::Result<()> {
    let path_str = path();
    let path = Path::new(&path_str);
    
    // Lire toutes les lignes du fichier
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let mut lines: Vec<String> = reader.lines().collect::<Result<_, _>>()?;
    
    // Convertir les indices de tâches en entiers
    let mut i_tasks: Vec<usize> = vec![];
    for task in tasks {
        match task.parse::<usize>() {
            Ok(n) if n > 0 && n <= lines.len() => i_tasks.push(n - 1), // Ajustement pour l'indexation à partir de 0
            _ => println!("Index de tâche invalide: {}", task),
        }
    }
    
    // Marquer les tâches comme terminées
    for &idx in &i_tasks {
        if idx < lines.len() {
            let line = &lines[idx];
            if line.starts_with("[ ]") {
                lines[idx] = line.replacen("[ ]", "[*]", 1);
            }
        }
    }
    
    // Réécrire le fichier
    let mut file = File::create(path)?;
    for line in lines {
        writeln!(file, "{}", line)?;
    }
    
    Ok(())
}