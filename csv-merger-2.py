import csv

# Prompt user for file names
dspace_csv = input("Enter the name of the file to be imported to Dspace (including .csv extension): ")
auto_prefix_csv = input("Enter the name of the auto-prefix output file (including .csv extension): ")

# Load Auto-prefix output CSV into a dictionary for easy lookup
auto_prefix_data = {}
with open(auto_prefix_csv, mode="r", encoding="utf-8") as auto_file:
    auto_reader = csv.DictReader(auto_file)
    for row in auto_reader:
        auto_prefix_data[row["source"]] = row["doi"]

# Define all possible `dc.identifier.uri` field names
uri_fields = ["dc.identifier.uri[]", "dc.identifier.uri", "dc.identifier.uri[en]"]

# Initialize counters
dois_added = 0
rows_skipped = 0
total_auto_prefix_dois = len(auto_prefix_data)

# Read the Dspace Import CSV and update the dc.identifier.uri fields
updated_rows = []
with open(dspace_csv, mode="r", encoding="utf-8") as dspace_file:
    dspace_reader = csv.DictReader(dspace_file)
    fieldnames = dspace_reader.fieldnames  # Retain original fieldnames

    for row in dspace_reader:
        matched = False  # Track if any field matches the source
        for uri_field in uri_fields:
            if uri_field in row and row[uri_field].strip():  # Check if the field exists and has data
                existing_uri = row[uri_field].strip()

                # Skip if the URI already contains a DOI
                if any(prefix in existing_uri for prefix in ["10.25316", "https://doi.org"]):
                    print(f"Skipping row with existing DOI in field {uri_field}: {existing_uri}")
                    rows_skipped += 1
                    matched = True  # Mark as handled to avoid "No match" message
                    break

                # Check for a match with the source
                if existing_uri in auto_prefix_data:
                    print(f"Match found for: {existing_uri} in field {uri_field}")
                    row[uri_field] += "||" + auto_prefix_data[existing_uri]
                    dois_added += 1
                    matched = True
                    break  # Stop further processing once a match is found

        if not matched:
            # Log a "No match" message only if no action was taken for any URI field
            print(f"No match for any field in row ID: {row.get('id', 'Unknown')}")

        updated_rows.append(row)

# Write the updated data back to a new CSV file
output_csv = "updated_" + dspace_csv
with open(output_csv, mode="w", encoding="utf-8", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

# Sum it up!
print("\n--- Summary ---")
print(f"Total DOIs in Auto-prefix CSV: {total_auto_prefix_dois}")
print(f"DOIs added: {dois_added}")
print(f"Rows skipped (DOI already present): {rows_skipped}")
print(f"Updated CSV saved as: {output_csv}")