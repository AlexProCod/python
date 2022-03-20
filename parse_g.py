import urllib.request
import xml.dom.minidom as minidom


def get_data(xml_url):
    try:
        web_file = urllib.request.urlopen(xml_url)
        return web_file.read()
    except:
        pass


def get_currencies_dictionary(xml_content):
    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Record")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Sell':
                    if child.firstChild.nodeType == 3:
                        cod = child.firstChild.data
                if child.tagName == 'Buy':
                    if child.firstChild.nodeType == 3:
                        buy = float(child.firstChild.data.replace(',', '.'))
        currency_dict[buy] = cod
    return currency_dict


def print_dict(dict):
    for key in dict.keys():
        print(key, dict[key])


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/xml_metall.asp?date_req1=18/03/2022&date_req2=20/03/2022'
    currency_dict = get_currencies_dictionary(get_data(url))
    print_dict(currency_dict)
