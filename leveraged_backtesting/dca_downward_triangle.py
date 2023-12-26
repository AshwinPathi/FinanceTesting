from typing import List

import utils


def generate_underlying_data(num_days: int) -> List[utils.DayData]:
	"""Generates a set of data that always goes down by 1 percent every day for the first half,
	then 1% up for the second half.
	"""
	start_price = 100
	price_percent_increase_per_day = 0.01
	flip_growth_day = num_days // 2

	data: List[utils.DayData] = []

	for day_i in range(num_days):
		open_price = start_price if day_i == 0 else data[day_i - 1].close_price
		if day_i >= flip_growth_day:
			close_price = open_price * (1 + price_percent_increase_per_day)
		else:
			close_price = open_price * (1 - price_percent_increase_per_day)

		data.append(utils.DayData(
			day=day_i,
			open_price=open_price,
			close_price=close_price
		))

	return data


def dca(series: List[utils.DayData]):
	dollar_amount_per_day = 10
	number_of_invested_days = 0

	stop_buying_day = len(series) // 2 # 50
	shares: List[utils.Order] = []

	for day, data in enumerate(series):
		buy_price = data.close_price

		# Buy on the way down
		if day < stop_buying_day:
			number_of_invested_days += 1
			shares.append(utils.Order(
				quantity=dollar_amount_per_day/buy_price,
				price=buy_price
			))

	# calculate PNL
	total_shares = sum([order.quantity for order in shares])
	final_portfolio_value = total_shares * series[-1].close_price
	total_invested = dollar_amount_per_day * number_of_invested_days
	print(f'Total invested value: {total_invested}')
	print(f'Final portfolio value: {final_portfolio_value}')
	print(f'Total shares: {total_shares}')
	print()

if __name__ == '__main__':
	num_days = 100
	leverage = 3

	data = generate_underlying_data(num_days)
	lev_data = utils.generate_leveraged_data(data, leverage)

	utils.compare_returns(data, lev_data)
	print()
	print('unleveraged')
	dca(data)
	print('leveraged')
	dca(lev_data)
	
	#utils.plot_comparison(data, lev_data)
