import requests
from bs4 import BeautifulSoup

for rno in range(160417737090, 1604177370101):
    page = requests.post('https://www.osmania.ac.in/res07/20190855.jsp', data={'htno': rno, 'mbstatus': 'SEARCH'})
    soup = BeautifulSoup(page.content, 'html.parser')
    name_table = soup.find(id='AutoNumber3')  # Find the table with student details (name, fname etc)
    name_rows = name_table.find_all('tr')  # Dividing the table into list of rows
    name_row = name_rows[2].find_all('td')  # Row 3 (indexed 2) has name, so divide row-3 into columns
    name = name_row[1].get_text()
    print(name)
    subjects = []  # We'll store subject names here
    grades = []  # This is for grade points for same indexed subject in subjects[]
    score_table = soup.find(id='AutoNumber4')  # Find the table with score
    score_rows = score_table.find_all('tr')  # Dividing the table into a list of rows
    for row in range(2, len(score_rows)):  # Since actual data starts from row 3 (indexed 2)
        score_cols = score_rows[row].find_all('td')  # Dividing each row into columns
        subjects.append(str(score_cols[1].get_text()).lstrip(
            '\xa0'))  # Extracting subject from column 2 (indexed 1) and removing escape chars\
        grades.append(str(score_cols[3].get_text()).lstrip(
            '\xa0'))  # Extracting the score for the same subject and removing escape chars'''

    result_table = soup.find(id='AutoNumber5')  # Find the table with final result
    result_rows = result_table.find_all('tr')  # Dividing the table into a list of rows
    result_row = result_rows[-1].find_all(
        'td')  # Generally Row 3 (indexed 2) has sgpa (or last row in case of 'promoted' case), so divide row-3 into columns
    sgpa = str(result_row[2].get_text()).strip()  # Extract sgpa from column 3 (indexed 2)

    print(sgpa)