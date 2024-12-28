import testlink
import os
import xml.etree.ElementTree as ET
file_for_documnet = 'document_test_link.txt'

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167" ## admin 
client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
#tls = tlh.connect(testlink.TestlinkAPIClient)

for m in testlink.testlinkargs._apiMethodsArgs.keys():
    print(m)
# show total args for each method 


# print(client.whatArgs('createTestCase'))

# tls.getTestSuitesForTestPlan(testplanid = 1 , )
# print(client.whatArgs('createTestProject'))
# tls.getTestProjectByName('' , [ TESTLINK_API_PYTHON_DEVKEY ])
# result = tlh.getProjects(['new_project_1403_10_05' , ])
# tlh.createTestProject()

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



# try : 
#     client.createTestProject( **project_info )
#     print("ok")
# except Exception as e : 
#     print(e)