from groupdocs.parser import Metered

def set_metered_license():
    # Set your public and private keys
    public_key = "******"
    private_key = "******"
    
    # Instantiate Metered and set keys
    metered = Metered()
    metered.set_metered_key(public_key, private_key)
    
    # Get amount (MB) consumed
    consumption_quantity = Metered.get_consumption_quantity()
    print(f"Amount (MB) consumed: {consumption_quantity}")
    
    # Get count of credits consumed
    consumption_credit = Metered.get_consumption_credit()
    print(f"Credits consumed: {consumption_credit}")

if __name__ == "__main__":
    set_metered_license()