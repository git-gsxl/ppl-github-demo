from unittest_demo.web_package.common.base import Base

# 1.新增项目
loc_新增项目 = ('xpath', '/html/body/div[2]/div[1]/div[2]/ul[1]/li[2]/a')
loc_项目名称 = ('id', 'project_name')
loc_负责人 = ('id', 'responsible_name')
loc_测试人员 = ('id', 'test_user')
loc_开发人员 = ('id', 'dev_user')
loc_发布应用 = ('id', 'publish_app')
loc_简要描述 = ('id', 'simple_desc')
loc_其他信息 = ('id', 'other_desc')
loc_提交 = ('id', 'send')
loc_弹窗确定 = ('xpath', '//*[@id="my-alert"]/div/div[3]/span')

# 2.删除项目
loc_项目列表 = ('xpath', '/html/body/div[2]/div[1]/div[2]/ul[1]/li[1]/a')
loc_删除操作 = ('xpath', '//*[@id="project_list"]/table/tbody/tr[1]/td[9]/div/div/button[3]/span')
loc_确定操作 = ('xpath', '//*[@id="my-invalid"]/div/div[3]/span[2]')
loc_删除断言 = ('xpath', '//*[@id="project_list"]/table/tbody/tr/td[6]')


class Home(Base):

    def add_projects(self, project_name='hrun', responsible_name=u'小龙', test_user=u'广深小龙、漂亮的小姐姐', dev_user=u'程序猿、程序媛'):
        ''' 新增项目 '''
        self.click(loc_新增项目)
        self.send(loc_项目名称, project_name)
        self.send(loc_负责人, responsible_name)
        self.send(loc_测试人员, test_user)
        self.send(loc_开发人员, dev_user)
        self.send(loc_发布应用, '测试的发布应用')
        self.send(loc_简要描述, '这是小龙和妹子一起努力的成果')
        self.send(loc_其他信息, '我可以不写吗？')
        self.click(loc_提交)

        if self.is_alert():
            self.click(loc_弹窗确定)


    def del_project(self):
        self.click(loc_项目列表)
        self.click(loc_删除操作)
        self.click(loc_确定操作)

    def exp(self):
        self.driver.refresh()
        self.click(loc_项目列表)
        try:
            res = self.get_text(loc_删除断言)
            if len(res) > 1:
                return False
            else:return True
        except: return True
