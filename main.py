import yfinance as yf
import pandas as pd

class Portfolio:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.fetch_data()

    def fetch_data(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)

    def validate_date_range(self, start_date, end_date):
        return start_date in self.data.index and end_date in self.data.index

    def calculate_profit(self, start_date, end_date):
        if not self.validate_date_range(start_date, end_date):
            return None 

        start_price = self.data.loc[start_date, 'Close']
        end_price = self.data.loc[end_date, 'Close']
        total_profit = (end_price - start_price) / start_price * 100
        return total_profit
    
    def calculate_annualized_profit(self, start_date, end_date):
        if not self.validate_date_range(start_date, end_date):
            return None 
        
        start_price = self.data.loc[start_date, 'Close']
        end_price = self.data.loc[end_date, 'Close']
        days_between = (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days
        years_fraction = days_between / 365.25
        total_profit = ((end_price/start_price)**years_fraction - 1) * 100
        return total_profit

if __name__ == '__main__':

    ## Variables
    etf_symbol = 'SPY'
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    profit_start_date = '2020-01-02'
    profit_end_date = '2021-01-29'

    annualized_profit_start_date = '2020-01-02'
    annualized_profit_end_date = '2021-01-29'

    portfolio = Portfolio(etf_symbol, start_date, end_date)
    profit = portfolio.calculate_profit(profit_start_date, profit_end_date)
    annualized_profit = portfolio.calculate_annualized_profit(annualized_profit_start_date, annualized_profit_end_date)

    if profit is None or annualized_profit is None:
        print('Invalid dates')
    else:
        print(f'Profit: {profit:.2f} %')
        print(f'Annualized profit: {annualized_profit:.2f} %')