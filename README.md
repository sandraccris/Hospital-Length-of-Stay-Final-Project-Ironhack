# Hospital Length of Stay: A Predictive Tool


![myimage](https://bestpractice.bmj.com/info/wp-content/uploads/2020/08/iStock-1194838627-scaled.jpg)


## :hospital: Project Overview 

The goal of this project was to create a tool by developing a **supervised classification machine learning model** that can predict the hospital length of stay for patients who are scheduled for General Surgery Procedures. 

**Hospital bed shortages** have been a significant challenge in healthcare worldwide, exacerbated further by the impact of the Covid19 pandemic. Surgical procedures often face cancellations due to a lack of available beds to accommodate post-operative patients.

In this context, accurately predicting the length of stay for patients becomes crucial for hospitals and healthcare facilities. A reliable predictive tool can assist hospital administrators, bed managers and healthcare staff in managing bed capacity effectively. By having a better estimate of the length of stay, hospitals can optimize their bed and staff allocation, improve patient safety, and enhance overall financial and medical efficiency.

This project was developed as part of the Ironhack Data Analytics Bootcamp. 


**Agile Project Planning Tool**: Jira 


## :file_folder: Dataset 	

**VitalDB** (Vital Signs DataBase) is an open Dataset from Seoul National University Hospital, Seoul, Republic of Korea containing perioperative clinical information, laboratory results and intraoperative monitoring parameters of 6,388 surgical patients (general, thoracic, urologic, and gynaecologic) who underwent routine or emergency surgery. 

The dataset includes 73 columns with Clinical parameters, 196 intraoperative monitoring parameters and 34 columns with Laboratory results parameters. For this project only data for General Surgical Patients was selected and used.

[Dataset](https://vitaldb.net/dataset/?query=overview) available here.

[CSV Files](https://www.kaggle.com/datasets/kamyababedi/vitaldb?select=clinical_parameters.csv) available here.

## :spiral_notepad: Repository Files 

01. [SQL Queries](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/blob/main/SQL_queries/sql_queries_LOS.sql)


02. [Streamlit Web App Development](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/tree/main/Streamlit_App). You can see it live by [cliking here](https://hospital-length-of-stay-final-project-ironhack-c3dx0z8b65p.streamlit.app/) and exploring its features.


03. [Tableau Documentation](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/tree/main/Tableau_dashboard). You can see my Tableau Dashboard about Factors Affecting Hospital Length of Stay by [clicking here](https://public.tableau.com/app/profile/sandra.cunha/viz/FactorsAffectingLengthofHospitalization/Dashboard1).


04. Machine Learning Model Development:
   
- 4.1 [Python Script 1 - Data Extraction, Cleaning, Exploratory Data Analysis](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/blob/main/Python_Scripts/01_Cleaning_EDA.ipynb)

- 4.2 [Python Script 2 - Pre-processing (continuation) and Modeling](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/blob/main/Python_Scripts/02_Preprocessing2_Modeling.ipynb)

- 4.3 [Python Script 3 - Model Optimization, Evaluation and Validation](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/blob/main/Python_Scripts/03_Random_Forest_Classifier_Optimization_Evaluation.ipynb)


05. [Final Project Presentation](insert link)


## :chart_with_upwards_trend: Results 

- #### Baseline Metrics 

![Baseline Metrics](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/assets/113031999/cf0c1e91-5881-45ab-9739-eb448c893c66)


- #### Random Forest Classifier Confusion Matrix
![confusion matrix](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/assets/113031999/4e750b21-77ae-430c-8c01-35fa38a00e61)

**Overall Accuracy of 74%**

Model is particularly effective in correctly predicting **Short Length of Stay** class, as evident from the higher precision (**78%**)  when comparing to Medium (70%) and Prolonged lengths (65%). 



![AUC ROC Curve](https://github.com/sandraccris/Hospital-Length-of-Stay-Final-Project-Ironhack/assets/113031999/c9ec89a8-692a-458b-bd01-484e4e58b9f1)

Model demonstrates ability in differentiating between the three classes: Short, Medium, and Prolonged Lengths of Stay. All classes have an AUC score above 0.5 which means there is high chance that this Random Forest Classifier model is able to discriminate between True positives and False positives for each class.


### :lock: Conclusion 


- The **Random Forest Classifier** Model having an overall accuracy of **74%**, shows promise as a reliable tool that could be used by hospital administrators, bed managers and healthcare professionals for predicting different Hospital Lengths of Stay (Short, Medium or Prolonged) in surgical patients. By performing accurate predictions, it can contribute to a more effective management of hospital resources (human and material) and reduce costs.

- Model's true effectiveness can only be determined by assessing its performance on **real-world unseen patient data**. Given that the model was trained on data where synthetic samples were generated for the minority classes (using SMOTE) to address the class imbalance issue, particular attention should be given to its performance on the "Medium" and "Prolonged" Length of Stay classes.

- The model's predictions could also be utilized by patients preoperatively to inform them about whether their hospital stay will be short, medium, or prolonged through an **web application**, based on specific input parameters. Empowering patients with this information can help them be proactive in preparing for surgery, planning their recovery and reducing anxiety level.

- Also, patients with a higher likelihood of a **prolonged hospital stay** can be targeted by hospital staff in order to develop and implement strategies earlier to optimize their discharge planning, recovery and potentially continuing care after discharge at home through **telemedicine**. This approach not only optimizes patient care but also helps to free up hospital beds and prevents surgery cancellations that happens often due to lack of beds.


### :handshake: Acknowledgments 

VitalDB. Lee HC, Park Y, Yoon SB, Yang SM, Park D, Jung CW. VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients. Sci Data. 2022 Jun 8;9(1):279. doi: 10.1038/s41597-022-01411-5. PMID: 35676300; PMCID: PMC9178032.  [Available Here](https://vitaldb.net/dataset/?query=overview#h.foizq7qqcyzk).

Lead Teacher: Xisca, Teaching Assistants: Laz, Sabina and Camille and all my class colleagues.

### :mag_right: Resources 

- https://www.sheffieldmca.org.uk/UserFiles/File/Ward_Collab/Ward_Principles/improving_length_of_stay_hospitals_web_final.pdf
- https://www.medcalc.org/manual/chi-square-table.php
- https://towardsdatascience.com/using-the-chi-squared-test-for-feature-selection-with-implementation-b15a4dad93f1
- https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e
- https://towardsdatascience.com/feature-engineering-for-machine-learning-3a5e293a5114
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7819802/
- https://vegibit.com/scikit-learn-hyperparameter-tuning-and-feature-selection/
