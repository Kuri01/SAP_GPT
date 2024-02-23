# SAP_GPT Application

The SAP_GPT application is a tool designed to streamline the process of creating test cases for SAP forms by utilizing the capabilities of OpenAI's GPT models. It reads screenshots of SAP forms, extracts functional specifications, and generates test cases based on the analysis. This application leverages OpenAI's GPT-4 Vision and GPT-4 Turbo models to understand and describe images and generate relevant textual content.

## Prerequisites

- Python 3

- An active OpenAI API key

- Required Python packages: `openai`, `requests`

## Installation

### Clone the Repository

Clone the SAP_GPT application repository to your local machine using Git or download the ZIP file.

```bash
git clone https://github.com/Kuri01/SAP_GPT.git
cd SAP_GPT
```

### Set Up a Python Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for your project. Use the following commands to set it up:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install openai requests
```

### Configure Environment Variables

For security reasons, it's advisable to keep your OpenAI API key in an environment variable. You can set this variable in your shell or use a `.env` file with a library like `python-dotenv` to load the variables.

```bash
export OPEN AI_API_KEY='your_api_key_here'
```

Replace `'your_api_key_here'` with your actual OpenAI API key.

for more information how to configure environment for openAI please visit [OpenAI](https://platform.openai.com/docs/quickstart?context=python)

## Usage

### Prepare Your Screenshot

Take a screenshot of the SAP form you want to analyze and save it as `screenshot.png` in the SAP_GPT application directory.

### Run the Script

Execute the main script to start the process:

```bash
python3 index.py
```

The script performs the following steps:

- Encodes the screenshot to a base64 format and sends it to the OpenAI API, requesting a description of the SAP form elements.

- Generates functional specifications based on the image description.

- Creates detailed test cases based on the functional specifications.

### Review Generated Files

After the script completes its execution, you will find three text files in your directory:

- `vision_description.txt`: Contains the description of the SAP form elements as interpreted from the screenshot.

- `functional_specs_description.txt`: Holds the functional specifications document for the SAP form.

- `testcases_description.txt`: Contains the generated test cases for the SAP form.

## Troubleshooting

- **API Key Issues**: Ensure that your OpenAI API key is correctly set in your environment variables. If you encounter authentication errors, verify that the key is valid and has the necessary permissions.

- **Dependency Errors**: If you run into issues with missing packages or version conflicts, make sure all dependencies are correctly installed in your environment. You may need to update your pip installer or re-install the dependencies.

## Contributing

Contributions to the SAP_GPT application are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

# Sample Output

The SAP_GPT application generates three text files as output, each containing specific information about the SAP form analyzed. Below are sample responses for each of the generated files.

## GPT Vision sample response:

```
The image displays a user interface for entering "G/L Account Posting: Header Data", likely a form within an SAP software system. The screen is divided into several sections with various input fields and options:

1. Title Bar: The top of the interface contains the title "Enter G/L Account Posting: Header Data".

2. Checkbox Options: There are checkboxes for "Held Document", "Account Assignment Model", "Fast Entry", "Post with Reference", and "Editing Options". These checkboxes are likely used to apply specific configurations or modes when entering data.

3. Main Data Input Section: This area includes input fields for:
   - "Document Date": A date input field which expects the user to input a date, represented in the format of day, month, and year. One date is partially visible as "16.02.2024", treated as confidential.
   - "Posting Date": Similarly, a date input field for the posting date. It's filled with the same date as above, which is also confidential.
   - "Document Number": An empty text field which would expect an alphanumeric identifier for the document being posted.
   - "Reference": An empty text field potentially for a reference number or code.
   - "Doc.Header Text": An empty text field likely for descriptive information about the document.
   - "Trading Part.BA": An empty text field for entering trading partner or business area information.

4. Additional Data Input Section: This area has fields for:
   - "Type": Filled with "SA", which is possibly a document type or transaction code.
   - "Company Code": Prefilled with "1010", indicating the code of the company or business entity. This is considered a placeholder or example, not confidential.
   - "Period": Filled with "2", which might represent a fiscal period or month.
   - "Currency/Rate": Prefilled with "EUR", indicating the Euro currency is being used.
   - "Transltn Date": An empty date field for a translation date, if applicable.
   - "Cross-CC Number": An empty text field perhaps intended for a cross-company code number or similar identifier.

5. First Line Item Section: There is a table-like section with the heading "First Line Item" which includes columns labeled "PstKy", "40 Account", "SGL Ind", and "TType". Inputs under these columns are likely to be:
   - "PstKy": A field likely to be an alphanumeric key or code for posting.
   - "40 Account": This cell contains a prefilled value "40", which may represent a specific account type or posting key.
   - "SGL Ind": An empty field expected to be a single ledger indicator or similar code.
   - "TType": An empty field where a transaction type or code is anticipated.

This interface represents a form-heavy ERP-style screen where accounting and financial transactions are recorded. The expected data would usually include
```

## GPT Functional specs response:

```
# Functional Specification Document for SAP Form: Enter G/L Account Posting: Header Data

## 1. Introduction
This document outlines the functional requirements and specifications for the development of a new SAP form titled "Enter G/L Account Posting: Header Data". This form is designed to facilitate the entry and processing of general ledger account postings within an SAP software system, focusing on the header data required for such postings.

## 2. Form Overview
The form serves as a user interface within the SAP system, allowing users to input and configure data related to G/L account postings. It is divided into several sections, each catering to different aspects of the posting process, including the input of main data, additional data, and line item information.

### 2.1 Title Bar
- **Title**: Enter G/L Account Posting: Header Data

### 2.2 Checkbox Options
- **Available Checkboxes**:
  - Held Document
  - Account Assignment Model
  - Fast Entry
  - Post with Reference
  - Editing Options

### 2.3 Main Data Input Section
- **Fields**:
  - Document Date (DD.MM.YYYY)
  - Posting Date (DD.MM.YYYY)
  - Document Number (Alphanumeric)
  - Reference (Alphanumeric)
  - Doc.Header Text (Text)
  - Trading Part.BA (Text)

### 2.4 Additional Data Input Section
- **Fields**:
  - Type (Pre-filled: "SA")
  - Company Code (Pre-filled: "1010")
  - Period (Numeric, Pre-filled: "2")
  - Currency/Rate (Pre-filled: "EUR")
  - Transltn Date (DD.MM.YYYY)
  - Cross-CC Number (Alphanumeric)

### 2.5 First Line Item Section
- **Columns**:
  - PstKy (Alphanumeric)
  - 40 Account (Numeric, Pre-filled: "40")
  - SGL Ind (Alphanumeric)
  - TType (Alphanumeric)

## 3. Technical Specifications
### 3.1 Development Environment
- SAP ERP system

### 3.2 Data Handling
- All inputs must allow for alphanumeric entries where specified.
- Date fields must incorporate a date picker for ease of use and to ensure proper formatting.
- Relevant fields (e.g., "Company Code") should be auto-populated based on the user profile or last entries where applicable.
- Checkbox options need to enable or disable specific features or fields in the form dynamically according to the selection.

### 3.3 Validation Rules
- Mandatory fields (e.g., Document Date, Posting Date) should be clearly marked and validated upon form submission.
- The "Document Number" field should validate against existing entries to avoid duplicates.
- Currency fields should only accept valid currency codes.
- Cross-field validation is required for date fields to ensure that the "Posting Date" cannot precede the "Document Date".

## 4. User Interface and Experience
- The form should utilize a responsive design to ensure usability across devices.
- Input fields, checkboxes, and other elements should be clearly labeled and logically arranged for intuitive navigation.
- A clear visual indication of mandatory versus optional fields will enhance user experience.
- Tooltips or help text should be available for complex fields like "PstKy" or "SGL Ind" to guide users during data entry.

## 5. Security and Compliance
- User access to the form should be controlled through SAP's standard authorization and role-based access mechanisms.
- All data handling and processing should comply with relevant data protection standards, including GDPR where applicable.

## 6. Testing Parameters
- Comprehensive testing must include scenarios covering all input combinations in the main and additional data sections.
- Testing should also cover all checkbox functionalities to ensure they correctly enable or disable form features.
- Error handling tests to verify that appropriate messages are displayed for invalid inputs or field validation failures.

## 7. Approval and Changes
- This document requires approval from the project stakeholders before development begins.
- Any significant changes proposed after approval must be documented and communicated to all stakeholders. 

## Author
Business Analyst, [Your Name]
[Date]
```

## GPT Test cases response:

```
### Test Case 1

- **Test Case ID**: TC001
- **Test Case Description**: Verify that mandatory fields are clearly indicated and validated upon form submission.
- **Steps**:
  1. Navigate to the "Enter G/L Account Posting: Header Data" form.
  2. Leave all fields, including the mandatory fields like "Document Date" and "Posting Date", empty.
  3. Attempt to submit the form.
- **Expected Result**: The form should not submit. There should be a clear visual indication (e.g., field borders turn red, an exclamation mark appears) next to the mandatory fields that were left blank, accompanied by a message indicating that these fields must be filled.

### Test Case 2

- **Test Case ID**: TC002
- **Test Case Description**: Validate the functionality of the date picker for the "Document Date" and "Posting Date".
- **Steps**:
  1. Navigate to the "Enter G/L Account Posting: Header Data" form.
  2. Click on the "Document Date" field.
  3. Select a date using the date picker.
  4. Repeat steps 2 and 3 for the "Posting Date" field.
- **Expected Result**: The date picker should be displayed upon clicking the date fields. The selected dates should correctly populate the "Document Date" and "Posting Date" fields in DD.MM.YYYY format.

### Test Case 3

- **Test Case ID**: TC003
- **Test Case Description**: Test the checkbox functionality to enable/disable specific features in the form.
- **Steps**:
  1. Navigate to the form.
  2. Observe the default state of form fields and options.
  3. Check the "Fast Entry" checkbox.
  4. Observe changes in the availability of form fields and options.
- **Expected Result**: Checking the "Fast Entry" checkbox should dynamically enable/disable certain fields or features of the form. These changes should be in accordance with the defined behaviors for this checkbox option in the specifications.

### Test Case 4

- **Test Case ID**: TC004
- **Test Case Description**: Ensure cross-field validation for "Posting Date" and "Document Date".
- **Steps**:
  1. Enter a "Document Date" that is chronologically after the "Posting Date".
  2. Attempt to submit the form.
- **Expected Result**: The form submission should be blocked. An error message should be displayed indicating that the "Posting Date" cannot be before the "Document Date".

### Test Case 5

- **Test Case ID**: TC005
- **Test Case Description**: Validate the auto-population of the "Company Code" based on user profiles or last entries.
- **Steps**:
  1. Log in with a user profile that has previously used a specific "Company Code".
  2. Navigate to the form.
  3. Observe the "Company Code" field.
- **Expected Result**: The "Company Code" field should be automatically populated with the last used code or a specific code based on the user profile, as per the specifications.

### Test Case 6

- **Test Case ID**: TC006
- **Test Case Description**: Verify the error handling for invalid input in the "Currency/Rate" field.
- **Steps**:
  1. Enter an invalid currency code in the "Currency/Rate" field (e.g., "XYZ").
  2. Attempt to submit the form.
- **Expected Result**: The form submission should be blocked. An error message should be displayed indicating that the entered value in the "Currency/Rate" field is not a valid currency code.

### Test Case 7

- **Test Case ID**: TC007
- **Test Case Description**: Check the response and visual feedback when a user attempts to enter a duplicate "Document Number".
- **Steps**:
  1. Enter a "Document Number" that already exists in the system.
  2. Attempt to submit the form.
- **Expected Result**: The form submission should be blocked. An appropriate error message should be displayed indicating that the entered "Document Number" is a duplicate and another value should be used. 

### Test Case 8

- **Test Case ID**: TC008
- **Test Case Description**: Verify the functionality and responsive design of the form across different devices.
- **Steps**:
  1. Open the form on a desktop browser.
  2. Observe and document the layout and usability.
  3. Open the form on a tablet and a smartphone.
  4. Compare the layout, usability, and any adjustments made for smaller screens.
- **Expected Result**: The form should display a responsive design that adjusts the layout and elements appropriately to provide usability across desktop, tablet, and smartphone screens, without compromising functionality or user experience.
```
