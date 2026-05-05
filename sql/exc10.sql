select a.code_module, b.code_module, a.code_presentation, b.code_presentation, count(*) as num_students
from studentregistration a
join  studentregistration b
using(id_student)
where a.date_unregistration is null and a.code_module < b.code_module and a.code_presentation != b.code_presentation
group by a.code_module,  b.code_module, a.code_presentation, b.code_presentation
order by num_students DESC;

select a.code_module, b.code_module, a.code_presentation, b.code_presentation, count(*) as num_students
from studentregistration a
join  studentregistration b
using(id_student)
where a.date_unregistration is null and a.code_module < b.code_module and a.code_presentation = b.code_presentation
group by a.code_module,  b.code_module, a.code_presentation, b.code_presentation
order by num_students DESC;