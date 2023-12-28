import requests
import tempfile
import os
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup
from datetime import datetime



#  Getting the response --DONE
# Sending the response as a text message(Date -> Links) --DONE
# Applying the Pdf Logic To alter the html to pdf -DONE 
# Completing the Other Research, Weekly and Daily newsletter --DONE
# 
def get_newspaper(url):
    """Get daily Newspaper for a zodiac sign.

    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    params = {}
    response = requests.get(url, params)
    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.find_all('tr')

    data_dict_list = {}

    #  Iterate through each row and extract date and link
    for row in rows:
        folder_name = row.select_one('td:nth-of-type(2)').text.strip()
        date = row.find('td').text.strip()
        link = row.find('a')['href']

    # Create a dictionary for each row
        pdf_link = download_pdf(date ,link , folder_name) if link.endswith('.pdf') else convert_html_to_pdf(date, link, folder_name)
        data_dict_list[date] = pdf_link


        
    print(f"11111 inside get_newspaper {data_dict_list}")
    return data_dict_list


def convert_html_to_pdf(date, link, folder_name='Daily NewsLetter pdf'):
    # using for only one
    # response = requests.get(links[0])
    # soup = BeautifulSoup(response.content)
    # pdf = pydf.generate_pdf(soup)
    # current_directory = os.getcwd()
    os.makedirs(folder_name, exist_ok=True)
    filename = f'Daily_Newsletter_{date}.pdf'
    file_path = os.path.join(folder_name, filename)
    pdf_options = {'page-size': 'A3','margin-top': '10mm','margin-right': '10mm','margin-bottom': '10mm','margin-left': '10mm'}
    HTML(link).write_pdf(file_path, stylesheets=[CSS(string='@page { size: A3; margin: 10mm; }')], pdf_options=pdf_options)

    print(f"11111 inside convert_html_to_pdf {file_path}")
    return file_path

def download_pdf(date, link, folder_name):
    os.makedirs(folder_name, exist_ok=True)
    filename = f'{folder_name.replace(" ", "_")}_{date}.pdf'
    file_path = os.path.join(folder_name, filename)
    response = requests.get(link)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    return file_path
