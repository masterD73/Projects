# which region is the wealthiest
with num_region as (select region, count(*) student_num_region from studentinfo  where final_result IN ("Pass", "Distinction") group by region)


select region, imd_band, count(*) as num, student_num_region, round(count(*) / student_num_region * 100, 2) as percentage
from studentinfo
inner join num_region using(region)
where final_result IN ("Pass", "Distinction")
group by region, imd_band
order by imd_band, percentage DESC
