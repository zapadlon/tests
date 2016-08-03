__author__ = 'zapadlo'
import requests
import lxml.html as html
#import time
#t1=time.time()
class avito_grab():

    def get_urls(self, base_url,css_selector,attr='href'):
        self.base_url = base_url
        self.css_selector = css_selector
        self.attr = attr

        self.page = requests.get(self.base_url)
        self.page_body = html.fromstring(self.page.text).cssselect(self.css_selector)
        return [x.get(self.attr) for x in self.page_body]
#### test ###
if __name__ == '__main__':
    css_selector = 'div.item a.item-description-title-link'
    base_url = 'https://www.avito.ru/sevastopol/velosipedy'
    attr = 'href'
    a = avito_grab()
    print(set(a.get_urls(base_url,css_selector,attr)))
    print(len(a.get_urls(base_url,css_selector,attr)))
    print((len(set(a.get_urls(base_url,css_selector,attr)))))
#############
#######