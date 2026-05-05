select activity_type, round(avg(avg_student_score), 2) as avg_score
from studentvle as sv
inner join vle as v
using(id_site)
inner join total_averages as t
on t.id_student = sv.id_student and v.code_module = sv.code_module and v.code_presentation = sv.code_presentation
group by activity_type
order by avg_score desc