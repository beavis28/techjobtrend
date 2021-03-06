import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule

from socareers.items import JobItem

class SOSpider(scrapy.Spider):
    name="socareers"
    allowed_domains = ["careers.stackoverflow.com","stackoverflow.com"]

    start_urls = [
        "http://careers.stackoverflow.com/jobs?searchTerm=&type=&location=&range=20&distanceUnits=Km",
    ]
    job_ids = set()


    def parse(self, response):
        for sel in response.xpath('//div[@data-jobid]'):
            id =''.join(sel.xpath('@data-jobid').extract())
            item = None
            if id not in self.job_ids:
                item = JobItem()
                item['_id'] = id
                item['title'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/h2/a/text()').extract())
                item['company'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/div[@class="-name"]/text()').extract()).strip()
                item['location'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/div[@class="-location"]/text()').extract()).strip()

                if sel.xpath('div[@class="-job-summary "]/div/span[@class="-salary"]/text()').extract():
                    item['salary'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/span[@class="-salary"]/text()').extract()).strip()
                else:
                    item['salary'] = ""

                if sel.xpath('div[@class="-job-summary "]/div/span[@class="-remote"]/text()').extract():
                    item['remote'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/span[@class="-remote"]/text()').extract()).strip()
                else:
                    item['remote'] = ""

                #if sel.xpath('div[@class="-job-summary "]/div/span[@class="-visa"]/text()').extract():
                #    item['visa'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/span[@class="-visa"]/text()').extract()).strip()
                #else:
                #    item['visa'] = ""

                #if sel.xpath('div[@class="-job-summary "]/div/span[@class="-relocation"]/text()').extract():
                #    item['relocation'] = ''.join(sel.xpath('div[@class="-job-summary "]/div/span[@class="-relocation"]/text()').extract()).strip()
                #else:
                #    item['relocation'] = ""

                item['tags'] = sel.xpath('div[@class="-job-summary "]/div/p/a/text()').extract()
            else:
                print "duplicate"

            yield item
        next_page = response.css("div.pagination > a.test-pagination-next::attr('href')").extract()
        if next_page:
            url = response.urljoin(next_page[0])
            yield scrapy.Request(url, self.parse)
