import scrapy
from covid_ontario.items import CovidOntarioItem
from scrapy.utils.response import open_in_browser
from datetime import datetime
import time

class OntarioSpider(scrapy.Spider):
    name = 'ontario'
    allowed_domains = ['www.ontario.ca']
    start_urls = ['https://www.ontario.ca/page/2019-novel-coronavirus']

    def parse(self, response):
        status_item = CovidOntarioItem()
        # some debugging here, remove it when you're done
        self.logger.warning('Table HTML %s', response)
        open_in_browser(response)
        status_dict = {
            'Number of cases': 'confirmed',
            'Resolved': 'resolved',
            'Deceased': 'deceased',
            'Currently under investigation': 'pending',
            'Total tests completed': 'total',
            'Male': 'male',
            'Female': 'female',
            '19 and under': 'youth',
            '20': '20-39',
            '40': '40-59',
            '60': '60-79',
            '80 and over': 'senior',
        }
        daily_data = {}
        for row in response.xpath('//table[1]/tbody/tr'):
            name = row.xpath(
                'td[1]/descendant-or-self::*/text()').get().strip()
            value = row.xpath(
                'td[2]/descendant-or-self::*/text()').get().strip()
            for label, key in status_dict.items():
                if name and value and label in name:
                    value = int(value.replace(',', ''))
                    # self.logger.warning('Table HTML %s', name)
                    # self.logger.warning('Label %s', name)
                    # self.logger.warning('Value HTML %s', name)
                    daily_data[key] = value

        # self.logger.warning('Daily Data %s', daily_data)
        status_item['confirmed'] = {
            'total': daily_data['confirmed'],
            'male': daily_data['male'],
            'female': daily_data['female'],
            'youth': daily_data['youth'],
            '20-39': daily_data['20-39'],
            '40-59': daily_data['40-59'],
            '60-79': daily_data['60-79'],
            'senior': daily_data['senior'],

        }

        status_item['deceased'] = daily_data['deceased']
        status_item['pending'] = daily_data['pending']
        status_item['resolved'] = daily_data['resolved']
        status_item['total'] = daily_data['total']

        today_date = datetime.date(datetime.now())
        date_timestamp = time.mktime(today_date.timetuple())
        status_item['date'] = date_timestamp
        yield status_item