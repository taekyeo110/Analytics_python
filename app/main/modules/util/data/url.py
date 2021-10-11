from urllib.parse import parse_qs, urlparse


def get_params(url: str):
    """
            return report data (with parsing)
    """
    return parse_qs(urlparse(url).query)
