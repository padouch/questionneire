create table question_type
(
    id          serial not null
        constraint question_type_pk
            primary key,
    q_type_name text,
    q_type_desc text
);

alter table question_type
    owner to postgres;

create table question
(
    id          serial not null
        constraint question_pk
            primary key,
	q_txt text,
	q_deleted boolean default true,
	q_aspect_id int,
	q_type_id int
);

alter table question
    owner to postgres;

create table question_aspect
(
	id serial
		constraint question_aspect_pk
			primary key,
	q_aspect text not null
);
alter table question_aspect
    owner to postgres;