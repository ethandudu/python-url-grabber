# License: GPL 3.0
import requests
from bs4 import BeautifulSoup


def get_links(url):
    """
    Return all the links from a given URL.

    Args:
        url (str): The URL from which to extract the links.

    Returns:
        list: A list containing the links found.
    """

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    urls = duplicate_remover(urls)
    return urls


def get_http_links(url):
    """
    Return the HTTP links from a given URL.

    Args:
        url (str): The URL from which to extract the links.
    
    Returns:
        list: A list containing the HTTP links found.
    """

    urls = get_links(url)
    http_urls = []
    for link in urls:
        if link and link.startswith('http') and not link.startswith('https'):
            http_urls.append(link)
    http_urls = duplicate_remover(http_urls)
    return http_urls


def get_https_links(url):
    """
    Return the HTTPS links from a given URL.

    Args:
        url (str): The URL from which to extract the links.

    Returns:
        list: A list containing the HTTPS links found.
    """

    urls = get_links(url)
    https_urls = []
    for link in urls:
        if link and link.startswith('https'):
            https_urls.append(link)
    https_urls = duplicate_remover(https_urls)
    return https_urls


def get_email_addresses(url):
    """
    Return the email addresses from a given URL.

    Args:
        url (str): The URL from which to extract the email addresses.

    Returns:
        list: A list containing the email addresses found.
    """

    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    emails = []
    for email in soup.find_all('a'):
        if email.get('href') and email.get('href').startswith('mailto:'):
            emails.append(email.get('href').split(':')[1])
    emails = duplicate_remover(emails)
    return emails


def duplicate_remover(lst):
    """
    Remove duplicates from a list.

    Args:
        lst (list): The list from which to remove duplicates.

    Returns:
        list: A list with no duplicates.
    """
    return list(set(lst))