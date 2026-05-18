def expert_system():
    print("=== Information Management Expert System ===")

    # User inputs
    file_type = input("Enter file type (text/video/image): ").lower()
    size = input("Enter file size (small/large): ").lower()
    importance = input("Enter importance (low/medium/high): ").lower()
    usage = input("Is it frequently used? (yes/no): ").lower()

    print("\n--- Recommendation ---")

    # Storage decision
    if size == "large" and importance == "high":
        print("Store in Cloud Storage and keep a Backup.")
    elif size == "small" and importance == "low":
        print("Store Locally.")
    elif importance == "high" and usage == "yes":
        print("Store in Fast-access Storage (SSD/Cloud).")
    else:
        print("Store in Standard Storage.")

    # Backup decision
    if importance == "high":
        print("Backup: Required.")
    elif importance == "medium":
        print("Backup: Optional.")
    else:
        print("Backup: Not needed.")

    # Archiving decision
    if usage == "no" and importance == "medium":
        print("Archive the file.")
    elif usage == "no" and importance == "low":
        print("Consider deleting or archiving.")
    else:
        print("No archiving needed.")

# Run system
expert_system()