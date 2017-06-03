set -o errexit

# Generate reference information
echo "Retrieving and processing reference metadata"
(cd build && python references.py)

# pandoc settings
CSL_PATH=citations.csl
CSS_PATH=github-pandoc.css
BIBLIOGRAPHY_PATH=literature-build/generated/bibliography.json
INPUT_PATH=literature-build/generated/all-sections.md

# Create HTML outpout
# http://pandoc.org/MANUAL.html
echo "Exporting HTML manuscript"
pandoc --verbose \
  --from=markdown --to=html5 \
  --filter pandoc-fignos \
  --bibliography=$BIBLIOGRAPHY_PATH \
  --metadata link-citations=true \
  --css=$CSS_PATH \
  --csl=$CSL_PATH \
  --katex \
  --output=output/index.html \
  $INPUT_PATH