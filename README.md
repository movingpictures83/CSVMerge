# CSVMerge
# Language: Python
# Input: TXT (contains a list of CSV files)
# Output: CSV (merged CSV files)
# Tested with: PluMA 1.0, Python 2.7

CSVMerge is a PluMA plugin that expects as input a .txt file containing
a list of CSV files to merge, one per line.  It will then merge those files
into a single CSV file.

The merged CSV file will contain the union of all rows and columns, with
zeroes assumed for any (i, j) that does not have a value in any of the
merged CSV files.  If the same (i, j) has a value in more than one of the CSV
files for merging, the last one will be assumed.
