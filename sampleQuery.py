import san
import matplotlib.pyplot as plt
san.ApiConfig.api_key = 'my-api-key'

data = san.get(
  "price_usd/ethereum",
  from_date="2019-01-01T00:00:00Z",
  to_date="2021-10-07T00:00:00Z",
  interval="1d"
)

plt.plot(data.value)
plt.xlabel('date')
plt.ylabel('eth price (usd)')
plt.title('ethereum price')
plt.show()