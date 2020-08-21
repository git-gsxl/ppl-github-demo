**=============  广深小龙-制作自动化测试框架之demo，欢迎各路大佬指点~  ===============**


简介：demo分为两个框架：①pytest     ②unittest 	  ③MySQL_diff

主要分享：web selenium 自动化测试框架  与  api request 自动化测试框架


1、unittest框架：unittest_demo


	1.api_packge：excel数据驱动设计模式
	    Python3 + unittest + request + excel ddt + HTMLTestRunner + 邮件通知
		--cases：用例excel编写、测试用例集合；
		--common：基类base request二次封装、excel读取封装、token获取封装、HTML报告模块、SQL操作封装；
		--report：run运行所以用例集合、邮箱发生错误用例时告知至个人邮箱
	使用注意：
		1.excel配置文件中设置host环境；
		2.token参数excel配置中设置；(access_token自行封装改进头部信息)
		3.tableName需与用例集合对应上；
		4.report邮箱需自行配置，sql配置；
	缺点挺多：很明显不灵活，还得不断改进(但好像又没必要)；
	
		
	2.web_packge：PageObject设计模式
        Python3 + unittest + selenium + HTMLTestRunner + 邮件通知
		--cases：测试用例集合；
		--common：基类base selenium二次封装、HTML报告模块、SQL操作封装、config封装；
		--pages: PageObject分模块封装页面元素；
		--report：run运行所以用例集合、邮箱发生错误用例时告知至个人邮箱；
	使用注意：		
		1.comon config配置文件中设置host环境、driver选择；
		2.report邮箱需自行配置，sql配置；
		3.base元素定位方法二次封装，要看懂会使用；


2、pytest框架：pytest_demo：


	1.api_packge: 类似PageObject设计模式
        Python3 + pytest + request + allure
		--api: api封装，类似PageObject设计模式
		--cases：pytest_conftest、测试用例集合；
		--common：基类base request二次封装、config配置url；
		--report: allure文件存储、渲染漂亮的报告；
	使用注意：
		1.pytest_conftest gettoken封装；
		2.access_token可加入直接传入，也可另封装；
		
		
	2.web_packge：PageObject设计模式
        Python3 + pytest + selenium + allure
		--cases：测试用例集合；
		--common：基类base selenium二次封装、HTML报告模块、SQL操作封装、config封装；
		--pages: PageObject分模块封装页面元素；
		--report：allure文件存储、渲染漂亮的报告；
	使用注意：		
		1.comon config配置文件中设置host环境、driver选择；
		2.base元素定位方法二次封装，要看懂会使用；
		
		
3、MySQL_diff：


	1.MySQL数据库的字段对比功能
	

最后：

	这只是一个简单demo，实际工作中还得结合项目的情况来各种封装，让其达到更好的效果；
	
	怎么不用yaml写用例? 答：喜欢用什么就用什么，yaml有助于以后集成到平台开发；
    
	Appium怎么没有demo? 答：有的，没有开源但也是各种封装，appium也很好用，不妨试试aritest；
	
	结合 jenkins 进行持续集成、分布式执行UI自动化脚本你需要了解更多 docker selenium；
	
	
关于我：在这里你将会了解到更多：https://www.cnblogs.com/gsxl/
	
	
	
