import matplotlib.pyplot as plt

# Data from table (Nürnberg, Station 10763)
months = [
    "202309", "202310", "202311", "202312", "202401", "202402", "202403", "202404",
    "202405", "202406", "202407", "202408", "202409", "202410", "202411", "202412",
    "202501", "202502"
]
tmm = [17.5, 12.2, 5.9, 4.1, 1.6, 7.3, 8.1, 10.6, 15.4, 18.4, 20.1, 21.2, 15.9, 11.3, 5.0, 1.9, 2.1, 1.2]  # Mittlere Temperatur
sos = [266.4, 129.5, 47.1, 40.6, 79.7, 52.1, 138.2, 171.0, 193.3, 211.7, 253.8, 284.9, 168.8, 78.8, 52.3, 36.7, 92.9, 93.8]  # Sonnenstunden
nmm = [4.0, 6.7, 7.1, 7.2, 6.3, 7.4, None, 6.7, 6.0, 5.8, 5.4, 4.8, 5.5, 7.1, 6.9, 6.9, 6.3, 5.7]  # Regenstunden (None für März 2023)
rss = [10.4, 44.7, 89.6, 57.0, 55.6, 49.2, 31.0, 40.2, 117.1, 53.7, 43.3, 74.3, 93.6, 56.8, 38.1, 37.9, 48.5, 38.8]  # Niederschlag

# Label month, e.g. "09/2024"
labels = [m[4:] + "/" + m[:4] for m in months]

# Replace missing values with 0
nmm = [0 if x is None else x for x in nmm]

# Plot Setup
fig, ax1 = plt.subplots(figsize=(16,7)) # Bigger overview

#Right Axis: Sun hours and rain
ax2 = ax1.twinx()
ax2.bar(labels, sos, color='gold', alpha=0.6, zorder=1, label='Sun hours (h)')
ax2.fill_between(labels, 0, rss, color='blue', alpha=0.3, zorder=2, label='Rainfall (mm)')
ax2.set_ylabel('Sun hours (h)/ Rainfall (mm)', color='k')
ax2.tick_params(axis='y', labelcolor='k')

# Left Axis: Temperature and Rain hours
ax1.plot(labels, tmm, 'r-', marker='o', alpha=1.0, zorder=3, label='Middle Temperature (C°)')
ax1.plot(labels, nmm, 'b--',  marker='s', zorder=4, label='Rain Days (d)')
ax1.set_xlabel('Month/Year')
ax1.set_ylabel('Middle Temperature (C°)/ Rain Days (d)', color='k')
ax1.tick_params(axis='y', labelcolor='k') # Löschen?
ax1.grid(True, linestyle='--', zorder=0)

#Title and Styling
plt.title('Weather Nürnberg since 09/2023, temperature, rain days, sun hours, rainfall', fontsize=14)
plt.xticks(rotation=45)
fig.legend(loc='upper center', bbox_to_anchor=(0.3, 0.95), ncol=4)
plt.tight_layout()

#Highlights
max_tmm_idx =  tmm.index(max(tmm))
ax1.annotate(f'Max Temp: {tmm[max_tmm_idx]}C°',
             xy=(max_tmm_idx, tmm[max_tmm_idx]),
             xytext=(max_tmm_idx+1, tmm[max_tmm_idx]+0.5),
             arrowprops=dict(facecolor='black'))

max_sos_idx = sos.index(max(sos))
ax2.annotate(f'Max Sun Hours: {sos[max_sos_idx]}h',
             xy=[max_sos_idx, sos[max_sos_idx]],
             xytext=(max_sos_idx-3, sos[max_sos_idx]-50),
             arrowprops=dict(facecolor='black'))

max_nmm_idx = nmm.index(max(nmm))
ax1.annotate(f'Max Rain Days: {nmm[max_nmm_idx]}h',
             xy=(max_nmm_idx, nmm[max_nmm_idx]),
             xytext=(max_nmm_idx+1, nmm[max_nmm_idx]+1),
             arrowprops=dict(facecolor='black'), zorder=7)

max_rss_idx = rss.index(max(rss))
ax2.annotate(f'Max Rainfall: {rss[max_rss_idx]}mm',
             xy=[max_rss_idx, rss[max_rss_idx]],
             xytext=(max_rss_idx-3, rss[max_rss_idx-15]),
             arrowprops=dict(facecolor='black'))

plt.show()