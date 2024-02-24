import re
import mechanize, requests
from bs4 import BeautifulSoup

output_file='set_numbers.txt'

def get_years():
	url_years = 'https://www.brickeconomy.com/sets'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	}
	response = requests.get(url_years, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	yearrows = soup.select('.panel-body > .yearwrap')
	
	years = [yearrow.contents[0].text for yearrow in yearrows]
	return years

def get_sets_from_page(page):
    numbers = []
    s = BeautifulSoup(page, features="html5lib")
    sets = s.find_all(class_='mb-5')
    for set in sets:
        uri = set.find('a').get('href')
        r = re.compile(r"set/([^/]+)")
        m = re.search(r, uri)
        numbers.append(m.group(1))
            
    return numbers

def get_sets_in_year(year):

    url = "https://www.brickeconomy.com/sets/year/" + str(year)
    br = mechanize.Browser()
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0')]

    br.open(url)
    
    set_numbers = get_sets_from_page(br.response().read())
    s = BeautifulSoup(br.response().read(), features="html5lib")
    saved_form = s.find('form', id='form1').prettify()

    br.select_form(nr=0)
    pageno = 2
    
    while True:
        
        # Find next page number link
        
        a = s.find('a', class_='page-link', string='Next')
        if not a:
            break
        parent = a.find_parent(class_='disabled')

        if parent:
            break
        
        r = re.compile(r"__doPostBack\('([^']+)")
        m = re.search(r, a['href'])
        event_target = m.group(1)
        
        r2 = re.compile(r"__doPostBack\('[^']+',\s*'([^']+)")
        m2 = re.search(r2, a['href'])
        event_arg = m2.group(1)

            # Regenerate form for next page
        html = saved_form.encode('utf8')
        resp = mechanize.make_response(html, [("Content-Type", "text/html")],
                                           br.geturl(), 200, "OK")

        br.set_response(resp)
        br.select_form(nr=0)
        br.form.set_all_readonly(False)
        br.form['__EVENTTARGET'] = event_target
        br.form['__EVENTARGUMENT'] = event_arg
        br.form.new_control('hidden', '__ASYNCPOST', {'value': 'true'})
        br.form.new_control('hidden', 'ctl00$ScriptManager1', {'value': 'ctl00$ContentPlaceHolder1$ctlSets$UpdatePanelMain|'+event_target})
        br.form.fixup()
        
        ctl = br.form.find_control('ctl00$ContentPlaceHolder1$ctlSets$cmdPBOwnedWantedChanged')
        br.form.controls.remove(ctl)
        ctl = br.form.find_control('ctl00$cmdRegionModalPB')
        br.form.controls.remove(ctl)
        ctl = br.form.find_control('ctl00$cmdDefault')
        br.form.controls.remove(ctl)
        ctl = br.form.find_control('ctl00$cmdLoginModalPB')
        br.form.controls.remove(ctl)
        ctl = br.form.find_control('ctl00$cmdSearchHeader2')
        br.form.controls.remove(ctl)
        ctl = br.form.find_control('ctl00$cmdSearchHeader')
        br.form.controls.remove(ctl)

        br.submit()
       
        # parse set numbers
        resp = br.response().read()
        r = re.compile(r"ContentPlaceHolder1_ctlSets_UpdatePanelMain\|([^|]+)")
        m = re.search(r, resp.decode('utf-8'))
        page_data = m.group(1)
        s = BeautifulSoup(page_data, features="html5lib")

        
        set_numbers += get_sets_from_page(page_data)
        pageno += 1
    
    return set_numbers
       

def get_all_sets(filename):
    records_file = open(filename, "a")
    years = get_years()
    for year in years:
        sets = get_sets_in_year(year)
        for set in sets:
            records_file.write(set + '\n')
	
get_all_sets(output_file)

