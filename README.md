# tgraph
Command line tool to create ASCII visualisations of notes that are structure by indentation.

This python script generates tree graphs from hirachically structured text documents.
The hirachy is definden by the indentation (number of spaces and/or tabs).


Usage example:

tree.py [-I X] file1.txt [file2.txt file3.txt ..]

The -I option sets the steps X for the depth of the subbranches.
Allowed values for X are positive integers.

Example:
=== INPUT:
```
TODO.txt
.git
    COMMIT_EDITMSG
    objects
    HEAD
    branches
    packed-refs
    logs
        HEAD
        refs
    description
    info
        exclude
    config
    FETCH_HEAD
    hooks
    refs
        heads
            master
        tags
        remotes
    index
    ORIG_HEAD
README.md
ttree.py
.gitignore
tgraph.py
examples
    list_graph.txt
    list.txt
    files.txt
    files_graph.txt
```

=== OUTPUT:
```
          /TODO.txt
          |          /COMMIT_EDITMSG
          |          |objects
          |          |HEAD
          |          |branches
          |          |packed-refs
          |          |logs______/HEAD
          |          |          \refs
          |          |description
          |.git------|info-------exclude
          |          |config
          |          |FETCH_HEAD
files-----|          |hooks
          |          |          /heads------master
          |          |refs------|tags
          |          |          \remotes
          |          |index
          |          \ORIG_HEAD
          |README.md
          |ttree.py
          |.gitignore
          |tgraph.py
          |          /list_graph.txt
          |examples--|list.txt
          |          |files.txt
          \          \files_graph.txt
```

