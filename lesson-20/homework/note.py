# Homework 1:
# Using chinook.db write pandas code.

# 1 Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.
import pandas as pd
import sqlite3

# Connect to the database file
conn = sqlite3.connect("C:\\Users\\user\\Downloads\\chinook.db")

# Create a cursor to run SQL queries
cursor = conn.cursor()

# Test: show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)


df = pd.read_sql("SELECT * FROM invoices", conn)
print(df)
conn.close()

filt = df.groupby('CustomerId')['Total'].sum().reset_index()
print(filt)

customer_spend = filt.merge(df, on='CustomerId')
print(customer_spend)

filt1 = customer_spend.sort_values(by='Total_x', ascending=False).head(5)
print(filt1)

print(filt1[['CustomerId', 'Total_x']])

# 2 Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
# A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
conn = sqlite3.connect("C:\\Users\\user\\Downloads\\chinook.db")
df2 = pd.read_sql('SELECT * FROM invoices', conn)
df3 = pd.read_sql('SELECT * FROM tracks', conn)
df6 = pd.read_sql('SELECT * FROM invoice_items', conn)
merged = df2.merge(df6, on='InvoiceId')
merged2 = merged.merge(df3, on='TrackId')
print(merged2)
filte = merged2.groupby(['TrackId', 'AlbumId'])['TrackId'].nunique().reset_index()
print(filte)

album_track_counts = df3.groupby('AlbumId')['TrackId'].nunique().reset_index()
album_track_counts.rename(columns={'TrackId':'TotalTracks'}, inplace=True)
customer_album_stats = filte.merge(album_track_counts, on='AlbumId')
customer_album_stats['FullAlbum'] = customer_album_stats['TracksPurchased'] == customer_album_stats['TotalTracks']
def preference(group):
    if all(group['FullAlbum']):
        return 'Full Album'
    else:
        return 'Individual Tracks'

customer_pref = customer_album_stats.groupby('CustomerId').apply(preference).reset_index()
customer_pref.rename(columns={0:'Preference'}, inplace=True)
summary = customer_pref['Preference'].value_counts(normalize=True) * 100
summary_df = summary.reset_index()
summary_df.columns = ['Preference', 'Percentage']

print(summary_df)
