import time

from scrap import scrape_instance


def main():
    links = scrape_instance.extract_links()
    titles = scrape_instance.extract_titles()

    scrape_instance.save_json_extracted(links, "data/links.json")
    scrape_instance.save_json_extracted(titles, "data/titles.json")
    scrape_instance.save_all_html_content()


if __name__ == "__main__":
    main()
