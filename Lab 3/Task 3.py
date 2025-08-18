def calculate_power_bill(units_consumed, customer_type="residential"):
    """
    Calculate power bill based on units consumed and customer type.
    
    Args:
        units_consumed (float): Number of units consumed
        customer_type (str): Type of customer - "residential", "commercial", or "industrial"
        
    Returns:
        dict: Dictionary containing bill details
    """
    
    # Tariff rates (per unit) for different customer types
    tariffs = {
        "residential": {
            "slab1": {"limit": 100, "rate": 3.50},
            "slab2": {"limit": 200, "rate": 4.50},
            "slab3": {"limit": float('inf'), "rate": 5.50}
        },
        "commercial": {
            "slab1": {"limit": 200, "rate": 5.00},
            "slab2": {"limit": 500, "rate": 6.50},
            "slab3": {"limit": float('inf'), "rate": 7.50}
        },
        "industrial": {
            "slab1": {"limit": 500, "rate": 6.00},
            "slab2": {"limit": 1000, "rate": 7.50},
            "slab3": {"limit": float('inf'), "rate": 8.50}
        }
    }
    
    # Fixed charges based on customer type
    fixed_charges = {
        "residential": 50,
        "commercial": 100,
        "industrial": 200
    }
    
    if customer_type not in tariffs:
        raise ValueError("Invalid customer type. Use 'residential', 'commercial', or 'industrial'")
    
    if units_consumed < 0:
        raise ValueError("Units consumed cannot be negative")
    
    # Get tariff structure for customer type
    tariff = tariffs[customer_type]
    fixed_charge = fixed_charges[customer_type]
    
    # Calculate bill based on slabs
    total_amount = fixed_charge
    remaining_units = units_consumed
    slab_details = []
    
    for slab_name, slab_info in tariff.items():
        if remaining_units <= 0:
            break
            
        if slab_name == "slab1":
            units_in_slab = min(remaining_units, slab_info["limit"])
        elif slab_name == "slab2":
            units_in_slab = min(remaining_units, slab_info["limit"] - tariff["slab1"]["limit"])
        else:  # slab3
            units_in_slab = remaining_units
            
        if units_in_slab > 0:
            slab_amount = units_in_slab * slab_info["rate"]
            total_amount += slab_amount
            
            slab_details.append({
                "slab": slab_name,
                "units": units_in_slab,
                "rate": slab_info["rate"],
                "amount": slab_amount
            })
            
            remaining_units -= units_in_slab
    
    # Calculate taxes and surcharges
    gst = total_amount * 0.05  # 5% GST
    surcharge = total_amount * 0.02  # 2% surcharge
    
    final_amount = total_amount + gst + surcharge
    
    return {
        "customer_type": customer_type,
        "units_consumed": units_consumed,
        "fixed_charge": fixed_charge,
        "slab_details": slab_details,
        "subtotal": total_amount,
        "gst": gst,
        "surcharge": surcharge,
        "total_amount": final_amount
    }


def display_bill(bill_details):
    """
    Display the power bill in a formatted way.
    
    Args:
        bill_details (dict): Bill details from calculate_power_bill function
    """
    print("\n" + "=" * 50)
    print("                    POWER BILL")
    print("=" * 50)
    print(f"Customer Type:     {bill_details['customer_type'].title()}")
    print(f"Units Consumed:    {bill_details['units_consumed']:.2f} units")
    print("-" * 50)
    
    print("SLAB WISE BREAKDOWN:")
    print("-" * 50)
    for slab in bill_details['slab_details']:
        print(f"{slab['slab'].upper()}: {slab['units']:.2f} units × ₹{slab['rate']:.2f} = ₹{slab['amount']:.2f}")
    
    print("-" * 50)
    print(f"Fixed Charge:      ₹{bill_details['fixed_charge']:.2f}")
    print(f"Subtotal:          ₹{bill_details['subtotal']:.2f}")
    print(f"GST (5%):          ₹{bill_details['gst']:.2f}")
    print(f"Surcharge (2%):    ₹{bill_details['surcharge']:.2f}")
    print("=" * 50)
    print(f"TOTAL AMOUNT:      ₹{bill_details['total_amount']:.2f}")
    print("=" * 50)


def get_user_input():
    """
    Get user input for power bill calculation.
    
    Returns:
        tuple: (units_consumed, customer_type)
    """
    print("Power Bill Calculator")
    print("=" * 30)
    
    # Get units consumed
    while True:
        try:
            units = float(input("Enter units consumed: "))
            if units < 0:
                print("Units cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get customer type
    print("\nCustomer Types:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    
    while True:
        choice = input("Select customer type (1/2/3): ").strip()
        if choice == "1":
            customer_type = "residential"
            break
        elif choice == "2":
            customer_type = "commercial"
            break
        elif choice == "3":
            customer_type = "industrial"
            break
        else:
            print("Please select 1, 2, or 3.")
    
    return units, customer_type


def main():
    """
    Main function to run the power bill calculator.
    """
    # Demo examples
    print("Power Bill Calculation Examples")
    print("=" * 40)
    
    # Example 1: Residential customer
    print("\nExample 1: Residential Customer (150 units)")
    bill1 = calculate_power_bill(150, "residential")
    display_bill(bill1)
    
    # Example 2: Commercial customer
    print("\nExample 2: Commercial Customer (300 units)")
    bill2 = calculate_power_bill(300, "commercial")
    display_bill(bill2)
    
    # Example 3: Industrial customer
    print("\nExample 3: Industrial Customer (800 units)")
    bill3 = calculate_power_bill(800, "industrial")
    display_bill(bill3)
    
    # Interactive calculation
    print("\n" + "=" * 50)
    print("Interactive Power Bill Calculator")
    print("=" * 50)
    
    try:
        units, customer_type = get_user_input()
        bill = calculate_power_bill(units, customer_type)
        display_bill(bill)
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()