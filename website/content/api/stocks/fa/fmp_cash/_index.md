## Get underlying data 
### stocks.fa.fmp_cash(symbol: str, limit: int = 5, quarterly: bool = False, ratios: bool = False, plot: bool = False) -> pandas.core.frame.DataFrame

Get cash flow

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    limit : int
        Number to get
    quarterly : bool, optional
        Flag to get quarterly data, by default False
    ratios: bool
        Shows percentage change, by default False
    plot: bool
        If the data shall be formatted ready to plot

    Returns
    -------
    pd.DataFrame
        Dataframe of company cash flow
