def report_output(validation_type, status, details):
    # Write the output to the report file
    with open("/Users/admin/PycharmProjects/test_automation_framework_nov/report", "a") as report:
        report.write(f"{validation_type}: {status} Details: {details}\n\n")


# 1. html / json
# 2. you can write output to tables ( report_summary/ report_detail)
# 3. custom log file which shows details about failure