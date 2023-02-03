-- 1. Вывести номера корпусов, если суммарный фонд финансирования расположенных в них кафедр превышает 13000000.
  select d.`building`
    from `departments` as d
group by d.`building`
  having sum(d.`financing`) > 13000000

-- 2. Вывести названия групп 5-го курса кафедры “Biotechnologies”, которые имеют более 35 пар в первую неделю.
  select g.`name`, group_concat(distinct d.`name`), count(*) as 'Lectures per week'
    from `departments` as d
    join `groups` as g
      on d.`id` = g.`department_id`
    join `groups_lectures` as gl
      on g.`id` = gl.`group_id`
    join `lectures` as l
      on gl.`lecture_id` = l.`id`
   where g.`year` = 5
     and d.`name` = 'Biotechnologies'
     and l.`date` >= '2022-09-01'
     and l.`date` <= '2022-09-08'
group by g.`name`
  having `Lectures per week` > 35

-- 3. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) больше, чем рейтинг группы “RG-032”.
with group_tmp as
    (select g.`name` as 'Group', round(avg(s.`rating`), 2) as 'Rating'
       from `groups` as g
	   join `groups_students` as gs
	     on g.`id` = gs.`group_id`
	   join `students` as s
		 on gs.`student_id` = s.`id`
   group by `Group`)

select `Group`, `Rating`
  from `group_tmp`
 where `Rating` > (select `Rating` from `group_tmp` where `Group` = 'RG-032')

-- 4. Вывести фамилии и имена преподавателей, ставка которых выше средней ставки профессоров.
  select t_.`name`, t_.`surname`
    from `teachers` as t_
   where t_.`salary` > (select avg(t.`salary`)
						  from `teachers` as t
						 where t.`is_professor` = 1
					  group by t.`is_professor`)
order by t_.`name`, t_.`surname`

-- 5. Вывести названия групп, у которых больше одного куратора.
  select g.`name` as 'Group'
    from `curators` as c
    join `groups_curators` as gc
      on c.`id` = gc.`group_id`
    join `groups` as g
      on gc.`group_id` = g.`id`
group by `Group`
  having count(*) > 1

-- 6. Вывести названия групп, имеющих рейтинг (средний рейтинг всех студентов группы) меньше, чем минимальный рейтинг групп 5-го курса.
  select g.`name` as 'Group'
    from `groups` as g
    join `groups_students` as gs
      on g.`id` = gs.`group_id`
    join `students` as s
      on gs.`student_id` = s.`id`
group by `Group`
  having avg(s.`rating`) < (select avg(s.`rating`) as 'Rating'
							  from `groups` as g
							  join `groups_students` as gs
					            on g.`id` = gs.`group_id`
							  join `students` as s
								on gs.`student_id` = s.`id`
							 where `g`.`year` = 5
						  group by g.`name`
						  order by `Rating`
							 limit 1)

-- 7. Вывести названия факультетов, суммарный фонд финансирования кафедр которых больше суммарного фонда финансирования кафедр факультета “Military Institute”.
  select f.`name`, sum(d.`financing`) as 'Financing'
    from `faculties` as f
    join `departments` as d
      on f.`id` = d.`faculty_id`
group by f.`name`
  having `Financing` > (select sum(d.`financing`)
						  from `faculties` as f
						  join `departments` as d
							on f.`id` = d.`faculty_id`
						 where f.`name` = 'School of Life Sciences'
					  group by f.`name`);

-- 8. Вывести названия дисциплин и полные имена преподавателей, читающих наибольшее количество лекций по ним.
with s1 as
(select s.`name` as 'Lecture name', concat_ws(' ', t.`name`, t.`surname`) as 'Full name', count(*) as 'Number lectures'
    from `teachers` as t
    join `lectures` as l
      on t.`id` = l.`teacher_id`
	join `subjects` as s
      on l.`subject_id` = s.`id`
group by `Lecture name`, `Full name`)

select s1.`Lecture name`, s1.`Full name`, s1.`Number lectures`
from s1
join (select `Lecture name`, max(`Number lectures`) as 'Max lectures' from s1 group by `Lecture name`) as s2
  on s1.`Lecture name` = s2.`Lecture name` and s1.`Number lectures` = s2.`Max lectures`

-- 9. Вывести название дисциплины, по которому читается меньше всего лекций.
  select count(l.`id`) as 'Minimum'
    from `subjects` as s
    join `lectures` as l
      on s.`id` = l.`subject_id`
group by s.`name`
order by `Minimum`
   limit 1

-- 10. Вывести количество студентов и читаемых дисциплин на кафедре “Laser Technologies”.
  select count(distinct concat_ws(' ', s.`name`, s.`surname`)) as 'Number of students ',
         count(distinct l.`subject_id`) as 'Number of lectures'
    from `departments` as d
    join `groups` as g
      on d.`id` = g.`department_id`
    join `groups_lectures` as gl
      on g.`id` = gl.`group_id`
    join `lectures` as l
      on gl.`lecture_id` = l.`id`
	join `groups_students` as gs
      on g.`id` = gs.`group_id`
	join `students` as s
      on gs.`student_id` = s.`id`
   where d.`name` = 'Laser Technologies'