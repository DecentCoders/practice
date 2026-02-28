import os

def manage_env_vars():
    # 1. Print the PATH environment variable
    try:
        path_var = os.environ["PATH"]
        print("=== PATH Environment Variable ===")
        # Split PATH into individual entries (easier to read)
        path_entries = path_var.split(os.pathsep)  # os.pathsep = ; (Windows) / : (macOS/Linux)
        for i, entry in enumerate(path_entries, 1):
            print(f"{i}. {entry}")
    except KeyError:
        print("Error: PATH environment variable not found.")

    # 2. Add a temporary environment variable (only exists for the script's runtime)
    os.environ["MY_VAR"] = "os_practice"
    print("\n=== Custom Environment Variable ===")
    print(f"MY_VAR: {os.environ['MY_VAR']}")

    # Optional: Remove the custom env var (uncomment if needed)
    # del os.environ["MY_VAR"]

manage_env_vars()