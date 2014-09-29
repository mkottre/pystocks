import ystockquote, sys

y = ystockquote

def print_stock(ticker):
	company = y.get_company_name(ticker)
	company = company.replace('"', '').strip()
	if len(company) <= 15:
		print(ticker+'\t'+company+'\t\t'+y.get_last_trade_price(ticker)+'\t'+y.get_market_cap(ticker)+'\t\t'+y.get_change(ticker)+'\t'+y.get_revenue(ticker))
	else:
		print(ticker+'\t'+company+'\t'+y.get_last_trade_price(ticker)+'\t'+y.get_market_cap(ticker)+'\t\t'+y.get_change(ticker)+'\t'+y.get_revenue(ticker))

print("TICKER\tCOMPANY\t\t\tPRICE\tMRKT CAP\tCHANGE\tREVENUE")

for counter in range(1, len(sys.argv)):
	print_stock(sys.argv[counter])
