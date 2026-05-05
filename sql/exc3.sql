CREATE DATABASE IF NOT EXISTS university;
# Module Presentation
CREATE TABLE IF NOT EXISTS courses (
code_module varchar(45),
code_presentation varchar(45),
module_presentation_length varchar(45),
PRIMARY KEY (code_module, code_presentation)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\courses.csv'
IGNORE INTO TABLE courses
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

CREATE TABLE IF NOT EXISTS vle (
id_site int primary key,
code_module varchar(45),
code_presentation varchar(45),
activity_type varchar(45),
week_from int,
week_to int,
FOREIGN KEY(code_module, code_presentation) REFERENCES courses(code_module, code_presentation)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\vle.csv'
IGNORE INTO TABLE vle
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(id_site, code_module, code_presentation, activity_type, @week_from, @week_to)
SET week_from = NULLIF(@week_from, ''), week_to = NULLIF(@week_to , '');

CREATE TABLE IF NOT EXISTS assessments (
code_module varchar(45),
code_presentation varchar(45),
id_assessment int PRIMARY KEY,
assessment_type varchar(45),
date int,
weight int,
FOREIGN KEY (code_module, code_presentation) REFERENCES courses(code_module, code_presentation)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\assessments.csv'
IGNORE INTO TABLE assessments
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(code_module, code_presentation, @id_assessment, assessment_type, @date, @weight)
SET id_assessment = NULLIF(@id_assessment, ''), date = NULLIF(@date, ''),  weight = NULLIF(@weight, '');

# Student Info
CREATE TABLE IF NOT EXISTS studentinfo (
code_module varchar(45),
code_presentation varchar(45),
id_student int primary key,
gender varchar(3),
region varchar(45),
highest_education varchar(45),
imd_band varchar(16),
age_band varchar(16),
num_of_prev_attempts int,
studied_credits int,
disability varchar(3),
final_result varchar(45),
FOREIGN KEY (code_module, code_presentation) REFERENCES courses(code_module, code_presentation)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\studentInfo.csv'
IGNORE INTO TABLE studentinfo
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(code_module, code_presentation, @id_student, gender, region, highest_education, imd_band, age_band, @num_of_prev_attempts, @studied_credits, disability, final_result)
SET id_student = NULLIF(@id_student, ''), num_of_prev_attempts =  NULLIF(@num_of_prev_attempts, ''), studied_credits = NULLIF(@studied_credits, '');


# Student Activities
CREATE TABLE IF NOT EXISTS studentassessment (
id_assessment int,
id_student int,
date_submitted int,
is_banked tinyint,
score float,
FOREIGN KEY (id_student) REFERENCES studentinfo(id_student),
FOREIGN KEY (id_assessment) REFERENCES assessments(id_assessment)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\studentAssessment.csv'
INTO TABLE studentassessment
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@id_assessment, @id_student, @date_submitted, @is_banked, @score)
SET id_assessment = NULLIF(@id_assessment, ''), id_student =  NULLIF(@id_student, ''), date_submitted = NULLIF(@date_submitted, ''),
is_banked =  NULLIF(@is_banked, ''), score = NULLIF(@score, '');

CREATE TABLE IF NOT EXISTS studentvle (
code_module varchar(45),
code_presentation varchar(45),
id_student int,
id_site int,
date int,
sum_click int,
FOREIGN KEY (code_module, code_presentation) REFERENCES courses(code_module, code_presentation),
FOREIGN KEY (id_student) REFERENCES studentinfo(id_student),
FOREIGN KEY (id_site) REFERENCES vle(id_site)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\studentVle.csv'
INTO TABLE studentvle
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@code_module, @code_presentation, @id_student, @id_site, @date, @sum_click)
SET id_site = NULLIF(@id_site, ''), id_student =  NULLIF(@id_student, ''), code_module = NULLIF(@code_module, ''),
code_presentation =  NULLIF(@code_presentation, ''), date = NULLIF(@date, ''), sum_click = NULLIF(@sum_click, '');

CREATE TABLE IF NOT EXISTS studentregistration (
code_module varchar(45),
code_presentation varchar(45),
id_student int,
date_registration int,
date_unregistration int,
FOREIGN KEY(code_module, code_presentation) REFERENCES courses(code_module, code_presentation),
FOREIGN KEY(id_student) REFERENCES studentinfo(id_student)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\studentRegistration.csv'
INTO TABLE studentRegistration
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(code_module, code_presentation, @id_student, @date_registration, @date_unregistration)
SET id_student =  NULLIF(@id_student, ''), date_registration = NULLIF(@date_registration, ''),
date_unregistration =  NULLIF(@date_unregistration, '');