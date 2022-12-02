import logging
import os

import internetarchive
from retry import retry


def main():
    """Upload the provided files to archive.org."""
    # Get env variables
    access_key = os.getenv("access-key")
    secret_key = os.getenv("secret-key")
    identifier = os.getenv("identifier")
    files = os.getenv("files")

    # Set the logger
    logging.basicConfig(level="DEBUG", format="%(asctime)s - %(name)s - %(message)s")
    logger = logging.getLogger(__name__)

    logger.debug(f"Uploading {files}")
    kwargs = dict(
        access_key=access_key,
        secret_key=secret_key,
        verbose=True,
        files=files,
    )
    _upload(identifier, **kwargs)


@retry(tries=5, delay=30, backoff=2)
def _upload(identifier: str, **kwargs):
    internetarchive.upload(identifier, **kwargs)


if __name__ == "__main__":
    main()
