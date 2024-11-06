import requests
from bs4 import BeautifulSoup
import os

# Function to fetch HTML content of a page
def fetch_html(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve page: {url}")
        return None

# Function to extract PDF download link from Project Gutenberg
def get_pdf_link(book_url):
    html_content = fetch_html(book_url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Searching for the PDF download link
        pdf_link = soup.find('a', {'title': 'Download this ebook as a PDF'})
        if pdf_link:
            return "https://www.gutenberg.org" + pdf_link.get('href')
    return None

# Function to download the PDF
def download_pdf(pdf_url, download_folder):
    pdf_name = pdf_url.split('/')[-1]
    pdf_path = os.path.join(download_folder, pdf_name)
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(pdf_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {pdf_name}")
    else:
        print(f"Failed to download: {pdf_url}")

# Main function to download the PDF
def download_book_pdf(book_url, download_folder='downloaded_books'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    pdf_link = get_pdf_link(book_url)
    if pdf_link:
        download_pdf(pdf_link, download_folder)
    else:
        print("PDF link not found for this book.")

# Example usage: Replace with actual book URL from Project Gutenberg
if __name__ == '__main__':
    # Provide the URL of the book page from Project Gutenberg
    book_url = input("Enter the URL of the book page (e.g., https://www.gutenberg.org/ebooks/1342): ")
    download_book_pdf(book_url)
