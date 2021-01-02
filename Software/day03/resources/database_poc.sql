--
-- SOFTWARE Pool day 03 - Morning
-- PoC Database
-- Made with <3 by PoC
--

--
-- Name: pole; Type: TYPE; Schema: -; Owner: -
--

CREATE TYPE poles AS ENUM (
    'IA',
    'Software',
    'Security',
    'Hardware',
    'Health',
    'AR/VR'
);


--
-- Name: role; Type: TYPE; Schema: -; Owner: -
--

CREATE TYPE roles AS ENUM (
    'manager',
    'resident'
);


--
-- Name: status; Type: TYPE; Schema: -; Owner: -
--

CREATE TYPE status AS ENUM (
    'todo',
    'in progress',
    'done'
);


--
-- Name: Member; Type: TABLE; Schema: -; Owner: -
--

create table Members
(
    id    serial not null
        constraint member_pkey
            primary key,
    name  varchar(32),
    email varchar(250),
    role  roles default 'resident'::roles
);

--
-- Name: Project; Type: TABLE; Schema: -; Owner: -
--

create table Projects
(
    id     serial not null
        constraint project_pkey
            primary key,
    name   varchar(32),
    pole   poles,
    status status default 'todo'::status
);

--
-- Name: MemberProjectRelation; Type: TABLE; Schema: -; Owner: -
--

create table MemberProjectRelation
(
    memberid  integer not null
        constraint memberprojectrelation_memberid_fkey
            references Members,
    projectid integer not null
        constraint memberprojectrelation_projectid_fkey
            references Projects,
    constraint memberprojectrelation_memberid_projectid_key
        unique (memberid, projectid)
);


--
-- Insert data
--

--
-- Insert Projects
--
INSERT INTO projects (id, name, pole, status) VALUES (1, 'Hexapod', 'Hardware', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (2, 'PoC-AV', 'Security', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (8, 'PoC-TF', 'Security', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (9, 'Researchshare', 'Software', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (10, 'PoC2Peer', 'Software', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (11, 'SmartVote', 'Software', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (12, 'InMoov', 'Hardware', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (13, 'Escape-VR', 'AR/VR', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (14, 'Urban Guide', 'Health', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (15, 'Mind', 'Health', 'in progress');
INSERT INTO projects (id, name, pole, status) VALUES (16, 'SmartPoêle', 'Hardware', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (17, 'UglyDetector', 'Hardware', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (18, 'PoCZero', 'IA', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (21, 'PoCRocket', 'Hardware', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (22, 'Chaussette', 'Software', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (23, 'SkateGlider', 'Hardware', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (24, 'WhiteComet', 'Security', 'done');
INSERT INTO projects (id, name, pole, status) VALUES (25, 'BlackComet', 'Security', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (26, 'PoCovid', 'Health', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (27, 'BlackMirror', 'Hardware', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (28, 'CastleMind', 'AR/VR', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (29, 'IntraPoC', 'Software', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (30, 'Poggle', 'Software', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (31, 'Twytch', 'Software', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (32, 'LaSalle', 'AR/VR', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (33, 'Patoche', 'IA', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (34, 'GrobG4', 'Security', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (35, 'Yoda', 'AR/VR', 'todo');
INSERT INTO projects (id, name, pole, status) VALUES (36, 'PoCWar', 'Software', 'done');
INSERT INTO projects (id, name, pole, status) VALUES (37, 'Roublard', 'IA', 'todo');

--
-- Insert Members
--
INSERT INTO members (id, name, email, role) VALUES (1, 'Tom', 'tom.vasek@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (3, 'Luca', 'petit.lucas@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (4, 'Valentin', 'octonauts.nemo@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (5, 'Coline', 'cleopatre.moov@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (6, 'Loic', 'loic.champion@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (7, 'Paul', 'pol.fleekx@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (8, 'Cyril', 'cyril.tourne-vis@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (9, 'Maxime', 'lord.corbinouze@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (11, 'Naoufel', 'naoufel.marabou@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (13, 'Lorenzo', 'lorenzo.becker@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (12, 'Lucie', 'lucie.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (14, 'Quentin', 'quentin.francois@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (15, 'Jerome', 'jerome.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (16, 'Theo', 'theo.libelule@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (18, 'Thomas', 'thomas.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (17, 'Gregoire', 'gregoire.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (19, 'Quentin', 'quentin.marabou@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (20, 'Romain', 'romain.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (21, 'Killian', 'killian.mc-gregor@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (22, 'Alexandre', 'alexandre.trading@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (23, 'Edouard', 'edouard.game@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (24, 'Theo', 'theo.magicien@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (25, 'Damien', 'damien.hobbit@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (26, 'Guillaume', 'guillaume.beau-gosse.charo.tacleur.tchatcheur@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (27, 'Roman', 'roman.bruel@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (28, 'Paul', 'paul.english@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (29, 'Ugo', 'ugo.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (30, 'Yohann', 'yohann.hexapod@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (31, 'Allan', 'allan.the@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (32, 'Matthis', 'mathis.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (33, 'Lucas', 'luca.ekip.boss@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (34, 'Timothée', 'timothée.gemini@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (35, 'Noé', 'noé.gemini@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (2, 'Alexandre', 'lord.alexandre.naturel@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (36, 'Bibas', 'bibas.le-s@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (37, 'Gabriel', 'gabriel.martin@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (38, 'Jeremy', 'jeremy.le-vilain@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (39, 'Theo', 'theo.zoupoutoux@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (40, 'Laurane', 'laurane.martin@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (41, 'Clement', 'clement.martin@epitech.eu', 'manager');
INSERT INTO members (id, name, email, role) VALUES (42, 'Robin', 'robin.lisse@epitech.eu', 'resident');
INSERT INTO members (id, name, email, role) VALUES (10, 'Slohan', 'slo.soin.tu-tournes@epitech.eu', 'manager');

--
-- Insert relation
--
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 29);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 10);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 11);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 2);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 8);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 22);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 24);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 36);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 37);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 9);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 11);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 13);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 28);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (4, 15);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (4, 18);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 18);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (4, 33);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (8, 1);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 1);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (13, 1);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (30, 1);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 2);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (21, 2);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (23, 2);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (21, 8);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (13, 8);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (22, 9);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (19, 9);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (32, 9);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (17, 10);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (25, 10);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (9, 10);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (14, 11);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 12);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (8, 12);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (5, 12);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (15, 12);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (7, 10);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (20, 13);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (16, 13);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (31, 13);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 14);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (5, 14);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (28, 15);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (27, 15);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 16);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (29, 16);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (31, 16);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (4, 17);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 17);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 17);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (42, 18);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 37);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (30, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (24, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (19, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (21, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (28, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 22);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (9, 22);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 23);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (23, 23);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (39, 23);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (39, 21);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 24);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (20, 24);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (23, 24);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (41, 27);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (40, 27);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (33, 27);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (34, 27);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (35, 27);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 28);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 28);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 28);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (38, 28);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 29);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 29);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (15, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (12, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (10, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (26, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (21, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 30);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 31);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (34, 31);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (35, 31);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (37, 31);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (38, 31);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (2, 32);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (3, 32);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (11, 32);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 32);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (5, 33);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (10, 33);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (25, 33);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (28, 33);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (1, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (24, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (6, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (21, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (27, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (16, 34);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (15, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (36, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (26, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (30, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (33, 35);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (15, 36);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (24, 36);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (42, 36);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (20, 36);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (13, 37);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (29, 37);
INSERT INTO memberprojectrelation (memberid, projectid) VALUES (33, 37);
