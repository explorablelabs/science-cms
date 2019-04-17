# Takes in a file CSV file and outputs each row as a Markdown file with YAML front matter named after first column.
# Data in the first row of the CSV is assumed to be the column heading.
# Original work borrowed from: https://www.bryanklein.com/blog/hugo-python-gsheets-oh-my/

# Import the python libraries.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path
import os
import json

# Delete old page files. Leave the _index.md file there.
if os.path.exists("./site/content/post/fake_ic50_data.md"):
    os.remove("./site/content/post/fake_ic50_data.md")

# Get JSON_DATA from the build environment.
jsondict = json.loads(os.environ['JSON_DATA'])

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(jsondict, scope)
client = gspread.authorize(creds)

# Open the Google Sheet by ID.
sheet1 = client.open_by_key(os.environ['GSHEET_KEY']).sheet1

# Extract all of the records for each row.
sheetdata1 = sheet1.get_all_records()

# Loop through each row once to get molecule list
molecule_list = []
for row_index, row in enumerate(sheetdata1):
  if row.get("approved") == "x":
    molecule = row.get("smiles")
    molecule_list.append(molecule)
list_of_molecules = ".".join(molecule_list)
print list_of_molecules

# Set location to write new files to.
filename = "./site/content/post/fake_ic50_data.md"
new_yaml = open(filename, 'w')
# Empty string that we will fill with YAML formatted text based on data extracted from our CSV.
yaml_text = ""
yaml_text += "---\n"
yaml_text += "title: Pulling data from Google Sheets\n"
yaml_text += "description: 'The data below is pulled from this private Google Sheet. The build script has read-only access via Google Sheets OAuth 2.0 API. Molecules are rendered from SMILES in the Google Sheet.'\n"
yaml_text += "image: '/img/gsheet_screenshot.png'\n"
yaml_text += "molecule_list: '%s'\n" % list_of_molecules
yaml_text += "---\n"

# Loop through each row to get IC50 data if you want to display this as well
# TODO: make a nice table to display this. It doesn't look great just as text.
for row_index, row in enumerate(sheetdata1):
  if row.get("approved") == "x":
    fake_ic50 = row.get("fake_ic50")
    molecule_id = row.get("molecule_id")
    #cell_text = str(molecule_id) + ": " + str(fake_ic50) + "\n "
    #yaml_text += cell_text
        
# Write our YAML string to the new text file and close it.
new_yaml.write(yaml_text + "---\n")
new_yaml.close()
