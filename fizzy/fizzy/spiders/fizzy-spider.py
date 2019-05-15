from fizzy.items import Transaction
import scrapy

class FizzySpider(scrapy.Spider):
    name = "fizzy"
    start_urls = ['https://etherscan.io/txs?a=0xe083515d1541f2a9fd0ca03f189f5d321c73b872&ps=100',]
    allowed_domains = ['etherscan.io']

    def parse(self, response):
        for transaction in response.css('span.text-truncate a'):
            if transaction.css('a::attr(href)')[0].extract().startswith("/tx/"):
                yield response.follow(transaction, callback = self.parse_transaction)

        for page in response.css('ul.pagination:nth-child(1) > li:nth-child(4) > a:nth-child(1)'):
            yield response.follow(page, callback = self.parse)

    def parse_transaction(self, response):
        
        #transaction data
        try:
            txHash = response.css('#spanTxHash::text').extract_first().strip()
        except:
            txHash = response.css('div#tx::text').extract_first().strip()
        
        try:
            txReceiptStatus = response.css('.u-label--sm::text').extract_first().strip()
        except:
            txReceiptStatus = response.css('div.col-sm-9:nth-child(4) > span:nth-child(1) > font:nth-child(1)::text').extract_first().strip()

        try:    
            blockHeight = response.css('#ContentPlaceHolder1_maintable > div:nth-child(5) > div:nth-child(2) > a:nth-child(1)::text').extract_first().strip()
        except:
            blockHeight = response.css('div.col-sm-9:nth-child(6) > a:nth-child(1)::text').extract_first().strip()

        try:
            timeStamp = response.css('div.align-items-center:nth-child(7) > div:nth-child(2)::text')[1].extract()
        except:
            timeStamp = response.css('div.col-sm-9:nth-child(8)::text').extract_first().strip()

        try:    
            fromAddress = response.css('#addressCopy::text').extract_first().strip()
        except:
            fromAddress = response.css('div.col-sm-9:nth-child(10) > a:nth-child(1)::text').extract_first().strip()

        try:    
            toAddress = response.css('#contractCopy::text').extract_first().strip()
        except:
            toAddress = response.css('a.wordwrap::text').extract_first().strip()

        try:
            value = response.css('.u-label--value::text').extract_first().strip()
        except:
            value = response.css('#ContentPlaceHolder1_spanValue::text').extract_first().strip()

        try:
            gasLimit = response.css('#ContentPlaceHolder1_spanGasLimit::text').extract_first().strip()
        except:
            gasLimit = response.css('#ContentPlaceHolder1_spanGasLimit::text').extract_first().strip()

        try:
            gasUsed = response.css('#ContentPlaceHolder1_spanGasUsedByTxn::text').extract_first().strip()
        except:
            gasUsed = response.css('#ContentPlaceHolder1_spanGasUsedByTxn::text').extract_first().strip()

        try:    
            gasPrice = response.css('#ContentPlaceHolder1_spanGasPrice::text')[1].extract().strip()
        except:
            gasPrice = response.css('#ContentPlaceHolder1_spanGasPrice::text')[1].extract().strip()

        try:
            actualCost = response.css('#ContentPlaceHolder1_spanTxFee::text')[1].extract().strip()
        except:
            actualCost = response.css('#ContentPlaceHolder1_spanTxFee::text')[1].extract().strip()

        try:
            nonce = response.css('div.mn-3:nth-child(7) > div:nth-child(2) > span:nth-child(1)::text').extract_first().strip()
        except:
            nonce = response.css('div.col-sm-9:nth-child(24) > span:nth-child(1)::text').extract_first().strip()

        try:
            inputData = response.css('#inputdata::text').extract_first()
        except:
            inputData = response.css('#inputdata::text').extract_first()

        #event data
        eventName = response.css("#funcname_0::text").extract_first()
        eventParam1 = response.css('#chunk_1_1::text').extract_first()
        eventParam2 = response.css('#chunk_1_2::text').extract_first()
        eventParam3 = response.css('#chunk_1_3::text').extract_first()
        eventParam4 = response.css('#chunk_1_4::text').extract_first()
        eventParam5 = response.css('#chunk_1_5::text').extract_first()



        yield Transaction(
            txHash = str(txHash),
            txReceiptStatus = str(txReceiptStatus),
            blockHeight = str(blockHeight),
            timeStamp = str(timeStamp),
            fromAddress = str(fromAddress),
            toAddress = str(toAddress),
            value = str(value),
            gasLimit = str(gasLimit),
            gasUsed = str(gasUsed),
            gasPrice = str(gasPrice),
            actualCost = str(actualCost),
            nonce = str(nonce),
            inputData = str(inputData),
            eventName = str(eventName),
            eventParam1 = str(eventParam1),
            eventParam2 = str(eventParam2),
            eventParam3 = str(eventParam3),
            eventParam4 = str(eventParam4),
            eventParam5 = str(eventParam5),
        )
