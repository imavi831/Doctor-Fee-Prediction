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
Sure, here's a more descriptive explanation of the code snippets and files you provided:

### Web Scraping with Selenium and BeautifulSoup
- The following code snippet demonstrates web scraping using Selenium and Chrome WebDriver. It extracts data about chiropractors from Practo in cities like Bangalore, Delhi, and Mumbai and automates web browsing. The information is stored in an initially empty DataFrame.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIDBVxwJeCi3gdo4Nx0cxeLeT2zjrDVCyzBHB5r74JEZRvrxZU4cxQahq9uNDOfOWXhnt0ZjofIn5BeFf6ILe1UeMQ7lyk0TOByR-HjuMq-n8oYlUNoi4JPOAYS6uQ1AQwU7lu50h9QMyLE3UQqVMZwYa0ksCYrkgdkgf2r75zIEqGVL5kFx1Cbwlz/s16000/266239520-1e286d03-131f-4665-88b0-c5cf6a801b36.png)

- In this code snippet, BeautifulSoup is used to parse the HTML of Practo's web pages. It systematically navigates through the listings, retrieving details like the doctor's name, degree, years of experience, location, DP score, NPV, and consultation fee. This information is then appended to the previously created DataFrame for each chiropractor found in the specified cities.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh76MN1tsMnpFqPvavOtaEOGQNRaBqhbXCjgRzNHJgLuQaBFaKsuLxDJ2WrNyc7A0JulucqvQHUYyfzSswvM6ONOw9NrrYEqqykD6moU62aHGt5hw6e_hcaoPPAmGbAMy_iuO-dyjktN_JZ8Fh01YXplWVZzjHAy1aQGQmYvggDEUhiI_GN3fVjSmbw/s16000/266239786-063e6947-46c3-4e1d-a306-8f4168a3e9a0.png)


- The extracted data is accumulated in the DataFrame as shown below:
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQgPV34sYCxG_l9DvkbF8PZdkJq5nmb47cjiAuWc4tNvntKxW9YFXrNRLFact4dmeIAxbleyuRbjaJ_Ye9d3PDzOu0bezqgRKK8CxWt_JIItNAElE2-tAsnim1_vmmWQodEX7SLr4fUoboVM_68J1NYPfd5Y-qjYfavU4vT7qLwu5RVyTQIZa6f_Zn/s16000/269669513-1373a028-512c-4188-871e-40033a592534.png)

- Similar code can be applied to other doctor specializations by replacing the URL.

### CSV File
- The image below displays the CSV file created by aggregating all the scraped data into various dataframes. All CSV files were combined into a single CSV file, which is also available in the repository folder.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihNYG7qC_BTyZCVN5oGBPp67FeFC2TPf_eD7Hf41vvgPZj-pIReSkiOnwJLonMCYUWIkBzjrSH0Z9oq1Nii-eqyTytpJTLB7b6c0qXQ4Umkc8dxRP7D3CeNy1v6zNohah8cw4our5yO3JF0o4OV0-NUcffX8pu_tz_LMc8PVYeGDVRZ6B9y6t01wdh/s16000/259536462-b7bf92b4-f240-47f7-a596-2cae75d5427c.png)

### HTML Files
- The provided HTML code snippet represents the foundational structure of a basic webpage for "Doctor Fees Prediction." It incorporates jQuery and jQuery UI libraries, establishes fundamental styling, and defines the webpage's layout.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRWleHPP98d2LdPPPbYv2FOBntUl3UbD6aF8__4PIQnDLDFU22Me7MShAG653qwS0U6X_Qkf0yF8DPjfwoQKqFJ_lfGt0avF1olbqB-UC8G7dDI_1MyK-ZzvbQD62EQXNJtRa7vHx0-a4GjyJF_OFyc8BBvS1JrAGCNYal2aDRsyBBJIodLjbmdn0w/s16000/269673906-c3efaacc-35a1-4af6-b259-c0b358c3fb90.png)

- This HTML snippet depicts a form for "Doctor Fees Prediction." It comprises several input fields and a submit button enclosed within a <form> element.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh49oF0zWI329zvHJbKBgVrt93g-qaI9HxhgO3MRPPBZZ8YBpi3vsQWi_OF-FH_Pppe3nFzPp7I71ZgjVzwvJkUStl7mHlOspQHnlQyItqPYY3gEmWnabdM7LEhTtuPPUDCe-fZV0PS_vR5f96MZGTUEQdCTIIAoI3GuXGk26RBwNyTDgtrdZvO8cnN/s16000/269674684-6bf67f52-8b2f-415e-8f35-f0090d73de91.png)

### Flask File
- The Python Flask code provided establishes a web application for predicting doctor fees utilizing a pre-trained machine learning model.
- Users input data via a form, which is then processed to generate a fee prediction displayed on the webpage.
- You can access the complete code in the file named `app.py` in this repository.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisDDvznzrgKLJWKhiLz-OOIqc1iLQfRI0GLZCqeK5jOAWmt8ncry5hm6nTIgeZxRUMSMQQ4g8FlJSJEnyOnfyYhI9X-_ISb0jU0JXC6Y-bsH7ZbT7SU_ww5D08HRBAFKf2zUHHEdPnnLzX2XNqk4hwjJDHFpjRSU92_KiKQCHFAPyuyn2Nor64HU7_/s16000/269675495-98f3df17-76ff-41c4-a5b3-f3377d12cf4f.png)

## Web Page
- This screenshot below provides a visual representation of the web page created for predicting doctor fees using a Flask-based web application.
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhew16EXVysAW1oM00t55eCBPpZSUi1BhkWQEiBhezD6_Lc7D3RlHS-F6IhTYwCYBpe0Q_a2Q_vCi8xze-ABjHUq4BI4y-ttkRORDJg7lQzUFc9G5byfafKC1G0s-11FDcOGEStQ439ZaSbVXpW-1vwBm9TDCmVKwlXZJzgxUGbKfbC0iHcwVzBjtvE/s16000/ezgif.com-video-to-gif.gif)



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

Highest number of doctors are from Bangalore(2169) whereas Mumbai has 1458 doctors listed in the website.

------------------------------------------------------------------------------------------------------------------------

# Count  of Doctors in each Speciality
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/11079f23-5985-46d7-a25c-7913f54395fb)

The majority of doctors specialize in Dentistry(1460), while the fewest doctors are Chiropractors (7).

-------------------------------------------------------------------------------------------------------------------------

# Speciality wise Fees Analysis
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/3120eb36-d8f8-4fe7-9113-ee97cb757565)

Neurosurgeons and Ophthalmologists charge high consultation fees, while specialties like Dentistry, Dermatology, Gynecology/Obstetrics, Infertility Specialists, Physiotherapy, and Dietetics/Nutritionists offer almost free consultations.

--------------------------------------------------------------------------------------------------------------------------

# Percentage of  Doctors avilable in each of the city
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/c29cc699-51b6-47e8-9b0c-30814cb4e045)


-------------------------------------------------------------------------------------------------------------------------

# Distribution of  year of experience
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/e7aaa642-9722-4285-8638-63fa1bc0421b)

The plot above is showing that majority of doctors are in the range of experience between 13 to 15 years.


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
