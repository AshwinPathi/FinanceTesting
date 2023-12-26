from typing import List

import utils


def generate_underlying_data(num_days: int) -> List[utils.DayData]:
	"""Generates a set of data that always goes up by 1 unit every day."""
	start_price = 100
	price_increase_per_day = 1

	data: List[utils.DayData] = []

	for day_i in range(num_days):
		open_price = start_price if day_i == 0 else data[day_i - 1].close_price
		data.append(utils.DayData(
			day=day_i,
			open_price=open_price,
			close_price=open_price + price_increase_per_day
		))	
	return data


if __name__ == '__main__':
	num_days = 100
	leverage = 3

	data = generate_underlying_data(num_days)
	lev_data = utils.generate_leveraged_data(data, leverage)

	utils.plot_comparison(data, lev_data)

