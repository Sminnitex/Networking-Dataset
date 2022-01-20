import setup_path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import requests as r
import io
import zipfile as zip
import admin
import link
import os
import pathlib
from os import listdir
from os.path import isfile, join
import string as s

#First, let's check if our folder is in it's place
data_path=os.path.abspath("Drone_RCS_Measurement_Dataset")
if os.path.exists(data_path)==False:

        #We need to have admin priviliges
        if not admin.RunAsAdmin(admin.file_path):
                admin.RunAsAdmin('cmd.exe','arg1','arg2')

        #connecting to our url and checking the connection
        zip_url=link.getZipLink("https://ieee-dataport.org/saml_login?destination=/open-access/drone-rcs-measurements-26-40-ghz") 
        con=r.get(zip_url)
        print("Response error: " + str(con.raise_for_status()))

        #now let's download and extract the zip on our path
        directory_path=pathlib.Path().resolve()
        z=zip.ZipFile(io.BytesIO(con.content))
        z.extractall(directory_path)

#let's add our files to a list and read it
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

#now let's create some lists we will need
meanf=[]
stdf=[]
minimf=[]
maximf=[]
medf=[]
meant=[]
stdt=[]
minimt=[]
maximt=[]
medt=[]
meanp=[]
stdp=[]
minimp=[]
maximp=[]
medp=[]
meanr=[]
stdr=[]
minimr=[]
maximr=[]
medr=[]

#in our dataset we have 4 colums, f[GHz], theta[deg], phi[deg], RCS[dB]
#let's clean up our data:
#the only important thing for theta[deg], phi[deg], and RCS[dB], is that the value hasn't to be null
#while for f[GHz] the value also has to be between 26GHz and 40 GHz
#but we can also change angles from deg to rad
#so let's drop nulls, duplicates, invalid frequency values, and change angles misure unit to clean our data
n=0
while n<len(onlyfiles):
        print("file: " + str(onlyfiles[n]))
        df=pd.read_csv(data_path  +"/"+ onlyfiles[n])

        not_null=df.dropna()
        not_duplicate=not_null.drop_duplicates()
        clean=not_duplicate.drop(not_duplicate[(not_duplicate["f[GHz]"]<26) | (not_duplicate["f[GHz]"]>40)].index)

        #Now that we have cleaned our data we want to transfer our data to another file to analyze it
        meanf.append(clean["f[GHz]"].mean())
        meant.append(clean["theta[deg]"].mean())
        meanp.append(clean["phi[deg]"].mean())
        meanr.append(clean["RCS[dB]"].mean())
        stdf.append(clean["f[GHz]"].std())
        stdt.append(clean["theta[deg]"].std())
        stdp.append(clean["phi[deg]"].std())
        stdr.append(clean["RCS[dB]"].std())
        minimf.append(clean["f[GHz]"].min())
        minimt.append(clean["theta[deg]"].min())
        minimp.append(clean["phi[deg]"].min())
        minimr.append(clean["RCS[dB]"].min())
        maximf.append(clean["f[GHz]"].max())
        maximt.append(clean["theta[deg]"].max())
        maximp.append(clean["phi[deg]"].max())
        maximr.append(clean["RCS[dB]"].max())
        medf.append(clean["f[GHz]"].median())
        medt.append(clean["theta[deg]"].median())
        medp.append(clean["phi[deg]"].median())
        medr.append(clean["RCS[dB]"].median())
        n+=1

#Now that our cleaned files are ready, we can analyze them to obtain our graphs
no_csv=[s.replace(".csv", "") for s in onlyfiles]

fig, ax = plot.subplots(2,2, figsize=(10, 8), sharex=True)
fig.suptitle("Mean")
ax[0][0].plot(range(1, 18), meanf)
ax[0][1].plot(range(1, 18), meant)
ax[1][0].plot(range(1, 18), meanp)
ax[1][1].plot(range(1, 18), meanr)
ax[0][0].set_ylabel("Frequency [GHz]")
ax[1][0].set_ylabel("Theta [deg]")
ax[0][1].set_ylabel("Phi [deg]")
ax[1][1].set_ylabel("RCS [dB]")
for i in range(2):
        for j in range(2):
                axs=ax[i][j]
                axs.set_xticklabels(no_csv, rotation=90)
plot.subplots_adjust(hspace=0.25)
plot.xticks(np.arange(1, 18, 1))

fig2, ax2 = plot.subplots(2,2, figsize=(10, 8), sharex=True)
fig2.suptitle("Standard deviation")
ax2[0][0].plot(range(1, 18), stdf)
ax2[0][1].plot(range(1, 18), stdt)
ax2[1][0].plot(range(1, 18), stdp)
ax2[1][1].plot(range(1, 18), stdr)
ax2[0][0].set_ylabel("Frequency [GHz]")
ax2[1][0].set_ylabel("Theta [deg]")
ax2[0][1].set_ylabel("Phi [deg]")
ax2[1][1].set_ylabel("RCS [dB]")
for i in range(2):
        for j in range(2):
                axs=ax2[i][j]
                axs.set_xticklabels(no_csv, rotation=90)
plot.subplots_adjust(hspace=0.25)
plot.xticks(np.arange(1, 18, 1))

fig3, ax3 = plot.subplots(2,2, figsize=(10, 8), sharex=True)
fig3.suptitle("Minimum")
ax3[0][0].plot(range(1, 18), minimf)
ax3[0][1].plot(range(1, 18), minimt)
ax3[1][0].plot(range(1, 18), minimp)
ax3[1][1].plot(range(1, 18), minimr)
ax3[0][0].set_ylabel("Frequency [GHz]")
ax3[1][0].set_ylabel("Theta [deg]")
ax3[0][1].set_ylabel("Phi [deg]")
ax3[1][1].set_ylabel("RCS [dB]")
for i in range(2):
        for j in range(2):
                axs=ax3[i][j]
                axs.set_xticklabels(no_csv, rotation=90)
plot.subplots_adjust(hspace=0.25)
plot.xticks(np.arange(1, 18, 1))

fig4, ax4 = plot.subplots(2,2, figsize=(10, 8), sharex=True)
fig4.suptitle("Max")
ax4[0][0].plot(range(1, 18), maximf)
ax4[0][1].plot(range(1, 18), maximt)
ax4[1][0].plot(range(1, 18), maximp)
ax4[1][1].plot(range(1, 18), maximr)
ax4[0][0].set_ylabel("Frequency [GHz]")
ax4[1][0].set_ylabel("Theta [deg]")
ax4[0][1].set_ylabel("Phi [deg]")
ax4[1][1].set_ylabel("RCS [dB]")
for i in range(2):
        for j in range(2):
                axs=ax4[i][j]
                axs.set_xticklabels(no_csv, rotation=90)
plot.subplots_adjust(hspace=0.25)
plot.xticks(np.arange(1, 18, 1))

fig5, ax5 = plot.subplots(2,2, figsize=(10, 8), sharex=True)
fig5.suptitle("Median")
ax5[0][0].plot(range(1, 18), medf)
ax5[0][1].plot(range(1, 18), medt)
ax5[1][0].plot(range(1, 18), medp)
ax5[1][1].plot(range(1, 18), medr)
ax5[0][0].set_ylabel("Frequency [GHz]")
ax5[1][0].set_ylabel("Theta [deg]")
ax5[0][1].set_ylabel("Phi [deg]")
ax5[1][1].set_ylabel("RCS [dB]")
for i in range(2):
        for j in range(2):
                axs=ax5[i][j]
                axs.set_xticklabels(no_csv, rotation=90)
plot.subplots_adjust(hspace=0.25)
plot.xticks(np.arange(1, 18, 1))
plot.show()