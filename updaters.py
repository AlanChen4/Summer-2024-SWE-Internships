import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FileUpdater:
    """
    Used to fetches data from a given url and write to a file
    """

    @staticmethod
    def update(url: str, output: str) -> None:
        """
        :param url: The URL to read data from
        :param output: The path and filename to save the output
        """
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            with open(output, "w", encoding="utf-8") as file:
                file.write(response.text)
                logging.info(f"Successfully saved data to {output}")
        else:
            logging.error(f"Unable to get data from {url}")


def update_readme() -> None:
    url = os.environ.get("README_GENERATOR_URL", None)
    if url is None:
        logging.error("Please set a variable for README_GENERATOR_URL to call this method")
        return

    FileUpdater.update(url, "./README.md")


if __name__ == '__main__':
    update_readme()