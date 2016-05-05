#coding:utf-8

import scrapy,MySQLdb

class DmozSpider(scrapy.Spider):
    name = "word"

    # start_urls = [
    #    'http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/word&reqid=1462424853001_96'
    # ]

    def start_requests(self):


        formdata = {
            'params':'{"logid":-1,"query":"python","querySessions":["seo","seo","seo"],"querytype":1,"regions":"0","device":0,"rgfilter":1,"entry":"kr_station","planid":"0","unitid":"0","needAutounit":false,"filterAccountWord":true,"attrShowReasonTag":[],"attrBusinessPointTag":[],"attrWordContainTag":[],"showWordContain":"","showWordNotContain":"","pageNo":1,"pageSize":300,"orderBy":"","order":"","forceReload":true}',
            'source':'',
            'path':'jupiter/GET/kr/word',
            'userid':'10270352',
            'token':'6916277015f8fa2a72b343e24a90274da28822e988474ff0f5b4e75f8a9b4cbf997f9e74eb0599690bd278a4',
            'eventId':'1462424853001_80'
        }

        cookies = {
            'BAIDUID':'983CD6DE1D34D6962694CB315B1B4E25',
            'FG':'1',
            'BIDUPSID':'983CD6DE1D34D6962694CB315B1B4E25',
            'PSTM':'1458620335',
            'BDUSS':'np5eDMwVGI1MUlkUDlRemU4UTljNnpoSEtPY3Z3Y2piY3JyQ3EwclpkVmFQQ3hYQVFBQUFBJCQAAAAAAAAAAAEAAACr3u8LYmFmZWl0ZXdvY2FvAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFqvBFdarwRXS',
            '__cfduid':'ddd3a561f810bcab04ec2022220043ceb1461225032',
            'pgv_pvi':'9764871168',
            'SIGNIN_UC':'70a2711cf1d3d9b1a82d2f87d633bd8a02124313088',
            'uc_login_unique':'8b739051d4237158267fce108a711273',
            '__cas__st__3':'6916277015f8fa2a72b343e24a90274da28822e988474ff0f5b4e75f8a9b4cbf997f9e74eb0599690bd278a4',
            '__cas__id__3':'10270352',
            '__cas__rn__':'212431308',
            'SAMPLING_USER_ID':'10270352'
        }

        return [scrapy.FormRequest('http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/word&reqid=1462424853001_96',
                                   formdata = formdata,
                                   cookies= cookies,
                                   callback=self.parse)
                ]

    def parse(self, response):
        print response.body