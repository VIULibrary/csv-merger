# csv-merger 
Use in conjunction with the [##DataCite Bulk DOI Creator](https://github.com/VIULibrary/datacite-bulk-doi-creator), to merge the DOIs from the CSV output, with your dspace import file

1: Clone this script
2: Place your auto-prefix.py .csv outfile and your exported dspace metadata file (this will be the file you merge into, and import back into dspace) in the same directory as the csv-merger.py script.
4: Check your dspace file and see that it aligns with import2dspace.csv.sample or if you have messey field names, messy-import2dspace.csv.sample. 
3: Run it and you are prompted for the names of yor auto-prefix.csv files and the dspace export/import file.
4: Check the summary!

```
(3.11.0) Daniel@eSabretache3 csv-merger  % python csv-merger.py
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
5: Batch import to Dspace