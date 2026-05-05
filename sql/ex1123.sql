with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select gender, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by gender;

with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select highest_education, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by highest_education;

with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select imd_band, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by imd_band;

with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select age_band, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by age_band;

with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select disability, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by disability;

with clicks as (select id_student, avg(sum_click) as average_clicks
from studentvle
group by id_student)

select region, avg(average_clicks) average_clicks
from studentinfo
inner join clicks
using(id_student)
group by region;