# visPyGraph
A simple UI creation tool to speed up drawing graphical interfaces.

# To use
1. Ensure python 3.8+ is installed
2. Ensure graphics.py from John Zelle is installed
3. Navigate to either your console or IDE of choice and run the visPyGraph.py file
    * From console, navigate to the directory it is installed in and run "python visPyGraph" (may be python3 on some MacOS devices)
4. Draw desired shapes and labels inside of the designated area, and press the Save button before exiting
    * Make sure the graphicCode.py file is closed when you press Save otherwise there may be unpredictable behaviour
5. To exit the program press the Exit button


# Known Bugs
- Sometimes shapes will unexpectedly draw when switching colors or shapes while still having another shape selected
  * Suggestion to address: always switch back to regular cursor when changing color, changing shape, or saving
- Error messages will pile up in output window/console for a list access
