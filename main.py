# print("Entrez une valeur")
# compteur = int(input())
# for i in range(compteur):
#     print(i)

# print("Entrez un chiffre pour avoir sa table de multiplication")
# chiffre = int(input())
# for i in range(11):
#     print(i,"*",chiffre,"=",i*chiffre)

# for i in range(1,101):
#     if ((i % 3 == 0) and (i % 5 == 0)):
#         print("fizzbuzz")
#     elif(i % 3 == 0):
#         print("fizz")
#     elif(i % 5 ==0):
#         print("buzz")
#     else: print(i)
from flask import Flask, request

app = Flask(__name__)

data = [
    { "id": 1, "nom": "Pickles", "prenom": "Angelica", "ville": "Cesson-Sévigné" },
    { "id": 2, "nom": "Pickles", "prenom": "Tommy", "ville": "Saint-Grégoire" },
    { "id": 3, "nom": "Finster", "prenom": "Chuckie", "ville": "Betton" },
    { "id": 4, "nom": "DeVille", "prenom": "Phil", "ville": "Chantepie" },
    { "id": 5, "nom": "DeVille", "prenom": "Lil", "ville": "Pacé" },
    { "id": 6, "nom": "Carmichael", "prenom": "Susie", "ville": "Vezin-le-Coquet" }
]

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/profil/<user>')
def profil(user):
    return f"<p>Profile de {user} !</p>"

@app.route('/search')
def recherche():
    q = request.args.get('q', default="")
    return f"On recherche {q}"

@app.route('/users/<int:user_id>')
def search_user(user_id):
    for i in data:
        if(i["id"]==user_id):
            return f"L'utilisateur {i["nom"]} {i["prenom"]} vient de {i["ville"]}."
        
# @app.route('/users')
# def search_all_users():
#     q= request.args.get('q',default="")
#     results=[]
#     if(q==""):
#         return data
#     else:
#         for row in data:
#             if((q==row["id"]) or (q==row["nom"]) or (q==row["prenom"]) or (q==row["ville"])):
#                 results.append(row)
#         return results

@app.route('/users')
def search_all_users():
    results=[]

    if len(request.args) == 0:
            return data
    else: 
        for key,value in request.args.items():
            for row in data:
                if row[key] == value:
                    results.append(row)
        return results
    
# @app.route('/chat')
# def chat():
#     query_params = request.args.to_dict()
    
#     # Si aucun paramètre n'est passé, renvoyer toutes les données
#     if not query_params:
#         return str(data)

#     results = []
#     for row in data:
#         match = True
#         for key, value in query_params.items():
#             if key not in row or str(row[key]) != value:
#                 match = False
#                 break
#         if match:
#             results.append(row)
    
#     if results:
#         return str(results)
#     else:
#         return "Aucun résultat trouvé", 404

@app.route('/users')
def fetch_users():
    
    query_params = request.args.to_dict()
    print(query_params)

    results = []
    if len(request.args) == 0: return data
    for row in data:
        #Permet de caster notre id en string
        row['id'] = str(row['id'])
        # La flèche <= permet de vérifier que le dictionnaire de paramètre est contenu dans notre ligne
        if query_params.items() <= row.items():
            results.append(row)
    return results