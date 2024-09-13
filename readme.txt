OBJECTIFS :
- Comprendre plusieurs concepts et compétences fondamentales en gestion de bases de données et en SQL
- Maîtriser des compétences et des connaissances essentielles dans le développement du web en Python.

CONSIGNE : 

Dans la suite des notions abordées en cours, où nous avons créé des routes pour répondre à des requêtes clients, ce projet  s’inscrit dans la continuité de ce travail.

Les liens suivants sont les routes de votre serveur web qui permettent de récupérer les informations de la base de données. 

Vous devez créer la base de données pour accueillir les données dans un fichier que vous trouverez sur ce lien

Créer les routes pour les actions suivantes :

    GET /api/departements : Récupérer tous les départements.
    GET /api/departements/<int:departement_id> : Récupérer un département spécifique par son ID.
    GET /api/departements/code/<string:departement_code> : Récupérer un département par son code.
    GET /api/villes/nom/<string:ville_nom> : Récupérer les villes par nom.
    GET /api/villes/code_postal/<string:code_postal> : Récupérer les villes par code postal.
    GET /api/villes/population/<int:annee>/<int:population> : Récupérer les villes avec une population supérieure ou égale à une valeur spécifiée pour l'année spécifiée.
    GET /api/villes : Récupérer une liste limitée de villes (les 10 premières).
    GET /api/villes/<int:ville_id> : Récupérer une ville spécifique par son ID.
    GET /api/villes/departement/<string:departement_code> : Récupérer toutes les villes appartenant à un département spécifique par son code.

 

Cette API REST en Flask permet de récupérer des données des tables departement et villes sous forme de JSON.