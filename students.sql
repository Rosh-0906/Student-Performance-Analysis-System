create database details;
use details;
create table students (
	stud_name char(20), 
    stud_roll int, 
    sub_name char(20), 
    sub_mark int, 
    stud_atten int
);

insert into students (stud_name, stud_roll, sub_name, sub_mark, stud_atten) values 
	("Rajiv",101,"Maths",99,"77"),
    ("Gopal",102,"Python",90,"89"),
    ("John",103,"C++",79,"60"),
    ("Magg",104,"Java",60,"90"),
    ("Stephen",105,"SQL",85,"84")
;
select * from students;