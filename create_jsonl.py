import json
import sys
import os

def generate_jsonl(source_folder_path, summary_folder_path, output_folder_name):
    # Set file names
    source_file_name = "test.source"
    summary_file_name = "test_summaries.txt"

    # Create file paths
    source_file_path = os.path.join(source_folder_path, source_file_name)
    summary_file_path = os.path.join(summary_folder_path, summary_file_name)

    # Read source documents
    with open(source_file_path, "r") as source_file:
        sources = source_file.readlines()

    # Read summaries
    with open(summary_file_path, "r") as summary_file:
        summaries = summary_file.readlines()

    # Create output folder
    os.makedirs(output_folder_name, exist_ok=True)

    # Set output file name
    output_file_name = "data-dev.jsonl"
    output_file_path = os.path.join(output_folder_name, output_file_name)

    # Generate jsonl output
    with open(output_file_path, "w") as output_file:
        for i, (source, summary) in enumerate(zip(sources, summaries)):
            id = i + 1
            json_line = json.dumps({"id": id, "text": source.strip(), "claim": summary.strip(), "label": "CORRECT"})
            output_file.write(json_line + "\n")

    print(f"Generated output file: {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 create_jsonl.py <source_folder_path> <summary_folder_path> <output_folder_name>")
        sys.exit(1)

    source_folder_path = sys.argv[1]
    summary_folder_path = sys.argv[2]
    output_folder_name = sys.argv[3]

    generate_jsonl(source_folder_path, summary_folder_path, output_folder_name)

