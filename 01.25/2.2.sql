-- 1. Вывести количество преподавателей кафедры “Physics”.
select count(distinct t.`name`, t.`surname`) as 'Teachers'
  from `teachers` as t
  join `lectures` as l
    on t.`id` = l.`teacher_id`
  join `groups_lectures` as gl
    on l.`id` = gl.`lecture_id`
  join `groups` as g
    on gl.`group_id` = g.`id`
  join `departments` as d
    on g.`department_id` = d.`id`
 where d.`name` = 'Physics';

-- 2. Вывести количество лекций, которые читает преподаватель “Rigel Haney”.
select count(*) as 'Lectures'
  from `teachers` as t
  join `lectures` as l
    on t.`id` = l.`teacher_id`
 where t.`name` = 'Rigel' and t.`surname` = 'Haney';

-- 3. Вывести количество занятий, проводимых в корпусе “5”.
select count(*) as 'Lectures'
  from `departments` as d
  join `groups` as g
    on d.`id` = g.`department_id`
  join `groups_lectures` as gl
    on g.`id` = gl.`group_id`
  join `lectures` as l
    on gl.`lecture_id` = l.`id`
 where d.`building` = 5;

-- 4. Вывести номера корпусов и количество лекций, проводимых в них.
  select d.`building` as 'Building',
		 count(*) as 'Lectures'
    from `departments` as d
    join `groups` as g
      on d.`id` = g.`department_id`
	join `groups_lectures` as gl
      on g.`id` = gl.`group_id`
    join `lectures` as l
      on gl.`lecture_id` = l.`id`
group by `Building`
order by `Building`;

-- 5. Вывести количество студентов, посещающих лекции преподавателя “Vladimir Dalton”.
select count(*) as 'Students'
  from `students` as s
  join `groups_students` as gs
    on s.`id` = gs.`student_id`
  join `groups` as g
    on gs.`group_id` = g.`id`
  join `groups_lectures` as gl
    on g.`id` = gl.`group_id`
  join `lectures` as l
    on gl.`lecture_id` = l.`id`
  join `teachers` as t
    on l.`teacher_id` = t.`id`
 where t.`name` = 'Vladimir'
   and t.`surname` = 'Dalton';

-- 6. Вывести среднюю ставку преподавателей факультета “School of Computer Technologies and Control”.
select round(avg(t.`salary`)) as 'Average salary'
  from `faculties` as f
  join `departments` as d
    on f.`id` = d.`faculty_id`
  join `groups` as g
    on d.`id` = g.`department_id`
  join `groups_lectures` as gl
    on g.`id` = gl.`group_id`
  join `lectures` as l
    on gl.`lecture_id` = l.`id`
  join `teachers` as t
    on l.`teacher_id` = t.`id`
 where f.`name` = 'School of Computer Technologies and Control'

-- 7. Вывести минимальное и максимальное количество студентов среди всех групп.
select min(sub.`Stds_in_grp`) as 'Min', max(sub.`Stds_in_grp`) as 'Max'
  from (select count(*) as 'Stds_in_grp'
          from `groups` as g
          join `groups_students` as gs
            on g.`id` = gs.`group_id`
          join `students` as s
            on gs.`student_id` = s.`id`
      group by g.`name`) as sub

-- 8. Вывести средний фонд финансирования кафедр.
select round(avg(d.`financing`)) as 'Average financing'
  from `departments` as d;


-- 9. Вывести полные имена преподавателей и количество читаемых ими дисциплин.
  select concat_ws(' ', t.`name`, t.`surname`) as 'Teacher',
		 count(distinct s.`id`) as 'Subjects'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
    join `subjects` as s
      on l.`subject_id` = s.`id`
group by `Teacher`
order by `Teacher`;

-- 10. Вывести количество лекций в каждый день недели.
  select dayname(lectures.`date`) as 'Day of week',
		 count(*) as 'Lectures'
    from `lectures`
group by `Day of week`;

-- 11. Вывести номера корпусов и количество кафедр, чьи лекции в них читаются.
  select d.`building`, count(d.`name`) as 'Number of departments'
    from `departments` as d
group by d.`building`
order by d.`building`

-- 12. Вывести названия факультетов и количество дисциплин, которые на них читаются.
  select f.`name` as 'Faculty',
		 count(distinct s.`id`) as 'Subjects'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
	join `groups` as g
      on d.`id` = g.`department_id`
	join `groups_lectures` as gl
      on g.`id` = gl.`group_id`
	join `lectures` as l
      on gl.`lecture_id` = l.`id`
    join `subjects` as s
	  on l.`subject_id` = s.`id`
group by `Faculty`;

-- 13. Вывести количество лекций для каждой пары преподаватель-аудитория.
  select concat(t.`name`, ' ', t.`surname`, ' - ', d. `building`) as 'Teacher - building',
		 count(*) as 'Lectures'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
	join `groups_lectures` as gl
      on l.`id` = gl.`lecture_id`
	join `groups` as g
      on gl.`group_id` = g.`id`
	join `departments` as d
      on g.`department_id` = d.`id`
group by `Teacher - building`
order by `Teacher - building`;