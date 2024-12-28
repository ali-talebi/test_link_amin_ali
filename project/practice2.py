import testlink
import os
import xml.etree.ElementTree as ET
file_for_documnet = 'document_test_link.txt'

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167" ## admin 
client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)


#getTestPlanByName
#getUserByID
print(client.whatArgs('getExecutionSet'))


# for _ in client.getProjects() : 
#     print(_)
#     break 


# project_info = {
#     'name': 'project_created_from_code',  # Ensure this is not empty
#     'prefix': 'pcfc',                      # Ensure this is not empty
#     'notes': 'Project created via Python API',
#     'active': 1,
#     'public': 1,
#     'options': {
#         'requirementsEnabled': 1,
#         'testPriorityEnabled': 1,
#         'automationEnabled': 1,
#         'inventoryEnabled': 1
#     }
# }


# client.createTestProject(name = 'test_project_created_from_code' , prefix = "from_code_created")
# print(client.getTestCasesForTestSuite(testsuiteid = 73 , deep = None , details = None ))

  
# testcase_info = {
#     'testcaseName': 'from_code_test_Case',
#     'testSuiteId':  73 ,
#     'summary': 'summary from code ',
#     'testProjectId': 43 , 
#     'executionType': 1 ,
#     'status': 1 ,
#     'steps': [
#         {'step_number': 1, 'actions': 'Open the application.', 'expected_results': 'Application opens successfully.'},
#         {'step_number': 2, 'actions': 'Log in with valid credentials.', 'expected_results': 'User is logged in.'}
#     ] # Steps should be a list of dictionaries
# }


# client.createTestCase(**testcase_info)
#print(client.getRequirements(testprojectid = 43 , testplanid = 72 ))
# print(client.getProjectTestPlans(1) )
