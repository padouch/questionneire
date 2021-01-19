create table if not exists question_type
(
    id          serial not null
        constraint question_type_pk
            primary key,
    q_type_name text,
    q_type_desc text
);

alter table question_type
    owner to postgres;

create table if not exists question
(
    id          serial not null
        constraint question_pk
            primary key,
    q_txt       text,
    q_deleted   boolean default true,
    q_aspect_id integer,
    q_type_id   integer
);

alter table question
    owner to postgres;

create table if not exists question_aspect
(
    id       serial not null
        constraint question_aspect_pk
            primary key,
    q_aspect text   not null
);

alter table question_aspect
    owner to postgres;

create table if not exists question_lab
(
    id          serial not null
        constraint question_lab_pk
            primary key,
    q_txt       text,
    q_deleted   boolean default true,
    q_aspect_id integer,
    q_type_id   integer
);

alter table question_lab
    owner to postgres;

create table if not exists answer
(
    id          serial not null
        constraint answer_pk
            primary key,
    answer_text text
);

alter table answer
    owner to postgres;

create table if not exists question_answer
(
    id          serial not null
        constraint question_answer_pk
            primary key,
    answer_id   integer,
    qusetion_id integer
);

alter table question_answer
    owner to postgres;

