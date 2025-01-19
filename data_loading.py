from faker import Faker
fake = Faker()
import re



def is_android_key(line):
    """
    Checks if a line resembles an Android app link or encryption key.
    - Starts with `android://`
    - Contains `.android` suffix
    """
    # Match Android-specific patterns
    android_pattern = r'^android://[A-Za-z0-9+/=_-]+@com\.[A-Za-z0-9._-]+'
    android_suffix_pattern = r'\.android'

    return re.match(android_pattern, line) or re.search(android_suffix_pattern, line)

def process_file(filename, output_file):
    """
    Process a file line by line, ignoring Android keys and irrelevant lines.
    """
    with open(filename, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as out:
        record = ""  # Buffer to store the current URL or multi-line record
        for line in file:
            line = line.strip()

            # Ignore Android-specific keys
            if is_android_key(line):
                continue

            # Process valid URLs
            if line.startswith(("http://", "https://", "www.")):
                if record and ":" in record:
                    process_record(record, out)
                record = line
            else:
                record += " " + line

        if record and ":" in record:
            process_record(record, out)

def process_record(record, out):
    """
    Process a single record, extracting the full URL and credentials.
    """
    if "://" in record:
        url_prefix = record.split("://", 1)[0] + "://"
        rest_of_record = record.split("://", 1)[1]
        if ":" in rest_of_record:
            url, credentials = rest_of_record.split(":", 1)
            url = url_prefix + url
            first_name = fake.first_name()
            last_name = fake.last_name()
            out.write(f"{url}:{first_name}:{last_name}\n")

