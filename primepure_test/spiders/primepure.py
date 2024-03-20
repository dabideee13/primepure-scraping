import scrapy


class PrimepureSpider(scrapy.Spider):
    name = "primepure"
    start_urls = ["https://primepureglobal.com"]

    def parse(self, response):
        headers = response.xpath('//div[@class="header-item header-item--navigation text-center"]//a/text()').extract()
        print(f'Headers: {self.clean_headers(headers)}')

    def clean_header(self, header: str) -> str:
        return header.replace('/n', '').strip()

    def clean_headers(self, headers: list[str]) -> list[str]:
        return [self.clean_header(header) for header in headers]

    def format_headers(self, headers: list[str]) -> str:
        return ','.join(headers)