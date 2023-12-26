from typing import List
import random


import utils


def generate_underlying_data(num_days: int) -> List[utils.DayData]:
	start_price = 100
	price_increase_per_day = 1

	# Number of times the stock goes up or down
	num_ups = num_days // 2
	num_down = num_days - num_ups

	data: List[utils.DayData] = []

	for day_i in range(num_days):
		open_price = start_price if day_i == 0 else data[day_i - 1].close_price

		direction = random.randint(0, 1)
		if direction == 1:
			if num_ups > 0:
				close_price = open_price + price_increase_per_day
			else:
				close_price = open_price - price_increase_per_day
		if direction == 0:
			if num_down > 0:
				close_price = open_price - price_increase_per_day
			else:
				close_price = open_price + price_increase_per_day


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

	utils.plot_comparison(data, lev_data)

