import os
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath("index.html")

        # Go to the local file
        page.goto(f"file://{file_path}")

        # Wait for the fade-in animation to complete
        page.wait_for_timeout(2000)

        # Verify the new title is visible
        site_title = page.locator(".site-title")
        expect(site_title).to_be_visible()
        expect(site_title).to_have_text("PizzaDojo2Go.com")

        # Verify the old title is not visible
        old_title_h1 = page.locator(".text-logo h1")
        expect(old_title_h1).not_to_be_visible()

        # Verify the main headline is still there and is visible
        headline = page.locator(".headline")
        expect(headline).to_be_visible()
        expect(headline).to_have_text("Coming in 2026 to a community near you!")

        # Verify the buttons are visible
        about_us_btn = page.get_by_role("link", name="About Us")
        expect(about_us_btn).to_be_visible()

        # Take a screenshot
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run_verification()