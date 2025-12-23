from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pptx") as parser:
    # Check if image extraction is supported
    if not parser.features.images:
        print("Document doesn't support image extraction")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    # Check if document has pages
    if info.page_count == 0:
        print("Document has no pages")
        return
    
    # Iterate over pages
    total_images = 0
    for page_index in range(info.page_count):
        print(f"
Page {page_index + 1}/{info.page_count}:")
        
        # Extract images from the current page
        images = parser.get_images(page_index)
        
        if images:
            page_image_count = 0
            for image in images:
                print(f"  Type: {image.file_type}, Position: ({image.rectangle.left}, {image.rectangle.top})")
                page_image_count += 1
            
            print(f"  Total images on this page: {page_image_count}")
            total_images += page_image_count
        else:
            print("  No images on this page")
    
    print(f"
Total images in document: {total_images}")