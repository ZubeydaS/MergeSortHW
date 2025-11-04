| # | COMPAS COLUMN TITLE | DEFINITION |
|:--:|:-------------------:|:-----------:|
|1.| id: |  unique identification for each person | 
|2.| name:| name of the subject|
|3.| first:| first name of the person|  
|4.| last: | last name of the person|
|5.| compas_screening_date: | COMPAS screening data of the suspect|  
|6.| sex: |sex of the subject| 
|7.| dob:| date of birth of the subject|
|8.| age: | age category of the suspect at the time of the survey|
|9.| age_cat: |age category of the subject| 
|10.| race:  |race of the suspect |  
|11.| juv_fel_count: |the number of felony charges as a juvenile| 
|12.| decile_score:  |recidivism score from 1 to 10| 
|13.| juv_misd_count:  | the number of misdemeanor charges as a juvenile|  
|14.| juv_other_count: |the number of other charges for the suspect| 
|15.| priors_count: | the number of prior convictions for the suspect| 
|16.| days_b_screening_arrest: |screeding date happened before arrest date|  
|17.| c_jail_in:  |start timestamp of incarceration| 
|18.| c_jail_out: |end timestamp of incarceration| 
|19.| c_case_number: |charge case number of the suspect|  
|20.| c_offense_date:|charge offense date of the suspect| 
|21.| c_arrest_date:|charge arrest date of suspect| 
|22.| c_days_from_compas:| the count of days between screening date and (original) arrest date. If they are too far apart, that may i the number of days between committing an offense and going to jail|  
|23.| c_charge_degree: |charge degree of the suspect| 
|24.| c_charge_desc: |charge description of the suspect| 
|25.| is_recid: | whether the suspect recidivate| 
|26.| r_case_number: | recidivism case number of suspect | 
|27.| r_charge_degree:  | recidivism charge degree of suspect| 
|28.| r_days_from_arrest: | re-arrested from the re-offense date| 
|29.| r_offense_date:| recidivism offense date of the suspect|  
|30.| r_charge_desc: |recidivism charge description of the suspect | 
|31.| r_jail_in:| time and date when the suspect goes in the jail for recidivism| 
|32.| r_jail_out: |time and date when the suspect gets released from the jail for recidivism|  
|33.| violent_recid: |violent recidivism crime indicator of the suspect| 
|34.|is_violent_recid: |violent recidivism crime indicator of the suspect| 
|35.| vr_case_number:  |violent_charge_number of the suspect|  
|36.|vr_charge_degree: |violent_charge_degree of the suspect| 
|37.|vr_offense_date: |violent_charge_date of the suspect|
|38.| vr_charge_desc:  |violent_charge_description of the suspec|  
|39.| type_of_assessment:  |onstant “Risk of Recidivism” for all rows, can be omitted| 
|40.| decile_score: |repetition of column 12| 
|41.| score_text:  | decile score text -> low, medium, high|  
|42.| screening_date:  |COMPAS screening date of the suspect | 
|43.| v_type_of_assessment:  |constant “Risk of Violence” for all rows, can be omitted| 
|44.| v_decile_score:  |violent recidivism score from 1 to 10| 
|45.| v_score_text:  |violent recidivism score text -> low, medium, high| 
|46.| v_screening_date:  | COMPAS screening data of the suspect for violent crimes| 
|47.| in_custody:  | custody start date| 
|48.| out_custody:  |custody end date| 
|49.| priors_count:  |the number of prior conviction for the suspect| 
|50.| start survival analysis:  | start point of the suspect entering the analysis|
|51.| end survival analysis:  | end point of the suspect entering the survival analysis| 
|52.| event binary indicator: | denotes whether the event of recidivism has occurred or not| 
|53.| two_year_recid:  | target ->  two year recidivism (binary 0/1)| 
|54.| total_days_custody (in_custody - out_custody):  | how long the person stayed in custody| 
|55.| total_days_jail (c_jail_out - c_jail_in))l:  | how long the person stayed in jail|
