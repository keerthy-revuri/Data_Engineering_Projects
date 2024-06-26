
truncate table  postgres.public.github_staging;

copy postgres.public.github_staging(
	category,
	file_names,
	updated_dtm
)
FROM 'C:/Users/Public/dataeng_project_output/Github_data_to_excel/output/output.csv'
DELIMITER ','
CSV HEADER;

DELETE FROM postgres.public.github_staging where (category, file_names) is null;

DELETE FROM postgres.public.github_target using postgres.public.github_staging where github_staging.category = github_target.category
and github_staging.file_names = github_target.file_names;

drop table if exists temp_github_staging;

create temporary table temp_github_staging
as SELECT category,
          file_names,
          updated_dtm
FROM postgres.public.github_staging;

INSERT INTO postgres.public.github_target(
    category,
    file_names,
    updated_dtm
    )
SELECT category,
       file_names,
       updated_dtm
FROM temp_github_staging
group by
category,
file_names,
 updated_dtm

