import logging
import os
import requests


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
    FileUpdater.update("https://carbos-backend-0ace626eaf33.herokuapp.com/jobs/?board=SWE_2024_SUMMER_INTERNSHIP", "./README.md")


if __name__ == "__main__":
    update_readme()
