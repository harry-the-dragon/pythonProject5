import camelot
import pandas as pd

# harry = pd.read_html('https://en.wikipedia.org/wiki/University_of_Technology_Sydney')
# print (len(harry))
# print (harry)

# df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

# df_premier21.rename(columns={'FTHG' : 'home_goals', 'FTAG' : 'away_goals'}, inplace = True)


# print (df_premier21)


table = camelot.read_pdf('foo.pdf', pages='1', flavor='lattice' )
print (table)
