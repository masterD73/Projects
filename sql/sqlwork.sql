# exc 6

with weighted_assignments as (select *, weight * score / 100 as work_score
from studentassessment
join assessments using (id_assessment)
where assessment_type NOT IN ('Exam')),

weighted_exams as (select *, weight * score / 100 as exam_score
from studentassessment
join assessments using (id_assessment)
where assessment_type IN ('Exam'))

select round((count(*) * sum(work_score * exam_score) - sum(work_score) * sum(exam_score)) / 
        (sqrt(count(*) * sum(work_score * work_score) - sum(work_score) * sum(work_score)) * sqrt(count(*) * sum(exam_score * exam_score) - sum(exam_score) * sum(exam_score))), 2) 
        AS correlation_coefficient_sample
    from weighted_assignments
    inner join weighted_exams using(id_student);

# exc 7

create view weighted_assignments as (select *, weight * score / 100 as work_score
from studentassessment
join assessments using (id_assessment)
where assessment_type NOT IN ('Exam'));

create view weighted_exams as (select *, weight * score / 100 as exam_score
from studentassessment
join assessments using (id_assessment)
where assessment_type IN ('Exam'));

create view total as (select id_student, e.code_presentation, work_score + exam_score as total_score
from weighted_exams as e
inner join weighted_assignments using(id_student));

create view total_averages as (select id_student, studied_credits, round(avg(total_score), 2) avg_student_score
from total
inner join studentinfo using (id_student)
group by id_student
order by id_student);

create view total_course_avg as (select id_student, studied_credits, round(avg(total_score), 2) avg_student_score
from total
inner join studentinfo using (id_student)
group by id_student
order by id_student);

select distinct round((count(*) * sum(t.studied_credits * avg_student_score) - sum(t.studied_credits) * sum(avg_student_score)) / 
        (sqrt(count(*) * sum(t.studied_credits * t.studied_credits) - sum(t.studied_credits) * sum(t.studied_credits)) * sqrt(count(*) * sum(avg_student_score * avg_student_score) - sum(avg_student_score) * sum(avg_student_score))), 2) 
        AS coeff_credits_score
    from total_averages as t
    inner join weighted_exams using(id_student)
    inner join studentinfo using(id_student)
    where final_result NOT IN('Withdrawn');
    
/* round((count(*) * sum(studied_credits * avg_student_score) - sum(studied_credits) * sum(avg_student_score)) / 
        (sqrt(count(*) * sum(studied_credits * studied_credits) - sum(studied_credits) * sum(studied_credits)) * sqrt(count(*) * sum(avg_student_score * avg_student_score) - sum(avg_student_score) * sum(avg_student_score))), 2) 
        AS coeff_credits_score */