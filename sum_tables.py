from playwright.sync_api import sync_playwright
import re

URLS = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=69",
    "https://sanand0.github.io/tdsdata/js_table/?seed=70",
    "https://sanand0.github.io/tdsdata/js_table/?seed=71",
    "https://sanand0.github.io/tdsdata/js_table/?seed=72",
    "https://sanand0.github.io/tdsdata/js_table/?seed=73",
    "https://sanand0.github.io/tdsdata/js_table/?seed=74",
    "https://sanand0.github.io/tdsdata/js_table/?seed=75",
    "https://sanand0.github.io/tdsdata/js_table/?seed=76",
    "https://sanand0.github.io/tdsdata/js_table/?seed=77",
    "https://sanand0.github.io/tdsdata/js_table/?seed=78",
]

def extract_numbers(text):
    return [int(x) for x in re.findall(r"-?\d+", text)]

def main():
    total = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in URLS:
            page.goto(url)
            page.wait_for_selector("table")

            cells = page.query_selector_all("table td")

            for cell in cells:
                nums = extract_numbers(cell.inner_text())
                for n in nums:
                    total += n

        browser.close()

    print("FINAL TOTAL:", total)

if __name__ == "__main__":
    main()
