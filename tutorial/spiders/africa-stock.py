import scrapy


class AfricaStock(scrapy.Spider):
    name = "africa-stock"
    start_urls = [
        "https://www.african-markets.com/en/stock-markets/brvm"
    ]

    def parse(self, response):
        uls = response.xpath("//ul[@id='jmm-tabs1101']/li")
        content_div = response.xpath("//div[@class='tab-content']/div['tab-pane']")
        i = 0
        for indexli in uls:
            result = {
                "kategori": uls[i].css("span::text").get()
            }
            content_table = content_div[i].css('tbody tr')
            for tr in content_table:
                ltd = tr.css("td")
                result["list"] = {
                    "company" : ltd[0].css("td a::text").get(),
                    "point" : ltd[1].css("td::text").get(),
                    "growth" : ltd[2].css("td::text").get(),
                    "date" : ltd[3].css("td::text").get(),
                }
                yield result
            i += 1
