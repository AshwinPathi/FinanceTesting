from typing import List
import random


import utils


def generate_underlying_data(num_days: int) -> List[utils.DayData]:
	"""Generates a set of data that goes up for an equal amount of days as it goes down,
	i.e it should end at a price that is equal to what it started at. Each day's price movement
	is random with a 50/50 chance of going up or down on a given day, assuming we have not exhausted
	all our up or down days.
	"""
	start_price = 100
	price_percent_increase_per_day = 0.01

	# Number of times the stock goes up or down
	num_ups = num_days // 2
	num_down = num_days - num_ups

	data: List[utils.DayData] = []

	for day_i in range(num_days):
		open_price = start_price if day_i == 0 else data[day_i - 1].close_price

		direction = random.randint(0, 1)
		if direction == 1:
			if num_ups > 0:
				close_price = open_price * (1 + price_percent_increase_per_day)
				num_ups -= 1
			else:
				close_price = open_price * (1 - price_percent_increase_per_day)
		if direction == 0:
			if num_down > 0:
				close_price = open_price * (1 - price_percent_increase_per_day)
				num_down -= 1
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
