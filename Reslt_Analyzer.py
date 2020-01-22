import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_df(): #creating a new data frame
        df = pd.DataFrame(columns=['no_of_std', 'passed', 'prommoted', 'detained'])
        return df

def append_df(df,nos, pas, prom, det, dept): # appending data frames to main data frame
        data = {'no_of_std':nos, 'passed': pas, 'prommoted': prom, "detained": det, 'department': dept}
        temp_df = pd.DataFrame(data, columns=['no_of_std','passed', 'prommoted', 'detained'], index=[dept])# creating a temporary data frame
        df = df.append(temp_df,sort=False)
        return df


def fetch_result(batch_year,url):
        dept_code = 732 # department code of first department (civil) of my college
        for _ in range(8):
            start_roll_no = int("1604" + str(batch_year) + str(dept_code) + "001")# genertae roll numbers for every department
            end_roll_no = start_roll_no + 120# Each department will have maximum of 120 students
            passed = 0
            prommoted = 0
            detained = 0
            count=0
            print("FETCHING RESULTS OF " + str(dept_code))
            for rno in range(start_roll_no , end_roll_no,url): #fetch results of  each student
                         try:
                                page = requests.post(url, data={'htno': rno, 'mbstatus': 'SEARCH'})
                                soup = BeautifulSoup(page.content, 'html.parser')
                                result_table = soup.find(id='AutoNumber5')  # Find the table with final result
                                result_rows = result_table.find_all('tr')  # Dividing the table into a list of rows
                                result_row = result_rows[-1].find_all('td')  # Generally Row 3 (indexed 2) has sgpa (or last row in case of 'promoted' case), so divide row-3 into columns
                                sgpa = str(result_row[2].get_text()).strip()  # Extract sgpa from column 3 (indexed 2)
                                #print(sgpa)  #for printing the result of every student

                                if sgpa[1]=="A":
                                    #print(name)
                                    passed+=1
                                    #print("no of passed "+str(passed))
                                elif sgpa[1]=="R":
                                        prommoted+=1
                                        #print("prommoted "+str(prommoted))
                                else:
                                         detained += 1
                                         #print(name+" detained")
                         except :
                             print('\n' + str(rno) + " - Doesn't exists")
                             count+=1
            no_of_std = 120-count # calculating number of students in each department 
            if dept_code== 732:
                 result_df = create_df()
            result_df = append_df(result_df,no_of_std, passed, prommoted, detained, dept_code)
            if dept_code==739:
                    return result_df
            dept_code+=1
def vidualize(df):
    passed=df['passed'].tolist() #converting a column into a list
    prommoted=df['prommoted'].tolist()
    detained=df['detained'].tolist()
    no_of_std=df['no_of_std'].tolist()
    for i in range(len(no_of_std)): # calculating the percentage of passed,prommoted and detained students of each department
        nos = no_of_std[i]
        pas = (passed[i] / nos) * 100
        prom = (prommoted[i] / nos) * 100
        det = (detained[i] / nos) * 100
        passed[i] = round(pas)
        prommoted[i] = round(prom)
        detained[i] = round(det)
    labels=['CIVIL('+str(no_of_std[0])+')','CSE('+str(no_of_std[1])+')','ECE('+str(no_of_std[2])+')','EEE('+str(no_of_std[3])+')','INS('+str(no_of_std[4])+')',
            'IT'+str(no_of_std[5])+')','MECH'+str(no_of_std[6])+')','PRO'+str(no_of_std[7])+')']
    barWidth = 0.25
    r1 = np.arange(len(detained))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    # Make the plot
    plt.bar(r1, detained, color='#FFD700', width=barWidth, edgecolor='white', label='detained')
    plt.bar(r2, prommoted, color='#557f2d', width=barWidth, edgecolor='white', label='prommoted')
    plt.bar(r3, passed, color='#2d7f5e', width=barWidth, edgecolor='white', label='passed')
    plt.ylabel('percentage')
    plt.title('result  analyzer')
    plt.xlabel('departments', fontweight='bold',fontsize = 18)
    plt.xticks([r + barWidth for r in range(len(detained))], labels)
    plt.legend()
    plt.tight_layout()
    plt.show()
def main():

    batch_year =  0
    while (True):
        batch_year= int(input("Enter the batch number  \n note: 17 the is batch year of roll_no=160417737001 \n"))
        if len(str(batch_year)) == 2:
            break
        else:
            print("please enter correct information")
    url=str(input("paste the url of results website "))
    results_df= fetch_result(batch_year)
    print(results_df)
    vidualize(results_df)
main()
