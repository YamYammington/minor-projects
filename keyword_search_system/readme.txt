A file search system that utilises a keyword command, for logical searches or to exclude certain filenames.

Necessary packages:
- regex

Usage: 
import keyword_search_system

keyword_search_system.parse(<your keyword string>, <path to the folder to be searched>)


String syntax: @kw <logical keywords> n(<exluded keywords (start keywords with !)>)
Example for clarity: @kw untitled|happy&blush n(!yes)