import testlink
import os
import xml.etree.ElementTree as ET
file_for_documnet = 'document_test_link.txt'

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167" ## admin 
client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)



for project in client.getProjects() : 
    # print(project)
    # for key , value in project.items() : 
    #     print(key , '-->--' , value )
    print("Name of Project " , project['name'] , "Id of Project : " , project['id'] )
    
    
    for element in client.getProjectTestPlans(project['id']) : 
        print("         /////////////////////////// Test Plans ///////////////////////////  ")
        print(element)
        result = client.getTestSuitesForTestPlan(element['id'])
        for e in result : 
            print(f"Test Suite /n {e}")
            test_case = client.getTestCasesForTestSuite(testsuiteid = e['id'])
            print(f"test case ---> {test_case}")
    
        print("     ******************** /Test Plans ********************  ") 
            
    else : 
        print(" End OF Test Plan ")
    print("############################# *********** #############################")
    
    
