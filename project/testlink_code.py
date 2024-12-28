import testlink
import os
import xml.etree.ElementTree as ET

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167" ## admin 
#TESTLINK_API_PYTHON_DEVKEY="f1a81b56c3bba6825ecd6677c3ca0388" ## ali_talebi   


try :
    client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
    client.countProjects() ## When Running Error Connection Refued ! 
    result = client.getTestCase(None, testcaseexternalid='AT_test-4') ### prefix for each test case in testl suite , .... 
    
    
    ### status in e.x ) result = {'id':'92' , 'version':'' , 'status':'' , 'summary':'' , 'precondition':'' , 
    # 'execute_type':'1:manual or 2:Automated' 
    # }
    for key , value in result[0].items() : 
        print(key , '---->>>' , value ) 
        
    
    
except Exception as e : 
    print("Exceptaion Raised ! ")
    print(e)
    
