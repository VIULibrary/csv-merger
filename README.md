
# csv-merger-2

Use in conjunction with the [DataCite Bulk DOI Creator](https://github.com/VIULibrary/datacite-bulk-doi-creator) and the csv-merger-2 to map a dspace export .csv to a datacite import .csv, generate DOIs, and finally merge your DOIs in your dspace export/import .csv for importing into dspace

**csv-merger-1** --> **[DataCite Bulk DOI Creator](https://github.com/VIULibrary/datacite-bulk-doi-creator)** -- > **CSV-MERGER-2**



1. Clone this script
2. Place your auto-prefix.py .csv outfile and your exported dspace metadata file (this will be the file you merge into, and import back into dspace) in the same directory as the csv-merger.py script.
3. Check your dspace file and see that it aligns with import2dspace.csv.sample or if you have messey field names, messy-import2dspace.csv.sample.
4. Run it and you are prompted for the names of yor auto-prefix.csv files and the dspace export/import file.
5. Check the summary!

```
python csv-merger.py
Enter the name of the file to be imported to Dspace (including .csv extension): LimNaturalizationOriginal.csv
Enter the name of the auto-prefix output file (including .csv extension): LimNatProdOut.csv
Match found for: http://hdl.handle.net/10613/1955 in field dc.identifier.uri[]
Match found for: http://hdl.handle.net/10613/1957 in field dc.identifier.uri[]
Match found for: http://hdl.handle.net/10613/1958 in field dc.identifier.uri[]
Match found for: http://hdl.handle.net/10613/1954 in field dc.identifier.uri[]
Match found for: http://hdl.handle.net/10613/1956 in field dc.identifier.uri[]

--- Summary ---
Total DOIs in Auto-prefix CSV: 5
DOIs added: 5
Rows skipped (DOI already present): 0
Updated CSV saved as: updated_LimNatralizationOrignal.csv
```
6. Batch import to Dspace

