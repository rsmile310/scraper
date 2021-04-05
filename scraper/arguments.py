from argparse import ArgumentParser


def argparse_setup() -> ArgumentParser.parse_args:
    """Setup and return argparse."""
    parser = ArgumentParser()

    parser.add_argument(
        "-s", "--scrape", help="scrape product prices", action="store_true",
    )

    parser.add_argument(
        "-a", "--add", help="Add a product", action="store_true",
    )

    parser.add_argument(
        "--reset", help="delete data for each product in records.json, such as prices of each recorded day", action="store_true",
    )

    parser.add_argument(
        "--hard-reset", help="delete all content in records.json and products.csv", action="store_true",
    )

    parser.add_argument(
        "-c", "--category", help="the category the product is going to be in", type=str
    )

    parser.add_argument(
        "--threads", help="use threads when scraping product info", action="store_true"
    )

    parser.add_argument("-u", "--url", help="the url to the product", type=str)

    validate_arguments(parser)

    return parser.parse_args()


def validate_arguments(parser: ArgumentParser) -> None:
    """Validate arguments"""
    args = parser.parse_args()

    if args.add:
        if not args.category or not args.url:
            parser.error("When using --add, then --category and --url is required")
