# SQLiSearch
Tool for searching SQLi on google

This tool search with the google dorks that you provide on google, and then check for a possible sqli on those sites, it requires python3 in order to work

To install the requirements:
  pip3 -r install requirements.txt

To start playing around:

python3 SQLiSearch.py -q "php?id=" : Basic query for search for an injection on php pages

Another options:

  -n: number of searchs done by google
  
  -p: pause between searches, if it's too low google probably blocks you(dam u google!!)
