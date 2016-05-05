# word
这个用来从蜂巢获得关键词.

爬虫无非传递数据来着，重要的数据有以下
cookie
headers
ua
ip
data
url

了解这几个数据的传输可以爬去任何网站

对于scrapy来说，meddleware是一个比较难懂的点，但是现在看起来，meddleware的作用，仅仅用来处理代理问题就可以了，因为Request和RequestForm可以很容易传递出了代理之外的其他数据

那么，中继器的作用究竟是做什么呢
回到scrapy工作原理的框架之中，scrapy的特点是一个可以对采集的URL进行在处理的框架，有时候，我们不光采集一种页面，甚至我们不光采集一个网站，所以，分离出来headers头，cookie
，代理更方便我们管理，再来看，scrapy这点做的非常好，好到header头的ua和cookie都被分离出来

但是，越是细化越不方便人理解，最直观的就是，当我们在用scrapy的时候，数据放在哪？在哪里设置？如果像request一样，一股脑的扔进去，这样多容易理解，但这样，代码量就会大大加大

综上，我只是想说，如果你不理解scrapy，那就用scrapy自带request和requestform吧，虽然代码可能很丑

最后，总结scrapy可能有三个阶段
1，根据一些dome写一些脚本
2，对流程有一些自己的认识，并根据流程写脚本
3，对scrapy的设计原理有了深刻的认识