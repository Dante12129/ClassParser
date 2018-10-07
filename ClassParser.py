from bs4 import BeautifulSoup
import requests

def getAvailableSubjects(parsed_html):
    subjects_html = parsed_html.find(id='term_subj').find_all('option')
    subjects = {subject.string:subject['value'] for subject in subjects_html}
    return subjects

def getAvailableAttributes(parsed_html):
    attributes_html = parsed_html.find(id='attr').find_all('option')
    attributes = {attribute.string:attribute['value'] for attribute in attributes_html}
    return attributes

def getOpenCourses(subjects):
    with open('classes.txt', 'w', 1) as f:
        for full, subject in subjects.items():
            f.write(full + ':\n')
            response = requests.get('https://courselist.wm.edu/courselist/courseinfo/searchresults?term_code=201910&term_subj=%s&attr=0&attr2=0&levl=UG&status=OPEN&ptrm=0&search=Search' % subject)
            parsed = BeautifulSoup(response.text, 'html5lib')
            rows = parsed.find(id='results').find('table').find('tbody').find_all('tr')
            for row in rows:
                #print(row.find('td').find('a').string, end=' ')
                f.write(row.find('td').find('a').string + ' ')
                for data in row.find_all('td')[1:]:
                    #print(data.string, end=' ')
                    f.write(data.string + ' ')
                #print()
                f.write('\n')

response = requests.get('https://courselist.wm.edu/courselist')
parsed = BeautifulSoup(response.text, 'html5lib')
subjects = getAvailableSubjects(parsed)
attributes = getAvailableAttributes(parsed)
getOpenCourses({k:subjects[k] for k in subjects if k != 'ALL'})
