from typing import List

import utils


def generate_underlying_data(num_days: int) -> List[utils.DayData]:
	"""Generates a set of data that always goes up by 1 percent every day for the first half,
	then 1% down for the second half.
	"""
	start_price = 100
	price_percent_increase_per_day = 0.01
	flip_growth_day = num_days // 2

	data: List[utils.DayData] = []

	for day_i in range(num_days):
		open_price = start_price if day_i == 0 else data[day_i - 1].close_price
		if day_i >= flip_growth_day:
			close_price = open_price * (1 - price_percent_increase_per_day)
		else:
			close_price = open_price * (1 + price_percent_increase_per_day)

		data.append(utils.DayData(
			day=day_i,
			open_price=open_price,
			close_price=close_price
		))

	return data


if __name__ == '__main__':
	num_days = 100
	leverage = 3

	data = generate_underlying_data(num_days)
	lev_data = utils.generate_leveraged_data(data, leverage)

	utils.compare_returns(data, lev_data)
	utils.plot_comparison(data, lev_data)
