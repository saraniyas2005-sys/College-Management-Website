import os
import re

# Set the directory where your HTML files are stored
html_directory = r'C:\Users\hp\Desktop\college website\stannes_college_site\templates'  # Change this to your actual directory path

# This function will replace links and image sources in HTML
def update_html_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace CSS links
    content = re.sub(r'(<link.*?href=")([^"]+)(\.css)("[^>]*>)', r'\1{{ url_for("static", filename="\2.css") }}\4', content)

    # Replace JavaScript links
    content = re.sub(r'(<script.*?src=")([^"]+)(\.js)("[^>]*>)', r'\1{{ url_for("static", filename="\2.js") }}\4', content)

    # Replace image sources
    content = re.sub(r'(<img.*?src=")([^"]+)(\.jpg|\.jpeg|\.png|\.gif|\.svg)("[^>]*>)', r'\1{{ url_for("static", filename="\2\3") }}\4', content)

    # Replace internal links (e.g. href="/page.html")
    content = re.sub(r'(<a.*?href=")(/[^"]+)(["][^>]*>)', r'\1{{ url_for("\2") }}\3', content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Loop through all HTML files in the directory and apply the update
def update_all_html_files():
    for filename in os.listdir(html_directory):
        if filename.endswith('.html'):
            file_path = os.path.join(html_directory, filename)
            update_html_links(file_path)
            print(f"Updated {filename}")

# Run the update process
update_all_html_files()
