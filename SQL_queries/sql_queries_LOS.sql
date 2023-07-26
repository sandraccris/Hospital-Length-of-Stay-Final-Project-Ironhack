use ironhack_final_project;

-- How many patients we have in our dataset?
SELECT 
    COUNT(DISTINCT case_id)
FROM
    clinical_data;
-- Result: 5155 patients


-- Let's find out how many General Surgical patients had emergency surgery  (0-No, 1-Yes)

SELECT 
    department, emop, COUNT(emop) AS admission_type_planned
FROM
    clinical_data
WHERE
    department = 'General surgery'
        AND emop = '0' 
UNION SELECT 
    department, emop, COUNT(emop) AS admission_type_emergency
FROM
    clinical_data
WHERE
    department = 'General surgery'
        AND emop = '1';
-- Result: 3567 had a planned surgical procedure and 465 patients had an emergency surgical procedure.


-- Length of Stay Exploration

SELECT 
    department,
    optype,
    ROUND(AVG(dis / 86400)) AS avg_length_days
FROM
    clinical_data
WHERE
    dis > 0
GROUP BY department , optype
ORDER BY avg_length_days DESC;

-- Result:Thoracic surgery and General surgery have the longest LOS
-- Also, Transplantation patients from each have the longest hospital stay after surgery, followed by "Others". 


-- Which surgical procedures from Thoracic and General Surgery have a Length of Stay higher than the Average Lenght of Stay??

SELECT 
    department, opname, optype, ROUND(dis / 86400) AS LOS
FROM
    clinical_data
WHERE
    ROUND(dis / 86400) >= (SELECT 
            ROUND(AVG(dis / 86400))
        FROM
            clinical_data
        WHERE
            department = 'Thoracic surgery'
                OR department = 'General surgery')
ORDER BY LOS DESC;
-- Result: We can see that the longest lengths are associated with procedures normally performed in patients with chronic conditions and cancer, which are patients that remain hospitalized for long periods.


-- Now I want to know how many general surgical patients who are hypertensive and diabetic with a BMI = "obese" or "Pre-obese" have a prolonged Length of Stay (comparing with the avg LOS)?

-- First let's find out total amount of patients who are hypertensive and diabetic with a BMI of "obese and "Pre-obese":
SELECT 
    COUNT(*)
FROM
    (SELECT 
        case_id,
            department,
            preop_htn,
            preop_dm,
            bmi,
            CASE
                WHEN bmi >= 25.0 AND bmi <= 29.9 THEN 'Pre-obese'
                WHEN bmi >= 30.0 THEN 'Obese'
                ELSE 'Normal Weight'
            END AS BMI_status,
            ROUND(dis / 86400) AS LOS_days
    FROM
        clinical_data
    WHERE
        preop_htn = '1' AND preop_dm = '1'
            AND department = 'General surgery') AS subquery
WHERE
    BMI_status IN ('Obese' , 'Pre-obese');
-- Result: A total of 99 General surgical patients are diabetic, hypertensive and obese or pre-obese.


-- How many of them have a prolonged hospitalization?

WITH CTE_bmi_aggre AS (
SELECT case_id, department, preop_htn, preop_dm, bmi, 
    CASE 
        WHEN bmi >= 25.0 AND bmi <= 29.9 THEN "Pre-obese"
        WHEN bmi >= 30.0 THEN "Obese"
        ELSE "Normal Weight"
    END AS BMI_status, ROUND(dis/86400) AS LOS_days
FROM clinical_data
where preop_htn = "1" and preop_dm = "1" and department = "General surgery"
)
SELECT COUNT(*) as total_patients
FROM CTE_bmi_aggre
WHERE LOS_days >=
	(SELECT ROUND(AVG(dis/86400))
	FROM clinical_data WHERE department="General surgery") AND BMI_status IN ("Obese", "Pre-obese");
-- Result: 43% of General Surgical Patients (43 from a total of 99) who are diabetic and hypertensive and obese/pre obese had a prolonged hospital stay comparing with the average, that is almost half of the patients!!


-- OR I can do the above queries but with a VIEW, which will store the query result in memory and can be retrieved to be re used by other queries. 

CREATE VIEW bmi_aggr AS
    SELECT 
        case_id,
        dis,
        department,
        preop_htn,
        preop_dm,
        bmi,
        CASE
            WHEN bmi >= 25.0 AND bmi <= 29.9 THEN 'Pre-obese'
            WHEN bmi >= 30.0 THEN 'Obese'
            ELSE 'Normal Weight'
        END AS BMI_status,
        ROUND(dis / 86400) AS LOS_days
    FROM
        clinical_data
    WHERE
        preop_htn = '1' AND preop_dm = '1'
            AND department = 'General surgery'
;

SELECT 
    COUNT(*)
FROM
    bmi_aggr
WHERE
    BMI_status IN ('Obese' , 'Pre-obese')
ORDER BY LOS_days DESC;
-- Total 99 patients as we seen above in the CTE.


SELECT 
    COUNT(*) AS total_patients
FROM
    bmi_aggr
WHERE
    LOS_days >= (SELECT 
            ROUND(AVG(dis / 86400))
        FROM
            clinical_data
        WHERE
            department = 'General surgery')
        AND BMI_status IN ('Obese' , 'Pre-obese');
-- 43 patients as we seen above in the CTE