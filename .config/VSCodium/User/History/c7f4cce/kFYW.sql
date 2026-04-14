-- Table des utilisateurs
CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    mail VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Table des formulaires
CREATE TABLE form (
    id INT PRIMARY KEY AUTO_INCREMENT,
    form_name VARCHAR(100) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Table des questions
CREATE TABLE question (
    id INT PRIMARY KEY AUTO_INCREMENT,
    question TEXT NOT NULL,
    user_id INT NOT NULL,
    form_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (form_id) REFERENCES form(id) ON DELETE CASCADE
);
