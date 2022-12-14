"""CSIMarket Model"""
__docformat__ = "numpy"

import logging
from typing import List

import requests
from bs4 import BeautifulSoup

from openbb_terminal.decorators import log_start_end

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_suppliers(symbol: str) -> List[str]:
    """Get suppliers from ticker provided. [Source: CSIMarket]

    Parameters
    ----------
    symbol: str
        Ticker to select suppliers from

    Returns
    -------
    list[str]
        List of suppliers for ticker provided
    """
    # TODO: This link has a lot more data that we can display
    # TODO: We could at least sort the tickers based on market cap
    url_supply_chain = (
        f"https://csimarket.com/stocks/competitionNO3.php?supply&code={symbol.upper()}"
    )
    text_supplier_chain = BeautifulSoup(requests.get(url_supply_chain).text, "lxml")

    l_supplier = list()
    for supplier in text_supplier_chain.findAll(
        "td", {"class": "svjetlirub11 block al"}
    ):
        l_supplier.append(supplier.text.replace("\n", "").strip())

    return l_supplier


@log_start_end(log=logger)
def get_customers(symbol: str) -> List[str]:
    """Print customers from ticker provided

    Parameters
    ----------
    symbol: str
        Ticker to select customers from

    Returns
    -------
    list[str]
        List of customers for ticker provided
    """
    # TODO: This link has a lot more data that we can display
    # TODO: We could at least sort the tickers based on market cap
    url_customer_chain = (
        f"https://csimarket.com/stocks/custexNO.php?markets&code={symbol.upper()}"
    )
    text_customer_chain = BeautifulSoup(requests.get(url_customer_chain).text, "lxml")

    l_customer = list()
    for customer in text_customer_chain.findAll("td", {"class": "plava svjetlirub"}):
        l_customer.append(customer.text)

    return l_customer
