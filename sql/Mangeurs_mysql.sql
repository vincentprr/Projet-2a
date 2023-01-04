SET foreign_key_checks = 0;
DROP TABLE IF EXISTS PERSONNE, CLE, MANGEUR, EXPOSANT, REGIME, AVOIR, INTERVENANT, STAFF, LOGER,
HOTEL, VOYAGE, NAVETTE, TRANSPORTER, RESTAURANT, REPAS, CRENEAU, TRAVAILLER, MAISON_EDITION, AUTEUR, DEDICACER, APPARTIENT, MANGER;
SET foreign_key_checks = 1;

CREATE TABLE PERSONNE(
    idP int unsigned auto_increment,
    nomP VARCHAR(42),
    prenomP VARCHAR(42),
    typeId tinyint,
    ddnP date,
    telP VARCHAR(11),
    emailP VARCHAR(42),
    mdpP VARCHAR(65),
    remarques text,
    useCar tinyint unsigned,
    PRIMARY KEY (idP)
) ;

CREATE TABLE CLE(
    cleActivation VARCHAR(42),
    PRIMARY KEY (cleActivation)
) ;

CREATE TABLE MANGEUR(
    idP int unsigned,
    PRIMARY KEY (idP)
) ;

CREATE TABLE EXPOSANT(
    idP int unsigned,
    numStand smallint unsigned,
    PRIMARY KEY (idP)
) ;

CREATE TABLE REGIME(
    idRegime int unsigned,
    nomRegime VARCHAR(42),
    PRIMARY KEY (idRegime)
) ;

CREATE TABLE AVOIR(
    idP int unsigned,
    idRegime int,
    PRIMARY KEY (idP, idRegime)
) ;

CREATE TABLE INTERVENANT(
    idP int unsigned,
    arrive datetime,
    depart datetime,
    PRIMARY KEY (idP)
) ;

CREATE TABLE STAFF(
    idP int unsigned,
    PRIMARY KEY (idP)
) ;

CREATE TABLE LOGER(
    idLog int unsigned,
    idP int unsigned,
    idHotel int unsigned,
    jourL date,
    PRIMARY KEY (idLog)
) ;

CREATE TABLE HOTEL(
    idHotel int unsigned,
    nomHotel VARCHAR(42),
    adresseHotel VARCHAR(42),
    telHotel varchar(11),
    mailHotel VARCHAR(42),
    capaciteHotel smallint unsigned,
    PRIMARY KEY (idHotel)
) ;

CREATE TABLE VOYAGE(
    idVoy int unsigned,
    heureDebVoy datetime,
    dureeVoy smallint,
    idNavette int unsigned,
    PRIMARY KEY (idVoy)
) ;

CREATE TABLE NAVETTE(
    idNavette int unsigned,
    capaciteNavette tinyint unsigned,
    PRIMARY KEY (idNavette)
) ;

CREATE TABLE TRANSPORTER (
    idVoy int unsigned,
    idP int unsigned,
    PRIMARY KEY (idVoy, idP)
) ;

CREATE TABLE RESTAURANT(
    idRest int unsigned,
    nomRest VARCHAR(42),
    idCreneauM int unsigned,
    idCreneauS int unsigned,
    PRIMARY KEY (idRest)
) ;

CREATE TABLE REPAS(
    idRepas int unsigned,
    jour date,
    estmidi VARCHAR(42),
    idRest int unsigned,
    PRIMARY KEY (idRepas)
) ;

CREATE TABLE CRENEAU(
    idCreneau int unsigned,
    dateDebut datetime,
    dateFin datetime,
    PRIMARY KEY (idCreneau)
) ;

CREATE TABLE TRAVAILLER(
    idCreneau int unsigned,
    idP int unsigned,
    PRIMARY KEY (idCreneau, idP)
) ;

CREATE TABLE MAISON_EDITION(
    idME int unsigned,
    nomME VARCHAR(42),
    numStand smallint unsigned,
    PRIMARY KEY (idME)
) ;

CREATE TABLE AUTEUR(
    idP int unsigned,
    PRIMARY KEY (idP)
) ;

CREATE TABLE DEDICACER(
    idP int unsigned,
    idCreneau int unsigned,
    PRIMARY KEY (idP, idCreneau)
) ;

CREATE TABLE APPARTIENT(
	idP int unsigned,
	idME int unsigned,
	PRIMARY KEY (idP, idME)
);

CREATE TABLE MANGER(
    idRepas int unsigned,
    idP int unsigned,
    PRIMARY KEY (idRepas, idP)
);

ALTER TABLE AVOIR ADD FOREIGN KEY (idP) REFERENCES MANGEUR(idP);
ALTER TABLE AVOIR ADD FOREIGN KEY (idRegime) REFERENCES REGIME(idRegime);
ALTER TABLE RESTAURANT ADD FOREIGN KEY (idCreneauM) REFERENCES CRENEAU(idCreneau);
ALTER TABLE RESTAURANT ADD FOREIGN KEY (idCreneauS) REFERENCES CRENEAU(idCreneau);
ALTER TABLE DEDICACER ADD FOREIGN KEY (idP) REFERENCES AUTEUR(idP);
ALTER TABLE DEDICACER ADD FOREIGN KEY (idCreneau) REFERENCES CRENEAU(idCreneau);
ALTER TABLE EXPOSANT ADD FOREIGN KEY (idP) REFERENCES PERSONNE(idP);
ALTER TABLE INTERVENANT ADD FOREIGN KEY (idP) REFERENCES MANGEUR(idP);
ALTER TABLE LOGER ADD FOREIGN KEY (idP) REFERENCES INTERVENANT(idP);
ALTER TABLE LOGER ADD FOREIGN KEY (idHotel) REFERENCES HOTEL(idHotel);
ALTER TABLE MANGEUR ADD FOREIGN KEY (idP) REFERENCES PERSONNE(idP);
ALTER TABLE STAFF ADD FOREIGN KEY (idP) REFERENCES MANGEUR(idP);
ALTER TABLE TRANSPORTER ADD FOREIGN KEY (idVoy) REFERENCES VOYAGE(idVoy);
ALTER TABLE TRANSPORTER ADD FOREIGN KEY (idP) REFERENCES INTERVENANT(idP);
ALTER TABLE TRAVAILLER ADD FOREIGN KEY (idCreneau) REFERENCES CRENEAU(idCreneau);
ALTER TABLE TRAVAILLER ADD FOREIGN KEY (idP) REFERENCES STAFF(idP);
ALTER TABLE VOYAGE ADD FOREIGN KEY (idNavette) REFERENCES NAVETTE(idNavette);
ALTER TABLE AUTEUR ADD FOREIGN KEY (idP) REFERENCES INTERVENANT(idP);
ALTER TABLE APPARTIENT ADD FOREIGN KEY (idP) REFERENCES INTERVENANT(idP);
ALTER TABLE APPARTIENT ADD FOREIGN KEY (idME) REFERENCES MAISON_EDITION(idME);
ALTER TABLE REPAS ADD FOREIGN KEY (idRest) REFERENCES RESTAURANT(idRest); --
ALTER TABLE MANGER ADD FOREIGN KEY (idRepas) REFERENCES REPAS(idRepas);
ALTER TABLE MANGER ADD FOREIGN KEY (idP) REFERENCES MANGEUR(idP);