-- Criar tabelas
CREATE TABLE fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

CREATE TABLE ingredientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity FLOAT NOT NULL,
    unit VARCHAR(50) NOT NULL,
    min_stock FLOAT,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES fornecedores(id)
);

CREATE TABLE movimentacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_id INT,
    movement_type VARCHAR(50),
    quantity FLOAT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ingredient_id) REFERENCES ingredientes(id)
);

-- Inserir dados de exemplo
INSERT INTO fornecedores (name, contact, email) VALUES
    ('Doces & Cia', '555-0101', 'contato@doces.com'),
    ('Mestre das Farinhas', '555-0102', 'vendas@mestrefarinhas.com'),
    ('Laticicios Delicia', '555-0103', 'pedidos@laticinios.com'),
    ('Reino dos Doces', '555-0104', 'info@reinoacucar.com'),
    ('Paraiso das Nozes', '555-0105', 'vendas@paraisonozes.com'),
    ('Mundo do Chocolate', '555-0106', 'pedidos@mundochocolate.com');

INSERT INTO ingredientes (name, quantity, unit, min_stock, supplier_id) VALUES
    ('Farinha de Trigo', 100.0, 'kg', 20.0, 2),
    ('Acucar Refinado', 80.0, 'kg', 15.0, 4),
    ('Manteiga', 50.0, 'kg', 10.0, 3),
    ('Gotas de Chocolate', 30.0, 'kg', 8.0, 6),
    ('Amendoas', 25.0, 'kg', 5.0, 5),
    ('Essencia de Baunilha', 5.0, 'L', 1.0, 1),
    ('Fermento em Po', 10.0, 'kg', 2.0, 2),
    ('Creme de Leite', 40.0, 'L', 8.0, 3);

INSERT INTO movimentacoes (ingredient_id, movement_type, quantity) VALUES
    (1, 'ENTRADA', 100.0),
    (2, 'ENTRADA', 80.0),
    (3, 'SAÍDA', 5.0),
    (4, 'ENTRADA', 30.0),
    (5, 'SAÍDA', 2.0),
    (6, 'ENTRADA', 5.0);