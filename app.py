from flask import Flask, g, request, jsonify
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'your_database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('init-db')
def init_db_command():
    init_db()
    print('Database initialized.')

@app.route('/execute_sql')
def execute_sql():
    db = get_db()
    # Lire le fichier SQL
    with open('data_villes.sql', 'r') as file:
        sql_query = file.read()
    try:
        result = db.execute(sql_query).fetchall()
        print(result)  # Ajouter ceci pour voir le résultat brut dans la console
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 400
    # Retourner les résultats sous forme de JSON
    return jsonify([dict(row) for row in result])

@app.route('/table/<table_name>')
def show_table(table_name):
    db = get_db()
    try:
        # Exécuter la requête pour récupérer toutes les données de la table spécifiée
        query = f'SELECT * FROM {table_name}'
        rows = db.execute(query).fetchall()
        
        # Convertir les résultats en JSON
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400

@app.route('/api/departements')
def show_departements():
    db = get_db()
    try:
        query = f'SELECT * FROM departement'
        rows = db.execute(query).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/departements/<int:departement_id>')
def show_departements_id(departement_id):
    db = get_db()
    try:
        query = f'SELECT * FROM departement WHERE departement_id={departement_id}'
        rows = db.execute(query).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/departements/code/<string:departement_code>')
def show_departements_code(departement_code):
    db = get_db()
    try:
        query = f'SELECT * FROM departement WHERE departement_code={departement_code}'
        rows = db.execute(query).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/villes/nom/<string:ville_nom>')
def show_villes_nom(ville_nom):
    db = get_db()
    try:
        query = 'SELECT * FROM villes_france_free WHERE ville_nom = ?'
        rows = db.execute(query, (ville_nom,)).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/villes/code_postal/<string:code_postal>')
def show_villes_code_postal(code_postal):
    db = get_db()
    try:
        query = 'SELECT * FROM villes_france_free WHERE ville_code_postal = ?'
        rows = db.execute(query, (code_postal,)).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400
    
@app.route('/api/villes/population/<int:annee>/<int:population>')
def show_villes_population(annee, population):
    db = get_db()
    try:
        # Construire dynamiquement le nom de la colonne en utilisant le formatage de chaîne
        column_name = f'ville_population_{annee}'
        query = f'SELECT * FROM villes_france_free WHERE {column_name} >= ?'
        
        # Exécuter la requête en passant la population en tant que paramètre
        rows = db.execute(query, (population,)).fetchall()
        
        # Retourner les résultats sous forme de JSON
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table ou la colonne n'existe pas
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Gérer les autres erreurs potentielles
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/villes')
def show_villes():
    db = get_db()
    try:
        query = f'SELECT * FROM villes_france_free LIMIT 10'
        rows = db.execute(query).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400

@app.route('/api/villes/<int:ville_id>')
def show_villes_id(ville_id):
    db = get_db()
    try:
        query = f'SELECT * FROM villes_france_free WHERE ville_id = ?'
        rows = db.execute(query, (ville_id,)).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400

@app.route('/api/villes/departement/<string:departement_code>')
def show_villes_departement(departement_code):
    db = get_db()
    try:
        query = f'SELECT * FROM villes_france_free WHERE ville_departement = ?'
        rows = db.execute(query, (departement_code,)).fetchall()
        return jsonify([dict(row) for row in rows])
    except sqlite3.OperationalError as e:
        # Gérer le cas où la table n'existe pas
        return jsonify({"error": str(e)}), 400   

if __name__ == '__main__':
    app.run(debug=True)