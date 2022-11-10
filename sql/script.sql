delimiter |

-- Impossible de réserver deux hotel pour un même jour et un même auteur

CREATE or replace trigger one_hotel_for_idp before insert on LOGER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idh int;
  declare jour date;
  select idP, idHotel, jourL into idp, idh, jour from LOGER where idP=new.idP;
  if idh != new.idHotel and jour = new.jourL then
    set mes = concat (' inscription impossible' , new.idHotel );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

CREATE or replace trigger one_hotel_for_idp_Update before update on LOGER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idh int;
  declare jour date;
  select idP, idHotel, jourL into idp, idh, jour from LOGER where idP=new.idP;
  if idh != new.idHotel and jour = new.jourL then
    set mes = concat (' inscription impossible' , new.idHotel );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- Impossible de réserver deux navette pour un même auteur

create or replace trigger one_transport_for_idp before insert on TRANSPORTER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idv int;
  select idP, idVoy into idp, idv from TRANSPORTER where idP=new.idP;
  if idv != new.idVoy then
    set mes = concat (' inscription impossible' , new.idVoy );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

create or replace trigger one_transport_for_idp_Update before update on TRANSPORTER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idv int;
  select idP, idVoy into idp, idv from TRANSPORTER where idP=new.idP;
  if idv != new.idVoy then
    set mes = concat (' inscription impossible' , new.idVoy );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- Un membre du staff ne peut pas faire deux travail en même temps

create or replace trigger just_one_job_for_staff before insert on TRAVAILLER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idc int;
  declare hdebut datetime;
  declare hfin datetime;
  declare newhdebut datetime;
  declare newhfin datetime;
  select idP, idCreneau into idp, idc from TRAVAILLER where idp=new.idp;
  select dateDebut, dateFin into hdebut, hfin from CRENEAU where idCreneau=idc;
  select dateDebut, dateFin into newhdebut, newhfin from CRENEAU where idCreneau=new.idCreneau;
  if hdebut<newhfin or hfin>newhdebut then
    set mes = concat (' inscription impossible' , new.idCreneau );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- Un auteur ne peut pas avoir deux créneau de dédicace qui se chevauche

create or replace trigger just_one_dedicace before insert on DEDICACER for each row
begin
  declare mes varchar(100);
  declare idp int;
  declare idc int;
  declare hdebut datetime;
  declare hfin datetime;
  declare newhdebut datetime;
  declare newhfin datetime;
  select idP, idCreneau into idp, idc from DEDICACER where idp=new.idp;
  select dateDebut, dateFin into hdebut, hfin from CRENEAU where idCreneau=idc;
  select dateDebut, dateFin into newhdebut, newhfin from CRENEAU where idCreneau=new.idCreneau;
  if hdebut<newhfin or hfin>newhdebut then
    set mes = concat (' inscription impossible' , new.idCreneau );
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- Un hotel ne peut pas accueillir plus d'intervenant que sa capacité maximal

create or replace trigger check_max_capacite_hotel before insert on LOGER for each row
begin
  declare mes varchar(200);
  declare capacite int;
  declare count_intervenant int;
  select count(idP) into count_intervenant from LOGER where idHotel=new.idHotel;
  select capaciteHotel into capacite from HOTEL where idHotel=new.idHotel;
  if capacite < count_intervenant then
    set mes = concat('Capacite maximal atteinte pour ', new.idHotel);
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- un voyage ne peut pas transporter plus d'intervenant qu'il n'a de place disponnible dans ses navettes

create or replace trigger check_max_capacite_voyage before insert on TRANSPORTER for each row
begin
  declare mes varchar(200);
  declare capacite int;
  declare count_intervenant int;
  select sum(capaciteNavette) into capacite from NAVETTE natural join VOYAGE where idVoy=new.idVoy;
  select count(idP) into count_intervenant from TRANSPORTER where idP=new.idP;
  if capacite < count_intervenant then
    set mes = concat('capacite maximal atteinte pour ', new.idVoy);
    signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
  end if;
end|

-- procedure qui retourne les auteurs qui n'ont pas de maison d'édition

create or replace procedure check_auteur()
begin
  declare res varchar(500) default '';
  declare nom varchar(42);
  declare idp int;
  declare finie boolean default false;
  declare auteurs cursor for
    select idP, nomP
      from AUTEUR natural join PERSONNE
        where idP not in(
          select idP
            from APPARTIENT
        );
  declare continue handler for not found set finie = true;
  open auteurs;
  while not finie do
    fetch auteurs into idp, nom;
    if not finie then
      set res = concat(res, ' ',idp, ' ', nom);
    end if;
  end while;
  close auteurs;
  select res;
end|

delimiter ;