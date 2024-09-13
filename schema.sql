DROP TABLE IF EXISTS villes_france_free;
DROP TABLE IF EXISTS departement;

CREATE TABLE villes_france_free (
  ville_id INTEGER PRIMARY KEY,
  ville_departement VARCHAR3 DEFAULT NULL,
  ville_slug TEXT DEFAULT NULL,
  ville_nom TEXT DEFAULT NULL,
  ville_nom_simple TEXT DEFAULT NULL,
  ville_nom_reel TEXT DEFAULT NULL,
  ville_nom_soundex TEXT DEFAULT NULL,
  ville_nom_metaphone TEXT DEFAULT NULL,
  ville_code_postal TEXT DEFAULT NULL,
  ville_commune TEXT DEFAULT NULL,
  ville_code_commune TEXT DEFAULT NULL,
  ville_arrondissement INTEGER DEFAULT NULL,
  ville_canton TEXT DEFAULT NULL,
  ville_amdi INTEGER DEFAULT NULL,
  ville_population_2010 INTEGER DEFAULT NULL,
  ville_population_1999 INTEGER DEFAULT NULL, 
  ville_population_2012 INTEGER DEFAULT NULL, 
  ville_densite_2010 INTEGER DEFAULT NULL,
  ville_surface FLOAT DEFAULT NULL,
  ville_longitude_deg FLOAT DEFAULT NULL,
  ville_latitude_deg FLOAT DEFAULT NULL,
  ville_longitude_grd TEXT DEFAULT NULL, 
  ville_latitude_grd TEXT DEFAULT NULL, 
  ville_longitude_dms TEXT DEFAULT NULL,
  ville_latitude_dms TEXT DEFAULT NULL, 
  ville_zmin INTEGER DEFAULT NULL,
  ville_zmax INTEGER DEFAULT NULL
);

CREATE TABLE departement (
  departement_id INTEGER PRIMARY KEY,
  departement_code VARCHAR3 DEFAULT NULL,
  departement_nom TEXT DEFAULT NULL,
  departement_nom_uppercase TEXT DEFAULT NULL,
  departement_slug TEXT DEFAULT NULL,
  departement_nom_soundex TEXT DEFAULT NULL
);
