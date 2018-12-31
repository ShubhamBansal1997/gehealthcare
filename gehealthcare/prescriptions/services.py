# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
from gehealthcare.users.models import User
 
def health_stats():
	try:
		data1=pd.read_csv('Key_indicator_districtwise_core.csv')


		#data1=pd.read_csv("/Users/shefalibansal/Downloads/health-analytics/Key_indicator_districtwise_core.csv")
		df=pd.DataFrame(data1['State_Name'])
		df2=pd.DataFrame(data1['State_District_Name'])
		output=pd.concat([df,df2],axis=1)
		Diarrhoea_Dysentery=[]
		for i in range(284):
		    Diarrhoea_Dysentery.append((data1['JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Diarrhoea_Dysentery_Person_Total'][i]/1000))
		    
		df=pd.DataFrame({'Diarrhoea_Dysentery':Diarrhoea_Dysentery})
		output=pd.concat([output,df],axis=1)

		respiratory_infection=[]
		for i in range(284):
		    respiratory_infection.append((data1['JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Acute_Respiratory_Infection_Ari_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'respiratory_infection':respiratory_infection})
		output=pd.concat([output,df],axis=1)

		fever=[]
		for i in range(284):
		    fever.append((data1['JJ_Persons_Suffering_From_Acute_Illness_Per_100000_Population_Fever_All_Types_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'fever':fever})
		output=pd.concat([output,df],axis=1)

		Diabetes=[]
		for i in range(284):
		    Diabetes.append((data1['KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Diabetes_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'Diabetes':Diabetes})
		output=pd.concat([output,df],axis=1)


		hypertension=[]
		for i in range(284):
		    hypertension.append((data1['KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Hypertension_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'hypertension':hypertension})
		output=pd.concat([output,df],axis=1)


		Tuberculosis=[]
		for i in range(284):
		    Tuberculosis.append((data1['KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Tuberculosis_Tb_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'Tuberculosis':Tuberculosis})
		output=pd.concat([output,df],axis=1)


		Asthama=[]
		for i in range(284):
		    Asthama.append((data1['KK_Having_Diagnosed_For_Chronic_Illness_Per_100000_Population_Asthma_Chronic_Respiratory_Disease_Person_Total'][i]/1000))
		   
		df=pd.DataFrame({'Asthama':Asthama})
		output=pd.concat([output,df],axis=1)


		health_stats_ = open('file', 'w')
		output.to_csv("health_stats_.csv")
	except:
		print("Excited")


def diet_plan():
	disease_percent=pd.read_csv("health_stats_.csv")
	p_district=pd.read_csv("district_disease_data.csv")

	mean_diarrhoea=0

	for i in range(disease_percent.shape[0]):
	    mean_diarrhoea=mean_diarrhoea+disease_percent['Diarrhoea_Dysentery'][i]
	    
	mean_diarrhoea=mean_diarrhoea/disease_percent.shape[0] 
	mean_resp=0

	for i in range(disease_percent.shape[0]):
	    mean_resp=mean_resp+disease_percent['respiratory_infection'][i]
	    
	mean_resp=mean_resp/disease_percent.shape[0] 

	mean_fever=0

	for i in range(disease_percent.shape[0]):
	    mean_fever=mean_fever+disease_percent['fever'][i]
	    
	mean_fever=mean_fever/disease_percent.shape[0] 

	mean_Diabetes=0

	for i in range(disease_percent.shape[0]):
	    mean_Diabetes=mean_Diabetes+disease_percent['Diabetes'][i]
	    
	mean_Diabetes=mean_Diabetes/disease_percent.shape[0] 

	mean_hypertension=0

	for i in range(disease_percent.shape[0]):
	    mean_hypertension=mean_hypertension+disease_percent['hypertension'][i]
	    
	mean_hypertension=mean_hypertension/disease_percent.shape[0] 

	mean_Tuberculosis=0

	for i in range(disease_percent.shape[0]):
	    mean_Tuberculosis=mean_Tuberculosis+disease_percent['Tuberculosis'][i]
	    
	mean_Tuberculosis=mean_Tuberculosis/disease_percent.shape[0] 

	mean_Asthama=0

	for i in range(disease_percent.shape[0]):
	    mean_Asthama=mean_Asthama+disease_percent['Asthama'][i]
	    
	mean_Asthama=mean_Asthama/disease_percent.shape[0] 

	df=pd.DataFrame(p_district['HADM_ID'])
	df1=pd.DataFrame({'Diarrhoea_Dysentery':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'respiratory_infection':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'fever':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'Diabetes':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'hypertension':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'Tuberculosis':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)
	df1=pd.DataFrame({'Asthama':np.zeros(p_district.shape[0] )})
	df=pd.concat([df,df1],axis=1)

	for i in range(p_district.shape[0]):
	    for j in range(disease_percent.shape[0]):
	        if(p_district['District'][i]==disease_percent['State_District_Name'][j]):
	            if(disease_percent['Diarrhoea_Dysentery'][i]>=mean_diarrhoea):
	                df['Diarrhoea_Dysentery'][i]=1
	            if(disease_percent['respiratory_infection'][i]>=mean_resp):
	                df['respiratory_infection'][i]=1
	                
	            if(disease_percent['fever'][i]>=mean_fever):
	                df['fever'][i]=1
	            if(disease_percent['Diabetes'][i]>=mean_Diabetes):
	                df['Diabetes'][i]=1
	            if(disease_percent['hypertension'][i]>=mean_hypertension):
	                df['hypertension'][i]=1
	            if(disease_percent['Tuberculosis'][i]>=mean_Tuberculosis):
	                df['Tuberculosis'][i]=1
	            if(disease_percent['Asthama'][i]>=mean_Asthama):
	                df['Asthama'][i]=1
	                 
	                
	            break    
	        
	        
	patient_disease = open('file', 'w')
	df.to_csv("patient_disease.csv")


	dictt={'Diarrhoea_Dysentery':{"VitaminC", "Zinc", "Iron","Copper"}, 
	       'respiratory_infection': {"VitaminA","VitaminB12","VitaminC","Magnesium", "Calcium", "Potassium"},
	       'fever':{"Calcium", "Iron", "VitaminA", "VitaminBComplex", "VitaminC"},
	       'Diabetes':{"VitaminBComplex", "VitaminCVitaminD", "VitaminE", "Calcium"},
	       'hypertension':{"VitaminB6", "VitaminC", "VitaminD", "VitaminBComplex", "Calcium", "Iron", "Zinc", "Iodine", "Magnesium"},
	       'Tuberculosis':{"VitaminB6", "VitaminC"},
	       'Asthama':{"VitaminD", "VitaminC", "VitaminE"}}

	data_final=pd.DataFrame(p_district['HADM_ID'])


	output=[]

	for i in range(df.shape[0]):
	    l=[]
	    diss=set()
	    if(df['Diarrhoea_Dysentery'][i]==1.0):
	        l.append('Diarrhoea_Dysentery')
	    if(df['respiratory_infection'][i]==1):
	        l.append('respiratory_infection')
	                
	    if(df['fever'][i]==1):
	        l.append('fever')
	    if(df['Diabetes'][i]==1):
	        l.append('Diabetes')
	    if(df['hypertension'][i]==1):
	        l.append('hypertension')
	    if(df['Tuberculosis'][i]==1):
	        l.append('Tuberculosis')
	    if(df['Asthama'][i]==1):
	        l.append('Asthama')
	    
	    if len(l)==0:
	        text="Hey! Stay fit. Take healthy food. These are some health tips.  # Copy your kitty: Learn to do stretching exercises when you wake up."
	        text+="It boosts circulation and digestion,and eases back pain. # Don’t skip breakfast. Studies show that eating a proper breakfast is one of the most positive things you can do if you are trying to lose weight. Breakfast skippers tend to gain weight."
	        text+="A balanced breakfast includes fresh fruit or fruit juice, a high-fibre breakfast cereal, low-fat milk or yoghurt, wholewheat toast, and a boiled egg.  # Brush up on hygiene. Many people don't know how to brush their teeth properly. Improper brushing can cause as much damage to the teeth and gums as not brushing at all. Lots of people don’t brush for long enough, don’t floss and don’t see a dentist regularly. Hold your toothbrush in the same way that would hold a pencil, and brush for at least two minutes. "
	    else:
	        text="Hey! Your area is prone to many diseases and you should take care of yourself. We recommend your diet should contain "
	        for i in range(len(l)):
	            for j in dictt[l[i]]:
	                diss.add(j)
	        for i in diss:
	            text=text+" "+i+" "
	#     print(text)
	        for j in diss:
	            if j=="VitaminC":
	                text+="  You must have Broccoli, Brussels sprouts, and cauliflower,Tomatoes and tomato juice"
	                break
	            if j=="VitaminBComplex":
	                text+="  For example, liver, legumes, dried beans and fresh orange juice. Also, fortified bread, cereals and rice is loaded with folate. Vitamin B12 (Cobalamin): Natural sources of vitamin B12 are found in fish, red meat, eggs, poultry, milk, milk products and cheese. Soy products and cereals also have high vitamin B12 content."
	                break
	            if j=="Iron" or j=="Zinc":
	                text+="  green vegetables, for example spinach, silverbeet and broccoli.lentils and beans.nuts and seeds.grains, for example whole wheat, brown rice and fortified breakfast cereals.dried fruit."
	                break
	            else:
	                text+="  you must have Eggs, milk, carrots, sweet potatoes, and cantaloupe Oranges, strawberries, tomatoes, kiwi, broccoli, and red and green bell peppers"
	                break
	    
	    output.append(text)
	    
	output=pd.DataFrame(output)

	data_final=pd.concat([data_final,output],axis=1)
	for i in range(data_final.shape[0]):
		try:
			#print(data_final['HADM_ID'][i])
			test = str(data_final['HADM_ID'][i])
			print(data_final[0][i])
			user = User.objects.get(hadm_id=test)

			user.statement = data_final[0][i]
			user.save()
		except:
			print("fucked")