import re
import unicodedata

def slugify(value):
    value = str(value)  # Ensure the input is a string
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value

# Define the title
title = 'Health Facility Gaps Map'

# Create a slugified version of the title
imgfile = 'img1/{}.png'.format(slugify(title))

print(imgfile)  # Output: img1/health-facility-gaps-map.png
