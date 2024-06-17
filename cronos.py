import requests
import time

def fetch_page_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print("Error fetching URL:", e)
    return None

def main():
    target_url = "https://www.pudn.com/"  # Specify your target URL here
    interval_seconds = 120  # Set the time period in seconds after which you want to fetch the page source
    file_number = 1

    while True:
        page_source = fetch_page_source(target_url)
        if page_source:
            output_file = f"output{file_number}.html"
            with open(output_file, "w", encoding='utf-8') as file:
                file.write(page_source)
            print(f"Page source saved to {output_file}.")
            file_number += 1
        else:
            print("Failed to fetch page source.")

        time.sleep(interval_seconds)  # Wait for the specified time period before fetching again

if __name__ == "__main__":
    main()