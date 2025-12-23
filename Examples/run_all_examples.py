import os
import subprocess
import sys

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "C://Licenses//GroupDocs.Total.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs Product for Python via .NET Examples!
=================================================================

This script will run a series of examples showcasing the features.
Each example demonstrates different use cases and functionalities such as:

- Working with documents.
- Processing files.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API! 

=======================================================
"""
    print(intro_text)

examples = [
    "getting-started/quick-start/extract_text_from_document.py",
    "getting-started/quick-start/get_document_information.py",
    "getting-started/quick-start/extract_metadata.py",
    "getting-started/quick-start/extract_images.py",
    "getting-started/quick-start/extract_text_from_specific_page.py",
    "getting-started/quick-start/check_format_support.py",
    "getting-started/installation/verify_installation.py",
    "getting-started/installation/extract_text_quick_start.py",
    "getting-started/how-to-run-examples/extract_text_from_document.py",
    "getting-started/how-to-run-examples/extract_text_from_pdf.py",
    "getting-started/how-to-run-examples/extract_metadata_example.py",
    "getting-started/how-to-run-examples/extract_images_example.py",
    "developer-guide/basic-usage/get-supported-file-formats/example-1.py",
    "developer-guide/basic-usage/get-supported-file-formats/example-2.py",
    "developer-guide/basic-usage/get-supported-file-formats/is_format_supported.py",
    "developer-guide/basic-usage/get-supported-file-formats/example-4.py",
    "developer-guide/basic-usage/get-supported-file-formats/process_file.py",
    "developer-guide/basic-usage/get-document-info/example-1.py",
    "developer-guide/basic-usage/get-document-info/example-2.py",
    "developer-guide/basic-usage/get-document-info/process_document.py",
    "developer-guide/basic-usage/get-document-info/example-4.py",
    "developer-guide/basic-usage/get-document-info/example-5.py",
    "developer-guide/basic-usage/extract-text-from-documents/example-1.py",
    "developer-guide/basic-usage/extract-text-from-documents/example-2.py",
    "developer-guide/basic-usage/extract-text-from-documents/example-3.py",
    "developer-guide/basic-usage/extract-text-from-documents/example-5.py",
    "developer-guide/basic-usage/parse-data-from-documents/example-1.py",
    "developer-guide/basic-usage/extract-metadata-from-documents/example-1.py",
    "developer-guide/basic-usage/extract-metadata-from-documents/example-2.py",
    "developer-guide/basic-usage/extract-images-from-documents/example-1.py",
    "developer-guide/basic-usage/extract-images-from-documents/example-2.py",
    "developer-guide/basic-usage/extract-data-from-attachments-and-zip-archives/example-1.py",
    "developer-guide/basic-usage/extract-data-from-attachments-and-zip-archives/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-accurate-mode/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-accurate-mode/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-accurate-mode/extract_text_safely.py",
    "developer-guide/advanced-usage/loading/load-file-from-local-disk/example-1.py",
    "developer-guide/advanced-usage/loading/load-file-from-local-disk/example-2.py",
    "developer-guide/advanced-usage/loading/load-file-from-local-disk/process_files_from_directory.py",
    "developer-guide/advanced-usage/loading/load-file-from-local-disk/safe_load_document.py",
    "developer-guide/advanced-usage/loading/load-options/example-1.py",
    "developer-guide/advanced-usage/loading/load-options/example-2.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/example-1.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/example-2.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/example-3.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/extract_specific_files.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/process_archive_recursively.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/extract_archive_metadata.py",
    "developer-guide/advanced-usage/working-with-archives/extract-data-from-zip-archives/create_archive_inventory.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/example-1.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/example-2.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/is_valid_url.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/export_hyperlinks_to_csv.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/analyze_hyperlinks_by_domain.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/extract_filtered_hyperlinks.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document/batch_extract_hyperlinks.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/example-1.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/example-2.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/example-3.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/example-4.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/example-5.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document/extract_images_from_directory.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/example-1.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/get_metadata_value.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/extract_metadata_as_dict.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/export_metadata_to_json.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/batch_extract_metadata.py",
    "developer-guide/advanced-usage/working-with-metadata/extract-metadata-from-documents/compare_metadata.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/example-1.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/example-2.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/example-3.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/export_tables_to_csv.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/example-5.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/example-6.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document/process_large_table.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/example-3.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/compare_extraction_modes.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/batch_extract_raw.py",
    "developer-guide/advanced-usage/extraction/extract-text-in-raw-mode/create_search_index.py",
    "developer-guide/advanced-usage/extraction/working-with-text/example-1.py",
    "developer-guide/advanced-usage/extraction/working-with-text/example-2.py",
    "developer-guide/advanced-usage/loading/load-file-from-stream/example-1.py",
    "developer-guide/advanced-usage/loading/load-file-from-stream/example-2.py",
    "developer-guide/advanced-usage/loading/load-file-from-stream/process_uploaded_file.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/example-1.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/count_container_items.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/list_container_contents.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/filter_by_extension.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/calculate_container_size.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/group_by_file_type.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/search_container_items.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/process_with_progress.py",
    "developer-guide/advanced-usage/working-with-archives/iterate-through-container-items/export_inventory_to_csv.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/example-1.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/example-2.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/export_page_hyperlinks.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/find_pages_with_external_links.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/analyze_hyperlink_distribution.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page/extract_hyperlinks_from_range.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/example-1.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/example-2.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/example-3.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/example-4.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/analyze_image_distribution.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page/example-6.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/example-1.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/example-2.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/example-3.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/compare_tables_across_pages.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/export_page_tables_to_json.py",
    "developer-guide/advanced-usage/working-with-tables/extract-tables-from-document-page/example-6.py",
    "developer-guide/advanced-usage/loading/load-password-protected-documents/example-1.py",
    "developer-guide/advanced-usage/loading/load-password-protected-documents/load_protected_document.py",
    "developer-guide/advanced-usage/loading/load-password-protected-documents/check_if_protected.py",
    "developer-guide/advanced-usage/loading/load-password-protected-documents/extract_from_protected.py",
    "developer-guide/advanced-usage/loading/load-password-protected-documents/process_protected_documents.py",
    "developer-guide/advanced-usage/template-based-parsing/working-with-templates/example-1.py",
    "developer-guide/advanced-usage/template-based-parsing/working-with-templates/example-2.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/example-1.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/categorize_by_file_type.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/get_supported_items.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/create_file_type_report.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/validate_container_contents.py",
    "developer-guide/advanced-usage/working-with-archives/detect-file-type-of-container-item/extract_type_specific_metadata.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/example-1.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/example-2.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/extract_header_links.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/extract_links_from_regions.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/extract_footer_links.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/extract_links_by_area_and_pattern.py",
    "developer-guide/advanced-usage/working-with-hyperlinks/extract-hyperlinks-from-document-page-area/extract_social_media_links.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/example-1.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/extract_images_from_regions.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/example-3.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/extract_header_logos.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/extract_by_quadrant.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-from-document-page-area/extract_large_images_from_area.py",
    "developer-guide/advanced-usage/extraction/search-text/example-1.py",
    "developer-guide/advanced-usage/extraction/search-text/example-2.py",
    "developer-guide/advanced-usage/extraction/search-text/example-3.py",
    "developer-guide/advanced-usage/extraction/search-text/example-4.py",
    "developer-guide/advanced-usage/extraction/search-text/example-5.py",
    "developer-guide/advanced-usage/extraction/search-text/advanced_search.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/example-1.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/example-2.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/example-3.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/get_file_format.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/example-5.py",
    "developer-guide/advanced-usage/loading/load-specific-file-formats/safe_load_with_format.py",
    "developer-guide/advanced-usage/working-with-archives/working-with-containers/print_text.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/example-1.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/example-2.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/save_images_with_custom_names.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/example-4.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/save_images_by_page.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/save_images_by_type.py",
    "developer-guide/advanced-usage/working-with-images/extract-images-to-files/batch_save_images.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/get_search_results_with_context.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/extract_multiple_highlights.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/create_document_preview.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/extract_highlight_with_words.py",
    "developer-guide/advanced-usage/extraction/extract-highlights/create_toc_with_previews.py",
    "developer-guide/advanced-usage/working-with-images/working-with-images/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/extract_hyperlinks_from_structure.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/analyze_tables.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/extract_formatted_text.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/save_structure_to_file.py",
    "developer-guide/advanced-usage/extraction/extract-text-structure/extract_section_info.py",
    "developer-guide/advanced-usage/options/example-1.py",
    "developer-guide/advanced-usage/errors-and-exceptions/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-areas/example-1.py",
    "developer-guide/advanced-usage/extraction/extract-text-areas/example-2.py",
    "developer-guide/advanced-usage/extraction/extract-text-areas/example-3.py",
    "developer-guide/advanced-usage/extraction/extract-text-areas/example-4.py",
    "developer-guide/advanced-usage/extraction/extract-text-areas/extract_from_regions.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
]

print_intro()

# Get current environment variables from the parent process
env = os.environ.copy()

# Run each example script
for example in examples:
    current_dir = os.path.dirname(__file__)
    example_path = os.path.join(current_dir, example)
    example_dir = os.path.dirname(example_path)

    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        # Execute the example script in the current environment
        subprocess.run(
            [sys.executable, example_path], 
            cwd=example_dir, 
            check=True, 
            env=env
        )
        print(f"{GREEN}Completed {example}{RESET}\n")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error running {example}: {e}{RESET}\n")
