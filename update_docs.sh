#!/bin/bash
GH_PAGES_SOURCES=docs

# git checkout gh-pages
rm -rf build _sources _static
git checkout master ${GH_PAGES_SOURCES}
git reset HEAD
make -C docs/ html
mv -fv docs/build/html/* ./
rm -rf ${GH_PAGES_SOURCES}
touch .nojekyll
git add -A
git ci -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages
# git checkout master
