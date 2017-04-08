#!/bin/bash

# Folders and files needed to generate Sphinx docs. These files will
# be copied from the master branch.
GH_PAGES_SOURCES='docs pylade'

# Copy docs source files from the master branch
git checkout master ${GH_PAGES_SOURCES}

# Generate new HTML docs using Sphinx Makefile
make -C docs/ html

# Move generated HTML files to the main folder and remove useless folders
mv -fv docs/build/html/* ./
rm -rf ${GH_PAGES_SOURCES}

# Create a .nojekyll file if not present
touch .nojekyll

# Ask for confirmation before pushing
printf "\nCommit name: '`git log master -1 --format=%B`'\n"
read -n 1 -p "Do you want to commit and push on gh-pages? [Y/n] " answer

if [[ $answer == "Y" || $answer == "y" || $answer = "" ]]; then
  printf "\n"
  # Stage changes, create commit and push
  git add -A
  git ci -m "Generated gh-pages for `git log master -1 --format='%B (%H)'`"
  git push origin gh-pages
else
  printf "\nNot pushing.\n"
fi

# Go back to master branch
# git checkout master
