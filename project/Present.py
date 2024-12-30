import testlink
import pytest 
import os
import xml.etree.ElementTree as ET
from TEST_FILE_TOTAL_TEST_CASE import * 
file_for_documnet = 'document_test_link.txt'

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167" ## admin 
client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
pytestmark = [pytest.mark.env_name("SNMP_CLI_env"), pytest.mark.cli_dev("shelf_olt")]

def Total_Test_Case(project_name , test_plan_name , test_suite_name ) : 
    total_project = client.getProjects()
    for iter_project in total_project : 
        if iter_project['name'] == project_name : 
            print("Project : " , iter_project )
            total_test_plan = client.getProjectTestPlans(iter_project['id'])
            for iter_plan in total_test_plan : 
                if iter_plan['name'] == test_plan_name :
                    print("Test Plan : " ,  iter_plan )
                    total_test_suite = client.getTestSuitesForTestPlan(iter_plan['id'])
                    print("Total_Test Suite : " ,total_test_suite  )
                    for iter_test_suite in total_test_suite : 
                        print("iter Test Suite ")
                        print(iter_test_suite)
                        print("iter_test_suite name " , iter_test_suite['name'])
                        total_test_cases = client.getTestCasesForTestSuite(testsuiteid = iter_test_suite['id'])
                        print("Total Test Case " , total_test_cases )

                            
                            
try :                     
    Total_Test_Case( 'OLT_SINA_Comp' , 'Sina_COM_TESTPLAN' , ' test_suite_1_olt_sin_com')

except Exception as e : 
    print(e)
