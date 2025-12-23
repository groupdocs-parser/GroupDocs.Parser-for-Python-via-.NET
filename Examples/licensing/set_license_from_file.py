from groupdocs.parser import License

def set_license_from_file():
    # Create an instance of License class
    license = License()
    
    # Set the license from file path
    license.set_license("path/to/GroupDocs.Parser.lic")

if __name__ == "__main__":
    set_license_from_file()