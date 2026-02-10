passwords = ["12345", "SecurePath7", "mypassword99", "PythonIsCool2026", "admin"]

for pw in passwords:
    # Rule 1: Length
    length_ok = len(pw) >= 8
    
    # Rule 2: Contains a number
    has_number = any(char.isdigit() for char in pw)
    
    # Rule 3: No "password" (case-insensitive)
    not_generic = "password" not in pw.lower()

    if length_ok and has_number and not_generic:
        print(f"Valid: {pw}")
    else:
        print(f"Invalid: {pw}")