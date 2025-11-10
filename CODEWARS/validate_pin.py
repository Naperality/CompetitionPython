# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot 
# contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    # return sum(1 if num.isdigit() else -10 for num in pin) in (4,6)
    return len(pin) in (4,6) and pin.isdigit()

print(validate_pin(input('Enter Pin Number: ')))