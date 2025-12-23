from groupdocs.parser import License

def set_license_from_stream():
    # Open the license file
    with open("path/to/GroupDocs.Parser.lic", "rb") as stream:
        # Create an instance of License class
        license = License()
        
        # Set the license from stream
        license.set_license(stream)

if __name__ == "__main__":
    set_license_from_stream()