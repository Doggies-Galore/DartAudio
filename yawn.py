def extract_text(line):
    # Split the line by commas
    parts = line.split(',')
    # Check if there are at least three parts (two commas)
    if len(parts) >= 3:
        # Return the text between the 2nd and 3rd comma
        return parts[2]
    else:
        return None

def main():
    input_file = "stations.txt"
    output_file = "brief.txt"

    with open(input_file, "r") as infile:
        with open(output_file, "w") as outfile:
            for line in infile:
                # Extract text between the 2nd and 3rd comma
                extracted_text = extract_text(line)
                if extracted_text:
                    # Write extracted text to output file
                    outfile.write(extracted_text.strip() + "\n")

    print("Extraction completed. Check 'brief.txt'.")

if __name__ == "__main__":
    main()
