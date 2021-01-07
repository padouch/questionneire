create table main.question_type
(
	"id" INTEGER
		constraint question_type_pk
			primary key autoincrement,
	q_type_name text,
	q_type_desc text