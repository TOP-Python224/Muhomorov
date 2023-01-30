-- 1. Вывести все возможные пары строк преподавателей и групп.
select distinct
	   `teachers`.`name`,
	   `teachers`.`surname`,
       `groups`.`name` as 'group_name'
  from `teachers`
  join `lectures`
    on `teachers`.`id` = `lectures`.`teacher_id`
  join `groups_lectures`
	on `lectures`.`id` = `groups_lectures`.`lecture_id`
  join `groups`
    on `groups_lectures`.`group_id` = `groups`.`id`;

-- 2. Вывести названия факультетов, фонд финансирования кафедр которых превышает фонд финансирования факультета.
select `faculties`.`name`
  from `faculties`
  join `departments`
    on `departments`.`faculty_id` = `faculties`.`id`
 where `departments`.`financing` > `faculties`.`financing`;

-- 3. Вывести фамилии кураторов групп и названия групп, которые они курируют.
select `curators`.`surname`,
	   `groups`.`name`
  from `curators`
  join `groups_curators`
    on `curators`.`id` = `groups_curators`.`curator_id`
  join `groups`
    on `groups_curators`.`group_id` = `groups`.`id`;

-- 4. Вывести имена и фамилии преподавателей, которые читают лекции у группы “PI-031”.
select distinct
       `teachers`.`name`,
	   `teachers`.`surname`
  from `teachers`
  join `lectures`
    on `teachers`.`id` = `lectures`.`teacher_id`
  join `groups_lectures`
    on `lectures`.`id` = `groups_lectures`.`lecture_id`
  join `groups`
    on `groups_lectures`.`group_id` = `groups`.`id`
 where `groups`.`name` = 'PI-031';

-- 5. Вывести фамилии преподавателей и названия факультетов, на которых они читают лекции.
select `teachers`.`surname`,
	   `faculties`.`name`
  from `teachers`
  join `lectures`
    on `teachers`.`id` = `lectures`.`teacher_id`
  join `groups_lectures`
    on `lectures`.`id` = `groups_lectures`.`lecture_id`
  join `groups`
    on `groups_lectures`.`id` = `groups`.`id`
  join `departments`
    on `groups`.`department_id` = `departments`.`id`
  join `faculties`
    on `departments`.`faculty_id` = `faculties`.`id`;

-- 6. Вывести названия кафедр и названия групп, которые к ним относятся.
select `departments`.`name` as 'dep_name',
	   `groups`.`name` as 'group_name'
  from `departments`
  join `groups`
    on `departments`.`id` = `groups`.`department_id`;

-- 7. Вывести названия дисциплин, которые читает преподаватель “Suki Martinez”.
select distinct
       `subjects`.`name`
  from `teachers`
  join `lectures`
    on `teachers`.`id` = `lectures`.`teacher_id`
  join `subjects`
    on `lectures`.`subject_id` = `subjects`.`id`
 where `teachers`.`name` = 'Suki'
   and `teachers`.`surname` = 'Martinez';

-- 8. Вывести названия кафедр, на которых читается дисциплина “Magna Duis”.
select distinct
	   `departments`.`name`
  from `departments`
  join `groups`
    on `departments`.`id` = `groups`.`department_id`
  join `groups_lectures`
    on `groups`.`id` = `groups_lectures`.`group_id`
  join `lectures`
    on `groups_lectures`.`lecture_id` = `lectures`.`id`
  join `subjects`
    on `lectures`.`subject_id` = `subjects`.`id`
 where `subjects`.`name` = 'Magna Duis';

-- 9. Вывести названия групп, которые относятся к факультету “School of Life Sciences”.
select `groups`.`name`
  from `groups`
  join `departments`
    on `groups`.`department_id` = `departments`.`id`
  join `faculties`
    on `departments`.`faculty_id` = `faculties`.`id`
 where `faculties`.`name` = 'School of Life Sciences';

-- 10. Вывести названия групп 5-го курса, а также название факультетов, к которым они относятся.
select `groups`.`name` as 'group_name',
	   `faculties`.`name` as 'faculty_name'
  from `groups`
  join `departments`
    on `groups`.`department_id` = `departments`.`id`
  join `faculties`
    on `departments`.`faculty_id` = `faculties`.`id`
 where `groups`.`year` = 5;

-- 11. Вывести полные имена преподавателей и лекции, которые они читают (названия дисциплин и групп), причем отобрать только те лекции, которые читаются в здании 3.
select concat_ws(' ', `teachers`.`name`, `teachers`.`surname`) as `full_name`,
	   `subjects`.`name` as 'subject_name' ,
       `groups`.`name` as 'group_name'
  from `teachers`
  join `lectures`
    on `teachers`.`id` = `lectures`.`teacher_id`
  join `subjects`
    on `lectures`.`subject_id` = `subjects`.`id`
  join `groups_lectures`
    on `lectures`.`id` = `groups_lectures`.`lecture_id`
  join `groups`
    on `groups_lectures`.`group_id` = `groups`.`id`
  join `departments`
    on `groups`.`department_id` = `departments`.`id`
 where `departments`.`building` = 3;

