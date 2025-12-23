from groupdocs.parser import Parser

def analyze_image_distribution(file_path):
    """
    Analyze how images are distributed across document pages.
    """
    with Parser(file_path) as parser:
        if not parser.features.images:
            print("Image extraction not supported")
            return
        
        info = parser.get_document_info()
        
        image_stats = []
        total_images = 0
        
        for page_index in range(info.page_count):
            images = parser.get_images(page_index)
            
            if images:
                # Count images on this page
                image_list = list(images)
                page_image_count = len(image_list)
                
                # Collect image types
                image_types = [img.file_type.extension for img in image_list]
                
                image_stats.append({
                    'page': page_index + 1,
                    'count': page_image_count,
                    'types': image_types
                })
                
                total_images += page_image_count
        
        # Print summary
        print(f"Document: {file_path}")
        print(f"Total pages: {info.page_count}")
        print(f"Total images: {total_images}")
        print(f"Average images per page: {total_images / info.page_count:.2f}
")
        
        # Print per-page details
        for stat in image_stats:
            types_str = ", ".join(set(stat['types']))
            print(f"Page {stat['page']}: {stat['count']} images ({types_str})")

# Usage
analyze_image_distribution("sample.pdf")