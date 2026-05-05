-- select code_presentation, round(count(id_student) /
-- ((select count(*) from studentregistration where date_unregistration is null)
-- - (select count(*) as num_students
-- from studentinfo
-- where final_result = "Withdrawn"
-- group by code_presentation
-- order by code_presentation)) * 100, 2) as percentage_student
-- from studentregistration
-- where date_unregistration is null
-- group by code_presentation
-- order by code_presentation;
# how many active students are in each semester, which semester has the most students?
with semester_students as (select s.code_presentation as semester, count(*) as num_students
from studentregistration as s
left join studentinfo using(id_student)
where s.date_unregistration is null and final_result != "Withdrawn"
group by s.code_presentation
order by semester)

select *
from semester_students
