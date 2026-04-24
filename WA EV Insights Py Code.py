# Importing relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

# Loading data
raw_data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# Reviewing data
raw_data.info()
raw_data.head(3)
raw_data.describe().transpose()

# Creating new data frame to avoid altering original dataset
data = raw_data.copy()


# =========================================================
# 1) DATA QUALITY & PREPROCESSING
# =========================================================

# Renaming new dataset columns
data.columns = ['VIN', 'County', 'City', 'State', 'Postal_Code', 'Model_Year', 'Make', 'Model', \
                'EV_Type', 'CAFV_Elig', 'Electric_Range', 'Base_MSRP', 'Legislative_District', \
                'DOL_Vehicle_ID', 'Vehicle_Location', 'Electric_Utility', '2020_Census_Tract']
data.head(3)

# Missing values
data.isna().sum().sort_values(ascending=False)

# Duplicates
data.duplicated().sum()

# Standardize categorical fields
data['Make'] = data['Make'].str.upper().str.strip()
data['City'] = data['City'].str.title().str.strip()

# Convert types
data['Model_Year'] = pd.to_numeric(data['Model_Year'], errors='coerce')
data['Electric_Range'] = pd.to_numeric(data['Electric_Range'], errors='coerce')
data['Base_MSRP'] = pd.to_numeric(data['Base_MSRP'], errors='coerce')

# Extract lat/long from Vehicle_Location
data[['Latitude','Longitude']] = data['Vehicle_Location'].str.extract(r'\((.*), (.*)\)').astype(float)


# =========================================================
# 2) CORE ANALYTICAL AXES
# =========================================================
# *********************************************************
# A. EV ADOPTION OVER TIME
# *********************************************************

ev_by_year = data.groupby('Model_Year').size()

plt.figure()
ev_by_year.plot()
plt.title('EV Adoption Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')

# *********************************************************
# B. MARKET SHARE BY MANUFACTURER
# *********************************************************

make_counts = data['Make'].value_counts().head(10)

plt.figure()
make_counts.plot(kind='bar')
plt.title('Top 10 EV Manufacturers')

# We think Tesla could be dominant in the market and proceed with a quick check
PercentTesla = (data['Make'] == 'TESLA').mean() * 100

# *********************************************************
# C. GEOGRAPHIC DISTRIBUTION
# *********************************************************

top_cities = data['City'].value_counts().head(10)

plt.figure()
top_cities.plot(kind='bar')
plt.title('Top Cities by EV Count')

# State density
state_counts = data.groupby('State').size()

# *********************************************************
# D. EV TYPE MIX (BEV VS PHEV)
# *********************************************************

# Understanding range anxiety vs adoption maturity
ev_type_dist = data['EV_Type'].value_counts(normalize=True) * 100

plt.figure()
ev_type_dist.plot(kind='bar')
plt.title('EV Type Distribution (%)')

# *********************************************************
# E. ELECTRIC RANGE ANALYSIS
# *********************************************************

plt.figure()
data['Electric_Range'].dropna().hist(bins=30)
plt.title('Distribution of Electric Range')

# Segment by make (reveals technology leadership)
data.groupby('Make')['Electric_Range'].mean().sort_values(ascending=False).head(10)

# *********************************************************
# F. PRICE VS RANGE
# *********************************************************

# Product positioning analysis
plt.figure()
plt.scatter(data['Base_MSRP'], data['Electric_Range'])
plt.xlabel('Price')
plt.ylabel('Range')
plt.title('Price vs Electric Range')


# =========================================================
# 3) ADVANCED INSIGHTS
# =========================================================
# *********************************************************
# A. COHORT ANALYSIS (EV GROWTH BY MANUFACTURER OVER TIME)
# *********************************************************

# Competitive dynamics
make_year = data.groupby(['Model_Year','Make']).size().unstack().fillna(0)

make_year[['TESLA','NISSAN','CHEVROLET']].plot()

# *********************************************************
# B. CAFV ELIGIBILITY ANALYSIS
# *********************************************************

# Policy impact (policy vs technology alignment)
data['CAFV_Elig'].value_counts(normalize=True)
data.groupby('CAFV_Elig')['Electric_Range'].mean()

# *********************************************************
# C. CLUSTERING
# *********************************************************

from sklearn.cluster import KMeans

df_cluster = data[['Electric_Range','Base_MSRP']].dropna()

kmeans = KMeans(n_clusters=3, random_state=0)
df_cluster['Cluster'] = kmeans.fit_predict(df_cluster)

plt.figure()
plt.scatter(df_cluster['Base_MSRP'], df_cluster['Electric_Range'], c=df_cluster['Cluster'])



