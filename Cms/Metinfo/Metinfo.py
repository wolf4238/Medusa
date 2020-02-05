#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Metinfo import MetinfoArbitraryFileReadVulnerability
from Cms.Metinfo import MetinfoInformationDisclosureVulnerability
from Cms.Metinfo import MetinfoSQLInjectionVulnerability
from ClassCongregation import WriteFile,UserAgentS
from tqdm import tqdm
def Main(Url,FileName,Values,ProxyIp):
    WriteFiles = WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [MetinfoArbitraryFileReadVulnerability.medusa(Url,RandomAgent,ProxyIp),
              MetinfoInformationDisclosureVulnerability.medusa(Url,RandomAgent,ProxyIp),
              MetinfoSQLInjectionVulnerability.medusa(Url,RandomAgent,ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="MetinfoCms plugin progress"):
            WriteFiles.Write(str(i))
    except:
        pass
