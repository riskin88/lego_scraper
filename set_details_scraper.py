import requests, random, math
import sys, os
from bs4 import BeautifulSoup

set_number_filename = 'set_numbers.txt'
output_table_filename = 'lego_sets.csv'

url_base = 'https://www.brickeconomy.com/set/'
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	}
keywords = [
		"Name",
		"Theme",
		"Subtheme",
		"Year",
		"Released",
		"Retired",
		"Availability",
		"Pieces",
		"Minifigs",
		"Retail price",
		"Value",
		"Growth",
		"Annual growth",
		"2023 growth",
		"Rolling growth",
		"Future growth",
		"Value",
		"Range"
		]
		

def get_sets(set_numbers):
    with open(output_table_filename, "a") as output_file:
        # Check if the file is empty and if so, write the header
        output_file.seek(0, os.SEEK_END)
        if output_file.tell() == 0:
            output_file.write('Set number; ')
            for keyword in keywords:
                output_file.write(keyword + '; ')
            output_file.write('\n')
        for set in set_numbers:
            get_setdata(set, output_file)

def get_random_set_numbers(n, src_filename):
    with open(src_filename, 'r') as file:
        lines = file.readlines()
        if lines:
            random_lines = random.sample(lines, n)
            return [line.strip() for line in random_lines]  # Strip newline characters
        else:
            return []
            
def get_all_numbers(src_filename):
    with open(src_filename, 'r') as file:
        lines = file.readlines()
        if lines:
            return [line.strip() for line in lines]  # Strip newline characters
        else:
            return []

def get_numbers_paged(src_filename, offset, limit):
    with open(src_filename, 'r') as file:
        lines = file.readlines()
        start_index = offset
        end_index = offset + limit

        if start_index >= len(lines):
            paged_lines = []
        else:
            paged_lines = lines[start_index:end_index]

        return [line.strip() for line in paged_lines]  # Strip newline characters

def get_setdata(id, records_file):
	url = url_base + id + "/"
	
	response = requests.get(url, headers=headers)

		
	soup = BeautifulSoup(response.text, 'html.parser')
	rows = soup.select('#ContentPlaceHolder1_SetDetails > .side-box-body > .rowlist') + soup.select('#ContentPlaceHolder1_PanelSetPricing > .side-box-body > .rowlist')


	div_index = 0
	records_file.write(id + '; ')
	for keyword in keywords:
		start_index = div_index
		while div_index < len(rows):
		    keyword_div = rows[div_index].select_one('.col-xs-5').find(string=lambda text: text and keyword in text)
		    if keyword_div:
		        value = keyword_div.find_parent(class_="col-xs-5").find_next_sibling().text.strip()
		        records_file.write(value + '; ')
		        ++div_index
		        break
		    div_index += 1
		else:
		    div_index = start_index
		    records_file.write('; ')
		    
		    
	records_file.write('\n')
	
	
	
if len(sys.argv) > 2:
    try:
        offset = int(sys.argv[1])
        limit = int(sys.argv[2])
        get_sets(get_numbers_paged(set_number_filename, offset, limit))
    except ValueError:
        print("Argument is not a number!")
else:
    get_sets(get_all_numbers(set_number_filename))
