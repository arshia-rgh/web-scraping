from scrape import scrape_instance


def main():
    links = scrape_instance.extract_links()
    titles = scrape_instance.extract_titles()

    scrape_instance.save(links, "data/links.json")
    scrape_instance.save(titles, "data/titles.json")


if __name__ == "__main__":
    main()
