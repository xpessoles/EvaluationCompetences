BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "competences_eleves" (
	"id_eleve"	INTEGER,
	"id_evaluation"	INTEGER,
	"id_comp"	INTEGER,
	"score"	TEXT,
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE IF NOT EXISTS "evaluations_eleves" (
	"id_eleve"	INTEGER,
	"id_evaluation"	INTEGER,
	"note_brute_sur20"	REAL,
	"note_traitee_sur20"	REAL,
	"note_harmo_sur20"	REAL,
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT
);
CREATE TABLE IF NOT EXISTS "questions_eleves" (
	"id_eleve"	INTEGER,
	"id_eval"	INTEGER,
	"id_question"	INTEGER,
	"note_question"	TEXT²
);
CREATE TABLE IF NOT EXISTS "commentaires_eleves" (
	"id_eleve"	INTEGER,
	"id_eval"	INTEGER,
	"commentaire"	TEXT
);
CREATE TABLE IF NOT EXISTS "questions" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"id_eval"	INTEGER,
	"num_ques"	INTEGER,
	"id_comp"	INTEGER,
	"note_ques"	INTEGER,
	"poids_comp"	INTEGER,
	"nom"	TEXT,
	"index_question"	INTEGER
);
CREATE TABLE IF NOT EXISTS "eleves" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"nom"	TEXT,
	"prenom"	TEXT,
	"num"	INTEGER,
	"num_ano"	TEXT,
	"annee"	INTEGER,
	"classe"	TEXT,
	"mail"	TEXT
);
CREATE TABLE IF NOT EXISTS "evaluations" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"type"	TEXT,
	"date"	TEXT,
	"classe"	TEXT,
	"numero"	INTEGER,
	"annee"	INTEGER
);
CREATE TABLE IF NOT EXISTS "competences" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"discipline"	TEXT,
	"filiere"	TEXT,
	"code"	TEXT,
	"nom_long"	TEXT,
	"nom_court"	TEXT,
	"semestre"	INTEGER
);
COMMIT;
