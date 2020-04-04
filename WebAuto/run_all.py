import unittest
from common import HTMLTestRunner_cn
# 用例的路径
casePath="E:\\SaasWebAuto\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
# print(discover)

# 报告路径
reportPath="E:\\SaasWebAuto\\report\\"+"reslut.html"
# 找到报告的路径并写入
fp=open(reportPath,"wb")
# retry重跑一次
runer=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="测试报告的名称",description="测试报告的描述",retry=1)
runer.run(discover)
# 关闭
fp.close()