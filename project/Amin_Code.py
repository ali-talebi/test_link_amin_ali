import testlink
import os
import xml.etree.ElementTree as ET

TESTLINK_API_PYTHON_SERVER_URL="http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php"
TESTLINK_API_PYTHON_DEVKEY="2a40335f269615f7ebcef5af20141167"
client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
# client.countProjects()

TEST_PLAN_ID = 1
BUILD_NAME = 'second release'
PROJECT_ID = 1

def create_test_report(test_case_external_id, status):
    """
    Create a simple XML report for Jenkins.
    """
    report_file = 'test_results.xml'

    # Create XML structure
    if not os.path.exists(report_file):
        root = ET.Element("testsuites")
        tree = ET.ElementTree(root)
    else:
        tree = ET.parse(report_file)
        root = tree.getroot()

    suite = ET.SubElement(root, "testsuite", name="Automated Tests")
    case = ET.SubElement(suite, "testcase", name=test_case_external_id)

    if status == 'p':
        ET.SubElement(case, "result").text = "passed"
    elif status == 'f':
        ET.SubElement(case, "result").text = "failed"
    else:
        ET.SubElement(case, "result").text = "blocked"

    tree.write(report_file)

def report_test_case_result(test_case_external_id, status):
    """
    This function will report the result of a test case to TestLink.
    """
    try:
        # expected args: testcaseid, testplanid, buildname, status, notes
        # The status should be 'p' for passed, 'f' for failed, or 'b' for blocked
        result = client.reportTCResult(
            testcaseid=40,
            testplanid=39,
            buildname='second release',
            status="p",
            notes='some notes',
            #user='admin'
            platformname=''
        )
        print(f"Test case {test_case_external_id} result reported as {status}")
    except Exception as e:
        print(f"Error reporting result for {test_case_external_id}: {e}")

def run_automated_tests():
    """
    This function simulates running automated tests.
    Here, we are just using random logic to simulate pass/fail results.
    You would replace this with your actual test logic.
    """
    test_cases = ["olt-20"]  # Example Test Case External IDs

    for test_case in test_cases:
        # Simulate running the test (random pass/fail)
        result = 'p'
        report_test_case_result(test_case, result)
        create_test_report(test_case, result)

if __name__ == '__main__':
    run_automated_tests()
    
    