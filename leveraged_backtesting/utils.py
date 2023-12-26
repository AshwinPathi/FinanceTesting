# Helper utilities for structs and leverage claculation
from typing import NamedTuple, List

import matplotlib.pyplot as plt



class DayData(NamedTuple):
	day: int
	open_price: float
	close_price: float

	def percent_change(self) -> float:
		return (self.close_price - self.open_price) / self.open_price


def generate_leveraged_data(underlying_data: List[DayData], leverage: float) -> List[DayData]:

	leveraged_data: List[DayData] = []

	for day_i, data in enumerate(underlying_data):
		leveraged_percent_increase = leverage * data.percent_change()
		
		open_price = data.open_price if day_i == 0 else leveraged_data[day_i - 1].close_price
		close_price = open_price + (open_price * leveraged_percent_increase)

		leveraged_data.append(DayData(
			day=day_i,
			open_price=open_price,
			close_price=close_price
		))
		
	return leveraged_data


def plot_comparison(underlying: List[DayData], leveraged: List[DayData]):
	assert len(underlying) == len(leveraged)

	num_days = len(underlying)
	x_axis = [i for i in range(num_days)]

	open_prices_underlying = [data.open_price for data in underlying]
	open_prices_leveraged = [data.open_price for data in leveraged]

	plt.plot(x_axis, open_prices_underlying)

	plt.plot(x_axis, open_prices_leveraged, '-.')

	plt.xlabel("Day since start of data")
	plt.ylabel("Open price")
	plt.title('Levered vs underlying open prices over time')
	plt.show()


def compare_returns(underlying: List[DayData], leveraged: List[DayData]):
	returns_underlying = 100 * (underlying[-1].close_price - underlying[0].open_price) / underlying[0].open_price
	returns_leveraged = 100 * (leveraged[-1].close_price - leveraged[0].open_price) / leveraged[0].open_price

	print(f'Returns for unlevered (between open first day and close last day):\n{returns_underlying}%')
	print()
	print(f'Returns for levered (between open first day and close last day):\n{returns_leveraged}%')
