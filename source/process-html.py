"""
After saving the html of a Career Center career fair event page's website
to a local file, run this script on the file to output the company names
and websites, in Markdown format (a bullet point list).
"""
from bs4 import BeautifulSoup
import sys

def main():
    if len(sys.argv) != 2:
        raise ValueError("Need input file as argument")
    input_filename = sys.argv[1]
    with open(input_filename, 'r') as file_obj:
        input_html = file_obj.read().replace('\n', '')
        soup = BeautifulSoup(input_html, 'html.parser')
        company_names_data = soup.find_all("td", class_="lst-cl_name")
        company_names = [td.get_text().rstrip() for td in company_names_data]
        company_websites_data = soup.find_all("td", class_="lst-cl_website")
        company_websites = [td.a.get('href') for td in company_websites_data]
        for i in range(len(company_names)):
            print '- [%s](%s)' % (company_names[i], company_websites[i])

if __name__ == "__main__":
    main()
