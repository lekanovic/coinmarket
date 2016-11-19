from coinmarketcap import Market
coinmarketcap = Market()

res = coinmarketcap.ticker('golem-network-tokens')
print res

res = coinmarketcap.ticker('Iconomi')
print res

res = coinmarketcap.ticker('SingularDTV')
print res
