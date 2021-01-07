create table main.question_type
(
    id          INTEGER
        constraint question_type_pk
            primary key autoincrement,
    q_type_name text,
    q_type_desc text
);

create table main.question
(
	id INTEGER
		constraint question_pk
			primary key autoincrement,
	q_txt text,
	q_deleted text default f,
	q_aspect_id int,
	q_type_id int
);
