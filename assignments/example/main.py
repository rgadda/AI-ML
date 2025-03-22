from src.preprocessing import normalize_data

def main():
    raw_data = [10, 20, 15, 30, 25]
    print("Original data:", raw_data)
    normalized = normalize_data(raw_data)
    print("Normalized data:", normalized)

if __name__ == "__main__":
    main()