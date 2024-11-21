
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

DROP table if temp_github_staging exists;

CREATE temporary table temp_github_staging as
SELECT Category, file_names, max(updated_dtm) from
postgres.public.github_staging group by category, file_names;

DELETE FROM postgres.public.github.staging using temp_github_staging
where github_staging.file_names = temp_github_staging.file_names and
github_staging.category = temp_github_staging.category
and github_staging.updated_dtm <> temp_github_staging.updated_dtm;

INSERT INTO postgres.public.github_target(
    category,
    file_names,
    updated_dtm
    )
SELECT category,
       file_names,
       updated_dtm
FROM temp_github_staging


