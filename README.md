# Doctor-Fee-Prediction
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/e873a621-a51d-4e47-af92-9db45ec52b1c)

# Introduction

Welcome to the repository for Doctor's Fee Prediction Machine Learning model! In this repository, I present an innovative solution aimed at predicting medical consultation fees based on various relevant factors. Whether you're a patient, healthcare professional, upcoming doctor or a data enthusiast, this project offers valuable insights into predicting the financial aspect of medical services.

# Problem Aimed to Solve

This project takes into consideration a number of factors such as Speciality of Doctor, Degree Type, Year of Experience, DP Score, City etc. for predicting the Doctor's fees which certainly helps patients and upcoming doctors to have an idea about it.

# Tools & Technologies Used
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/45351c55-f3d3-4721-86d6-30c0e4bbd68e)




# OUR APPROACH FOR THE PROJECT
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/3ea4bb7a-6da9-4698-bdbd-3dc60e0cc4a2)

# User's Manual
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/fc9f0b0b-ce13-4f24-946b-629e803315dd)


## Machine learning model-
In this project, we use a linear regression model to predict doctor's fees. Linear regression is a simple yet effective technique for modeling relationships between a dependent variable (doctor's fee ) and one or more independent variables (features).

### Variables-
- speciality_of_doctor: Specialty of the doctor
- degree_type: Type of degree (e.g., MBBS, MD, BDS)
- year_of_experience: Total years of experience
- Location: Clinic location
- city: City of the clinic
- dp_score: Doctor-patient experience score
- npv_: Number of people's votes



# Data Preparation
# Data Scarpping (Snapshots)
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/1e286d03-131f-4665-88b0-c5cf6a801b36)

----------------------------------------------------------------------------------------------------------------------
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/063e6947-46c3-4e1d-a306-8f4168a3e9a0)


# Data Cleaning (few code snippets)
1. Null Handling & Remove Noise Values
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/df0a8a1f-c73b-478b-b7a8-1523afb43c1e)


3. Change Data type of Consultation Column
   ![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/b0833efa-fb9d-4b76-80b1-f64ab82fb2fb)
   
   
5. In the data sets Location column and city column both have city name which is not generally required. so here we will split the column using ',' delimeter and then remove the column contain city name.
   ![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/dc2f6215-8f87-4e6e-89bb-9a958b9b3476)
   

# Exploratory Data Analysis(EDA)

# Number of Doctors by each City
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/a59d9f4e-ffdb-4082-be88-8a6dff9da469)

------------------------------------------------------------------------------------------------------------------------

# Count  of Doctors in each Speciality
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/11079f23-5985-46d7-a25c-7913f54395fb)



-------------------------------------------------------------------------------------------------------------------------

# Speciality wise Fees Analysis
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/3120eb36-d8f8-4fe7-9113-ee97cb757565)


--------------------------------------------------------------------------------------------------------------------------

# Percentage of  Doctors avilable in each of the city
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/c29cc699-51b6-47e8-9b0c-30814cb4e045)


-------------------------------------------------------------------------------------------------------------------------

# Correlation between the Variables By using Heatmap
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/b25da979-d418-46a0-8614-50963db2ba7a)


-------------------------------------------------------------------------------------------------------------------------

# Doctors Having Maximum number of Specialization
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/43d79d51-d358-444d-918e-258b987c37ba)



-------------------------------------------------------------------------------------------------------------------------

# Distribution of  year of experience
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/e7aaa642-9722-4285-8638-63fa1bc0421b)



# Key Insights
1. Most of the doctors have 13 to 15 years of experience.

2. Cities like Bangalore have a higher percentage of doctors, accounting for approximately 40.23%.

3. The majority of doctors specialize in Dentistry (1460), while the fewest doctors specialize in Chiropractic (7).

4. Bangalore has the highest number of doctors compared to Delhi and Mumbai.

5. In each city, the number of dentists is higher than other specialties because their consultation fees are completely free.

6. Neurosurgeons and Ophthalmologists charge high consultation fees, while specialties like Dentistry, Dermatology, Gynecology/Obstetrics, Infertility Specialists, Physiotherapy, and Dietetics/Nutritionists offer almost free consultations.

7. Locations like Saket in Delhi have the highest concentration of doctors.

8. The most common degree among doctors is BDS.

# Future scope

- This fee predictor can help upcoming doctors who are looking to set up their clinic to have an idea of how much other doctors are charging.
- Patients can have an idea of how much they are likely to be charged based on the factors that are mentioned in the model.
- A doctor looking to expand his/her clinic to other cities can also have an idea how much doctors are charging in that particulr city of an area of the city.

# Problems faced

- Faced problems while deploying the model onto the webpage, tackled it by referring to the free resources and tutorials available on YouTube.
- Having little knowledge about HTML and CSS, it was difficult to make a webpage, but took reference from YouTube and ChatGPT.
