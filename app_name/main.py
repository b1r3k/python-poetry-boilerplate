import argparse

from .config import settings
from .logging import root_logger as logger


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="your name")
    args = parser.parse_args()
    logger.info(f"Hello, {args.name}! My name is {settings.APP_NAME}")


if __name__ == "__main__":
    cli()
