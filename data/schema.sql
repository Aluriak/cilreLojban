--
-- schema.sql
--
-- Copyright (C) 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
--
--
-- Distributed under WTFPL terms
--
--            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
--                    Version 2, December 2004
--
-- Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
--
-- Everyone is permitted to copy and distribute verbatim or modified
-- copies of this license document, and changing it is allowed as long
-- as the name is changed.
--
--            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
--   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
--
--  0. You just DO WHAT THE FUCK YOU WANT TO.
--
--

-- DROPS
drop table if exists crossref;
drop table if exists dico;


-- CREATS
create table if not exists 'dico' (
    -- id is rowid
    gismu varchar(10) not null unique,
    rafsi varchar(20),
    english varchar(30),
    globalenglish varchar(30),
    definition text,
    unknown varchar(20),
    comment text
);

create table if not exists 'crossref' (
    -- id is rowid
    src integer,
    ref integer,
    foreign key(src) references(dico.rowid),
    foreign key(ref) references(dico.rowid)
);

-- vim:et
