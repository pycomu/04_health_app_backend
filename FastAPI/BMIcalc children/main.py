# https://python.plainenglish.io/rest-api-for-beginners-with-python-fastapi-86fa84fcda42

# Importing the FastApi class
from fastapi import FastAPI, Request
import uvicorn
import pandas as pd

# Creating an app object
app = FastAPI()

def calculation (df,child_age, child_bmi):
    y =0
    p_child = 0
    for age in df['Age_months']:
        if age > child_age:            
            for colomn in range(1,11):
                if df.iat[y,colomn] > child_bmi:
                
                    bmi_min = df.iat[y,colomn-1]
                    bmi_max = df.iat[y,colomn]
                    p_max = df.iat[219,colomn]
                    p_min = df.iat[219,colomn-1]
                    p_child = round((p_max-p_min) * (child_bmi-bmi_min) / (bmi_max-bmi_min) +p_min)
                    
                    # print("child_bmi ",child_bmi)
                    # print("bmi_min ",bmi_min, "bmi_max ", bmi_max)
                    # print("p_min ", p_min , "p_max ",p_max)
                    # print("the percentile is ",p_child,"%")
                    break
            break
        y += 1
    return p_child


@app.post("/bmicalc_child") # gender is 1 male and 0 female, age in months from 24 to 240.5
# async def calc_bmi(age_m:int, gender: int,height: int, weight: int): 
async def calc_bmi(info : Request):
    input = await info.json()
    age_m = input["age"]
    gender = input["gender"]
    height = input["height"]
    weight = input["weight"]

    result = round(weight/ (height/100*height/100),2)
    
    if age_m < 24 or age_m > 240.5:
        return {"error": "ERROR - Age in months {} is out of range (24 - 240.5)".format(age_m)}

    if gender == 1:
        if result < 13.52747 or result > 32.41344:
            return {"percentile":"ERROR ","error": "Calc.BMI {} is out of range".format(result)}
        df = pd.read_csv("BMIcalc children/bmi_age_male.csv", delimiter=',') # take care of working path !
        p_info = calculation (df, age_m, result)
        

    elif gender == 0:
        if result < 13.21253 or result > 35.10556:
            return {"percentile":"ERROR ","error": "Calc.BMI {} is out of range".format(result)}
        df = pd.read_csv("BMIcalc children/bmi_age_female.csv", delimiter=',') # take care of working path !
        p_info = calculation (df, age_m, result)
        
    else:
        return {"error": "ERROR - Gender must be 1 / male or 0 / female"}



    return {"height":height,
            "weight":weight,
            "gender": gender,
            "age_months":age_m,
            "BMI_calc": result,
            "percentile":p_info,
            "error":"",
            } 
    # no html page rendered as response !
    

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

