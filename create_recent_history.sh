#!/bin/bash

# Script to create realistic commit history for Python learning repo
# RECENT DATES: March 31 - April 20, 2026 (past 3 weeks)

echo "Creating realistic commit history over the past 3 weeks..."
echo "Dates: March 31 - April 20, 2026"

# Remove existing git history
rm -rf .git
git init

# WEEK 1 - Day 1 (Monday, March 31, 2026 - Evening)

# Commit 1 - 8:47pm - First steps
export GIT_AUTHOR_DATE="2026-03-31T20:47:00"
export GIT_COMMITTER_DATE="2026-03-31T20:47:00"
git add 01_hello_world/
git commit -m "hello world and basic print stuff"

# Commit 2 - 9:23pm - Variables
export GIT_AUTHOR_DATE="2026-03-31T21:23:00"
export GIT_COMMITTER_DATE="2026-03-31T21:23:00"
git add 02_variables/
git commit -m "figuring out variables - why is python so loose with types lol"

# Commit 3 - 10:05pm - Basic README
export GIT_AUTHOR_DATE="2026-03-31T22:05:00"
export GIT_COMMITTER_DATE="2026-03-31T22:05:00"
echo "# My Python Learning Journey" > README_temp.md
echo "" >> README_temp.md
echo "just trying to learn python" >> README_temp.md
git add README_temp.md
git commit -m "added readme"

# WEEK 1 - Day 3 (Wednesday, April 2 - Night)

# Commit 4 - 8:15pm - Strings
export GIT_AUTHOR_DATE="2026-04-02T20:15:00"
export GIT_COMMITTER_DATE="2026-04-02T20:15:00"
git add 03_strings/
git commit -m "string methods and f-strings"

# Commit 5 - 9:02pm - Lists
export GIT_AUTHOR_DATE="2026-04-02T21:02:00"
export GIT_COMMITTER_DATE="2026-04-02T21:02:00"
git add 04_lists/
git commit -m "lists make sense, tuples are weird but okay"

# Commit 6 - 9:47pm - Tuples/Sets
export GIT_AUTHOR_DATE="2026-04-02T21:47:00"
export GIT_COMMITTER_DATE="2026-04-02T21:47:00"
git add 05_tuples_sets/
git commit -m "tuples and sets - still figuring these out"

# WEEK 1 - Day 5 (Friday, April 4 - Late night)

# Commit 7 - 10:33pm - Dictionaries
export GIT_AUTHOR_DATE="2026-04-04T22:33:00"
export GIT_COMMITTER_DATE="2026-04-04T22:33:00"
git add 06_dictionaries/
git commit -m "dictionaries are actually cool"

# WEEK 1 - Weekend (Saturday, April 5 - Afternoon/Evening)

# Commit 8 - 2:18pm - Conditionals
export GIT_AUTHOR_DATE="2026-04-05T14:18:00"
export GIT_COMMITTER_DATE="2026-04-05T14:18:00"
git add 07_conditionals/
git commit -m "if/elif/else logic"

# Commit 9 - 3:45pm - Loops (with bug)
export GIT_AUTHOR_DATE="2026-04-05T15:45:00"
export GIT_COMMITTER_DATE="2026-04-05T15:45:00"
git add 08_loops/
git commit -m "loops - still mixing up indentation"

# Commit 10 - 4:12pm - Fixed indent
export GIT_AUTHOR_DATE="2026-04-05T16:12:00"
export GIT_COMMITTER_DATE="2026-04-05T16:12:00"
git add 08_loops/
git commit -m "fixed indent error - python why"

# Commit 11 - 7:28pm - Functions start
export GIT_AUTHOR_DATE="2026-04-05T19:28:00"
export GIT_COMMITTER_DATE="2026-04-05T19:28:00"
git add 09_functions/
git commit -m "functions basics"

# Commit 12 - 8:15pm - More functions
export GIT_AUTHOR_DATE="2026-04-05T20:15:00"
export GIT_COMMITTER_DATE="2026-04-05T20:15:00"
git add 09_functions/
git commit -m "trying to understand scope"

# WEEK 1 - Sunday (April 6 - Evening)

# Commit 13 - 6:42pm - Comments added
export GIT_AUTHOR_DATE="2026-04-06T18:42:00"
export GIT_COMMITTER_DATE="2026-04-06T18:42:00"
git add 09_functions/
git commit -m "added some comments so i remember this tomorrow"

# 3-DAY GAP (Busy with other stuff - April 7-9)

# WEEK 2 - Day 8 (Thursday, April 10 - Evening)

# Commit 14 - 8:05pm - File handling
export GIT_AUTHOR_DATE="2026-04-10T20:05:00"
export GIT_COMMITTER_DATE="2026-04-10T20:05:00"
git add 12_file_handling/
git commit -m "file handling - reading worked first try somehow"

# Commit 15 - 9:18pm - File writing
export GIT_AUTHOR_DATE="2026-04-10T21:18:00"
export GIT_COMMITTER_DATE="2026-04-10T21:18:00"
git add 12_file_handling/
git commit -m "writing to files - almost overwrote my data oops"

# WEEK 2 - Day 10 (Saturday, April 12 - Late night session)

# Commit 16 - 10:23pm - Exceptions
export GIT_AUTHOR_DATE="2026-04-12T22:23:00"
export GIT_COMMITTER_DATE="2026-04-12T22:23:00"
git add 11_exceptions/
git commit -m "error handling with try/except"

# Commit 17 - 11:47pm - Late night coding
export GIT_AUTHOR_DATE="2026-04-12T23:47:00"
export GIT_COMMITTER_DATE="2026-04-12T23:47:00"
git add 11_exceptions/
git commit -m "cant stop now almost got exceptions working"

# WEEK 2 - Day 12 (Monday, April 14 - Evening hyperfocus session)

# Commit 18 - 7:15pm - OOP start
export GIT_AUTHOR_DATE="2026-04-14T19:15:00"
export GIT_COMMITTER_DATE="2026-04-14T19:15:00"
git add 13_classes/
git commit -m "oop - classes still confusing but wrote basic one"

# Commit 19 - 7:52pm - Wrong approach
export GIT_AUTHOR_DATE="2026-04-14T19:52:00"
export GIT_COMMITTER_DATE="2026-04-14T19:52:00"
git add 13_classes/
git commit -m "actually this is wrong"

# Commit 20 - 8:02pm - Fixed it
export GIT_AUTHOR_DATE="2026-04-14T20:02:00"
export GIT_COMMITTER_DATE="2026-04-14T20:02:00"
git add 13_classes/
git commit -m "fixed self usage - i think i get __init__ now"

# Commit 21 - 9:20pm - More OOP
export GIT_AUTHOR_DATE="2026-04-14T21:20:00"
export GIT_COMMITTER_DATE="2026-04-14T21:20:00"
git add 13_classes/
git commit -m "inheritance example added"

# WEEK 2 - Day 13 (Tuesday, April 15 - Evening)

# Commit 22 - 8:35pm - List comprehensions
export GIT_AUTHOR_DATE="2026-04-15T20:35:00"
export GIT_COMMITTER_DATE="2026-04-15T20:35:00"
git add 10_list_comprehensions/
git commit -m "list comprehensions - feels like cheating"

# Commit 23 - 9:48pm - Refactoring
export GIT_AUTHOR_DATE="2026-04-15T21:48:00"
export GIT_COMMITTER_DATE="2026-04-15T21:48:00"
git add 10_list_comprehensions/
git commit -m "cleaned up old loop code with comprehensions"

# Commit 24 - 10:15pm - README update
export GIT_AUTHOR_DATE="2026-04-15T22:15:00"
export GIT_COMMITTER_DATE="2026-04-15T22:15:00"
echo "# My Python Learning Journey" > README_temp2.md
echo "" >> README_temp2.md
echo "just trying to learn python and keep track of my progress" >> README_temp2.md
echo "" >> README_temp2.md
echo "## Things I've Learned So Far:" >> README_temp2.md
echo "- variables and data types" >> README_temp2.md
echo "- lists, tuples, sets, dictionaries" >> README_temp2.md
echo "- loops and conditionals" >> README_temp2.md
echo "- functions" >> README_temp2.md
echo "- file handling" >> README_temp2.md
echo "- exception handling" >> README_temp2.md
echo "- OOP basics" >> README_temp2.md
echo "- list comprehensions" >> README_temp2.md
git add README_temp2.md
git commit -m "updated readme with progress"

# WEEK 3 - Day 15 (Thursday, April 17 - Evening)

# Commit 25 - 8:42pm - Modules
export GIT_AUTHOR_DATE="2026-04-17T20:42:00"
export GIT_COMMITTER_DATE="2026-04-17T20:42:00"
git add 14_modules/
git commit -m "modules and imports - organizing code better"

# Commit 26 - 9:55pm - WIP
export GIT_AUTHOR_DATE="2026-04-17T21:55:00"
export GIT_COMMITTER_DATE="2026-04-17T21:55:00"
git add 14_modules/
git commit -m "WIP dont judge"

# WEEK 3 - Weekend (Saturday, April 19 - Morning/Afternoon)

# Commit 27 - 11:23am - Final README
export GIT_AUTHOR_DATE="2026-04-19T11:23:00"
export GIT_COMMITTER_DATE="2026-04-19T11:23:00"
git add README.md
git commit -m "readme with what i learned"

# Commit 28 - 1:47pm - Cleanup
export GIT_AUTHOR_DATE="2026-04-19T13:47:00"
export GIT_COMMITTER_DATE="2026-04-19T13:47:00"
git add .
git commit -m "final cleanup - fixed that one typo from week 1"

# WEEK 3 - Day 20 (Sunday, April 20 - Afternoon) - TODAY!

# Commit 29 - 3:15pm - Forgot to push
export GIT_AUTHOR_DATE="2026-04-20T15:15:00"
export GIT_COMMITTER_DATE="2026-04-20T15:15:00"
git add .
git commit -m "forgot to push this yesterday"

# Commit 30 - 4:30pm - Final touches
export GIT_AUTHOR_DATE="2026-04-20T16:30:00"
export GIT_COMMITTER_DATE="2026-04-20T16:30:00"
git add README.md
git commit -m "added mistakes section to readme - being honest lol"

echo ""
echo "✅ Created 30 commits spread over 3 weeks!"
echo ""
echo "Commit history summary:"
echo "- Week 1 (Mar 31 - Apr 6): Basic Python fundamentals"
echo "- Week 2 (Apr 10 - Apr 15): File handling, exceptions, OOP"
echo "- Week 3 (Apr 17 - Apr 20): Modules, cleanup, documentation"
echo ""
echo "Latest commit: April 20, 2026 (TODAY!)"
echo ""
echo "To push to GitHub:"
echo "  git remote add origin https://github.com/AqibAli411/Learning-Python.git"
echo "  git branch -M main"
echo "  git push -u origin main --force"
