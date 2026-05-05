select gender, round(avg(avg_student_score), 2)
from total_averages
inner join studentinfo using (id_student)
group by gender;

select region, round(avg(avg_student_score), 2)
from total_averages
inner join studentinfo using (id_student)
group by region;


select imd_band, avg(avg_student_score)
from total_averages
inner join studentinfo using (id_student)
group by imd_band;

select age_band, avg(avg_student_score)
from total_averages
inner join studentinfo using (id_student)
group by age_band;

select disability, avg(avg_student_score)
from total_averages
inner join studentinfo using (id_student)
group by disability;

