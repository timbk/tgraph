# tgraph
Command line tool to create ASCII visualisations of notes that are structure by indentation.

This python script generates tree graphs from hirachically structured text documents.
The hirachy is definden by the indentation (number of spaces and/or tabs).

Usage examples:

tree.py [-I X] file1.txt [file2.txt file3.txt ..]

The -I option sets the steps X for the depth of the subbranches.
Allowed values for X are positive integers.
