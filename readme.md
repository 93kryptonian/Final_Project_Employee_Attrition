# Final Project JCDS 07

# Employee Attrition Tendency Detection

#### By: Khumaeni

## Background

<hr>
Employee Attrition lebih dikenal dengan Turn over rate
<br><br>
Karyawan berhenti dari perusahaan bukan hanya dapat mengganggu proses bisnis perusahaan, tetapi juga membuat perusahaan mengeluarkan cost yang tidak sedikit.
Yang menjadi concern dari prototype ini adalah untuk mendeteksi karyawan terutama yg memiliki performance bagus maupun yg high potential tetapi tidak puas dan cenderung ingin keluar dari perusahaan. Diharapkan dengan dapatnya deteksi dini, karyawan tersebut dapat ditangani sehingga tidak sampai keluar dari perusahaan.
<br>
<hr>

## ML Detection Prototype

### Dataset
Dataset yang digunakan berasal dari kaggle ![Kaggle_Dataset]:(https://www.kaggle.com/dredlaw/predict-employment-termination/data)

![Dataset](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/dataset.PNG)

## Data Description
- EmployeeID : ID Karyawan (Tetapi Tidak Unique)
- recorddate_key : Tanggal Data direcord
- birthdate_key : Tanggal lahir karyawan
- orighiredate_key : Tanggal Masuk Karyawan
- terminationdate_key : Tanggal terminate
- age : Usia
- length_of_service : Masa Kerja
- city_name : Nama Kota
- department_name : Nama Departemen
- Job_Title : Jabatan Karyawan
- store_name : Nama Toko
- gender_short : Jenis Kelamin
- gender_full : Jenis Kelamin
- termreason_desc : Alasan berhenti
- termtype_desc : Jenis termination
- STATUS_YEAR : Tahun record data
- STATUS : Status karyawan
- Business Unit : BU karyawan

## Data Exploration
Explorasi Dataset
![Exploration](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/Exploration.PNG)

## Termination report by Years
Report by Years
![Report](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/years.PNG)

## Feature Engineering
Data setelah dilakukan feature engineering
![engineering](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/engineering.PNG)

## Data Desc (After Feature Engineering)
1. **Age** : Usia Employee (dalam tahun)
2. **Length_of_Service** : Masa Kerja (dalam tahun)
3. **gender_short** : Jenis Kelamin (Female : 0, Male : 1)
4. **STATUS** : Status Employee (Active : 0, Terminated : 1)
5. **Business_Unit** : Unit Bisnis berdasarkan Tempat kerja (Head Office : 0, Store : 1)
6. **Job_Level** : Kategori Level jabatan di perusahaan (Staff : 0, Manager : 1, Board : 2, Executive : 3)
7. **Dept_Category** : Kategori departemen berdasarkan core (pekerjaan utama), (Business : 0, Customer : 1)
<hr>
# Algorithm 
<br>
Algoritma Machine Learning yang saya gunakan ada 4 yaitu:
<br>
1. KNN
2. Random Forest
3. XGBoost
4. SVM

## Saya membandingkan hasil Evaluation Metrics dari Algorithm tersebut, Hasilnya adalah :

### KNN
   ![KNN](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/eva_KNN.PNG)

### Random Forest Classifier
   ![RF](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/eva_RF.PNG)

### XGBoost
   ![XGB](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/eva_XGB.PNG)

### SVM
   ![SVM](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/eva_SVM.PNG)

<hr>
## Web Application
Tampilan dari Web Apps nya adalah sebagai berikut

1. Home <br>
Tampilan awal dari Applikasi
   ![Home](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/Home.PNG)

2. Predict <br>
Adalah halaman yg digunakan user untuk melakukan input data, untuk selanjutnya dilakukan deteksi
   ![predict](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/predict.PNG)

3. Result <br>
Halaman yg mengeluarkan Hasil dari Deteksi berdasarkan data yg telah diinput
   ![predict](https://github.com/93kryptonian/Final_Project_Employee_Attrition/blob/master/images/result.PNG)
<hr>

#### Khumaeni - 2020
