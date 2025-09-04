import os
import re
import shutil

# Paths (using raw string to handle Windows backslashes correctly)
posts_dir = r"C:\Users\seanh\Documents\angelmarielblog\content\posts"
attachments_dir = r"C:\Users\seanh\Documents\angelmarielblog\content\attachments"
static_images_dir = r"C:\Users\seanh\Documents\angelmarielblog\static\images"

# Step 1: Process each md file in the posts directory
for file in os.listdir(posts_dir):
    if file.endswith('.md'):
        file_path = os.path.join(posts_dir, file)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 2: Find all image URLs in the format [[image.png]]
        image_urls = re.findall(r'\[\[([^\]]+)\]\]', content)

        # Step 3: Replace the image URLs and ensure URLs are correctly formatted
        for image_url in image_urls:
            # Prepare the md-compatible URL with %20 replacing spaces
            md_url = f"![Image Description](/images/{image_url.replace(' ', '%20')})"
            content = content.replace(f"[[{image_url}]]", md_url)

            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image_url)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the md file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"Markdown files processed and images copied to static/images: {file}")