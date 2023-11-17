import json

# Load the JSON file
with open('bandit_report.json') as file:
    data = json.load(file)

# Create a dictionary to store unique combinations of filename and issue_text
unique_combinations = {}

# Iterate through the data
for entry in data['results']:
    # Filter entries based on severity (LOW, MEDIUM, HIGH)
    if entry['issue_severity'] in ('MEDIUM', 'HIGH'):
        # Generate a unique key using filename and issue_text
        key = (entry['filename'], entry['issue_text'])

        # Create a dictionary for the combination if it doesn't exist
        if key not in unique_combinations:
            unique_combinations[key] = {
                'severity': entry['issue_severity'],
                'issue_text': entry['issue_text'],
                'line_number': entry['line_number'],
                'filename': entry['filename'],
                'link': entry['more_info']
            }

# Print the results
for key, values in unique_combinations.items():
    print(f"Severity: {values['severity']}")
    print(f"Filename: {values['filename']}")
    print(f"Issue Text: {values['issue_text']}")
    print(f"Line Number: {values['line_number']}")
    print(f"Link: {values['link']}")
    print()
