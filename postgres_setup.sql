DROP DATABASE IF EXISTS sync_db;
CREATE DATABASE sync_db;
\connect sync_db;

CREATE TABLE participant
(
    participant_id serial,
    admin_date     date,
    CONSTRAINT participant_pk PRIMARY KEY(participant_id)
);

CREATE TABLE tasktype
(
    task_id         serial,
    task_name       text,
    CONSTRAINT tasktype_pk PRIMARY KEY(tasktype_id)
);

CREATE TYPE stamp_type AS ENUM ('input', 'output', 'marker');
CREATE TYPE inst_type AS ENUM ('right', 'left', 'piano', 'other')

CREATE TABLE stamp
(
    stamp_id       serial,
    sequence       smallint   NOT NULL, --stamp count per particpant
    stamp_type     stamp_type NOT NULL,
    instrument     inst_type  NOT NULL,
    micros         bigint     NOT NULL,
    participant_id smallint   REFERENCES participant (participant_id)
    tasktype_id    smallint   REFERENCES task (tasktype_id)
    CONSTRAINT stamp_pk PRIMARY KEY(stamp_id)
);

CREATE TYPE order_isi   as ENUM ('500 first', '800 first')
CREATE TYPE order_tasktype as ENUM (1, 2, 3, 4, 5, 6)

CREATE TABLE taskadmin
(
    taskadmin_id   serial,
    order_isi      order_isi,
    order_tasktype order_tasktype,
    admin_notes    text,
    participant_id smallint  REFERENCES participant (participant_id)
    task_id        smallint  REFERENCES task (task_id)
    CONSTRAINT taskadmin_pk PRIMARY KEY(taskadmin_id)
);


-- Run with:
-- psql -f filename.sql