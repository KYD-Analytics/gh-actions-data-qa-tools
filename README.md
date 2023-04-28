# Data Quality check tools for GitHub Actions

## Using the Python file:
Run the python file using the code below
```
    py csv_qa.py -k <key name> -s <start name> -e <end name> <csv file paths>
    OR
    py csv_qa.py --key <key name> --start <start name> --end <end name> <csv file paths>
```
The above Python file takes 3 optional values for key, start and end column names that will be checked for overlapping versions in .csv files.
Enter the .csv file paths at the end, can accept multiple files.
If version overlaps are found, the corresponding filename of where it was found will be listed along with the number of overlaps found in the file.

## Using workflows in GitHub Actions:
Clone the .github/workflows/data_quality_check.yml to integrate checks into GitHub Actions.
You can run the Python file above as a step in GitHub to stop merging of a PR when test fails by setting branch protection rules in GitHub to 'require status checks to pass before merging'.
It is also worth to protect the branch to be merged into by requiring a PR before merging so that status checks cannot be bypassed.

Note that there is another option of 'requiring status checks to be run' and you generally should not do that in this case because the step only runs when a .csv file is present in the PR. The checks will get stuck in a limbo if you enable this and create a PR that doesn't contain .csv files.
If you have to check that option, you could change the job in the workflow to check all files, not just .csv files. You can then filter the files in the Python program to only run on .csv files, the checks would pass even if no files are passed to the program.
