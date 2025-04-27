def calculate_discount(total_amount, is_repetitive_customer):
    discount = 0

    # Check amount-based discount
    if total_amount >= 75000:
        discount += 50
    elif total_amount >= 30000:
        discount += 30
    elif total_amount >= 15000:
        discount += 10

    # Check repetitive customer discount
    if is_repetitive_customer:
        discount += 5

    # Calculate final amount after discount
    discount_amount = (discount / 100) * total_amount
    final_amount = total_amount - discount_amount

    return discount, discount_amount, final_amount


# Example usage
def main():
    try:
        total_amount = float(input("Enter Total Bill Amount: Rs. "))
        repeat_customer_input = input("Is the customer a repetitive customer? (yes/no): ").strip().lower()
        is_repetitive_customer = repeat_customer_input in ['yes', 'y']

        discount_percent, discount_amount, final_amount = calculate_discount(total_amount, is_repetitive_customer)

        print("\n----- Super Store Bill -----")
        print(f"Total Bill Amount: Rs.{total_amount:.2f}")
        print(f"Total Discount Applied: {discount_percent}%")
        print(f"Discount Amount: Rs.{discount_amount:.2f}")
        print(f"Final Amount to Pay: Rs.{final_amount:.2f}")
        print("----------------------------")

    except ValueError:
        print("Invalid input. Please enter numeric value for amount.")

if __name__ == "__main__":
    main()
