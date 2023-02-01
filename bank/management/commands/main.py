from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import NoSuchElementException
from django.core.management.base import BaseCommand
from bank.models import *
WINDOW_SIZE = "1920,1080"


class parser:

    def __init__(self,url):

        self.element=None
        self.url=url

    def baza(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(executable_path='/home/jet/Видео/chromedriver', options=options)
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        url = self.url
        driver.get(url)
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(60)
        try:
            self.element = WebDriverWait(driver, 15).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[6] '))
                )
        except:
            print('404')

    def found_element(self):

        usual = self.element.find_elements(By.CLASS_NAME, 'SitesSerp__items')

        sums = 0
        for k in usual:
            c = k.find_elements(By.CSS_SELECTOR, 'div.SiteSnippetSearch')
            sums += 3
            print(sums)

            for j in c:
                name = j.find_element(By.CLASS_NAME, 'SiteSnippetSearch__heading').text
                # print(name

                Gallerys = []
                link = j.find_element(By.CSS_SELECTOR, 'a.Link.Link_js_inited').get_attribute("href")  # link

                description = j.find_element(By.CLASS_NAME, 'SiteSnippetSearch__contentWrapper').find_element(
                    By.CSS_SELECTOR, 'div.SiteSnippetSearch__content').find_element(By.CSS_SELECTOR,
                                                                                    'div.SiteSnippetSearch__content_body').find_element(
                    By.CSS_SELECTOR, 'div.SiteSnippetSearch__description').text #описание


                street = j.find_element(By.CLASS_NAME, 'SiteSnippetSearch__contentWrapper').find_element(By.CLASS_NAME,
                                                                                                         'SiteSnippetSearch__content').find_element(
                    By.TAG_NAME, 'p').text

                try:
                    metro = j.find_element(By.CLASS_NAME, 'SiteSnippetSearch__contentWrapper').find_element(
                        By.CLASS_NAME, 'SiteSnippetSearch__content').find_element(By.CLASS_NAME,
                                                                                  'SiteSnippetSearch__info').find_element(
                        By.CSS_SELECTOR, 'span.MetroStation__title').text
                except NoSuchElementException:
                    pass
                # print(metro)
                try:
                    Gallery__item = j.find_elements(By.CLASS_NAME, 'Lazy')

                    for i in Gallery__item:
                        dfdf = i.find_elements(By.TAG_NAME, 'img')
                        for e in dfdf:
                            # print(e.get_attribute("src"))
                            Gallerys.append(e.get_attribute("src"))

                except NoSuchElementException :
                    pass


                infos=[]
                try:#цены ,площать ,тип
                    information_costs = j.find_element(By.CLASS_NAME, 'SiteSnippetSearch__contentWrapper').find_element(
                        By.CSS_SELECTOR, 'div.SiteSnippetSearch__content').find_element(By.CSS_SELECTOR,
                                                                                        'div.SiteSnippetSearch__content_body').find_element(
                        By.CSS_SELECTOR, 'div.SnippetPriceTable').find_elements(By.CLASS_NAME, 'SnippetPriceTable__row')
                    for i in information_costs:
                        title = i.find_elements(By.CLASS_NAME, 'SnippetPriceTable__title')
                        area = i.find_elements(By.CLASS_NAME, 'SnippetPriceTable__area')
                        price = i.find_elements(By.CLASS_NAME, 'SnippetPriceTable__price')


                        for info in title:

                            infos.append(info.text)

                        for info in area:

                            infos.append(info.text.split()[1])


                        for info in price:

                            s=''
                            for d in info.text.split()[1:4]:
                                s += d
                            infos.append(s)

#

                    title=infos[0]

                    try:
                        title1 = infos[6]
                    except IndexError:
                        title1 = ''

                    try:
                        title2 = infos[9]
                    except IndexError:
                        title2 = ''
                    try:
                     title3 = infos[12]
                    except IndexError:
                        title3=''
                    try:
                     title4 = infos[15]

                    except IndexError:
                        title4 = ''

                    area=infos[1]

                    try:
                        area1 = infos[4]
                    except IndexError:
                        area1 = ''
                    try:
                        area2 = infos[7]
                    except IndexError:
                        area2 = ''

                    try:
                        area3 = infos[10]
                    except IndexError:
                        area3 = ''
                    try:
                        area4 = infos[13]

                    except IndexError:
                        area4 = ''

                    prices = infos[2]
                    try:
                        prices1 = infos[5]
                    except IndexError:
                        prices1 = ''
                    try:
                        prices2 = infos[8]
                    except IndexError:
                        prices2 = ''
                    try:
                        prices3 = infos[11]
                    except IndexError:
                        prices3 = ''
                    try:
                        prices4 = infos[14]

                    except IndexError:
                        prices4 = ''

                except NoSuchElementException :
                      pass

                try:#картики
                    Gallery__item = j.find_elements(By.CLASS_NAME, 'Lazy')

                    for i in Gallery__item:
                        dfdf = i.find_elements(By.TAG_NAME, 'img')
                        for e in dfdf:
                            # print(e.get_attribute("src"))
                            Gallerys.append(e.get_attribute("src"))

                except NoSuchElementException :
                    pass
                try:
                    a = homes.objects.get(complex=name)

                except homes.DoesNotExist:
                    p = homes(
                        complex=name,
                        link=link,
                        street=street,
                        description=description,
                        metro=metro,
                        photo=Gallerys[0],# первая картинка
                    ).save()

                try:
                        p = housing_cost.objects.get(
                            complex=homes.objects.get(complex=name))

                except housing_cost.DoesNotExist:
                     p = housing_cost(
                           complex=homes.objects.get(complex=name),
                           title = title,
                           title1 = title1,
                           title2 = title2,
                           title3 = title3,
                           title4 = title4,
                           area = area,
                           area1 = area1,
                           area2 = area2,
                           area3 = area3,
                           area4 = area4,
                           prices = prices,
                           prices1=prices1,
                           prices2 = prices2,
                           prices3 = prices3,
                           prices4 = prices4,
                          ).save()

class Command(BaseCommand):

 def handle(self, *args, **options):

     a=parser("https://realty.ya.ru/moskva_i_moskovskaya_oblast/kupit/novostrojka/")
     a.baza()
     a.found_element()


