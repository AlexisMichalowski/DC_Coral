####################################
#
# Downloading the full dataset 
#
##################################

if (!require(RSQLite)) install.packages(RSQLite)

library(RSQLite)

filename <- "Global_Coral_Bleaching_Database_SQLite_11_24_21.db"
sqlite.driver <- dbDriver("SQLite")
db <- dbConnect(sqlite.driver,
                dbname = filename)

#Some operations
dbListTables(db)

#data to predict (chose one, maybe the % seems interesting)
Bleaching_Level <- dbReadTable(db,"Bleaching_tbl")

Environmental <- dbReadTable(db,"Environmental_tbl")

Site_Info <- dbReadTable(db,"Site_Info_tbl")

Sample_Event <- dbReadTable(db,"Sample_Event_tbl")

Cover <- dbReadTable(db,"Cover_tbl")

to_remove=c()
#Suppress Enivronemental ID ID and REEF ID ect (all dbd related data)
to_remove=c(to_remove,"Environmental_ID","Site_Name","Reef_ID","Data_Source","Realm_Name")
#Suppres Date related field
to_remove=c(to_remove,"Date_Month","Date_Year","Date_Day")
#Suppress comment related field
to_remove=c(to_remove,"Comments.x","Comments.y")
#Suppress TRIAL shit as nothing seems to be said about it
to_remove=c(to_remove,"TRIAL501","TRIAL534","TRIAL528")
#Suppress column who bring localisaion data who brings a biais (maybe not lmao)
to_remove=c(to_remove,"Ocean_Name","Country_Name","City_Town_Name_2","Latitude_Degrees",
            "State_Island_Province_Name","City_Town_Name_3","Longitude_Degrees","Ecoregion_Name",
            "City_Town_Name","City_Town_Name_4"
)

Bleaching_Level<-Bleaching_Level[!is.na(Bleaching_Level$Percent_Bleached),c("Sample_ID","Percent_Bleached")]
Env_Sam=merge(Environmental,Sample_Event,by="Sample_ID")
Env_Sam_Sit=merge(Env_Sam,Site_Info,by="Site_ID")
Env_Sam_Sit_Cover=merge(Env_Sam_Sit,Cover,by="Sample_ID")
data=merge(Env_Sam_Sit,Bleaching_Level,by="Sample_ID")

df <- data[, -which(colnames(data) %in% to_remove)]
write.csv(df,"data_camp.csv")