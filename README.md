# Folder description

**SelectingBeaches** contains codes and data sets for selecting beaches

**SelectingHotels** contains codes and data sets for selecting hotels within a specified distance for each beach selected from the *SelectingBeaches* folder

**finalHotelSample** contains the final sample of hotels based on 225 beaches from the *SlectingBeaches* folder and the hotels from the *SelectingHotels* folder


* 1. In the first stage, all hotels located within 30 miles of the nearest UK beach were sampled using UK Beach Pollution Data from Yong and Hotel Census Data from STR. The constructed sample at this stage includes the necessary information about the beach with which each hotel has been paired as well as the calculated distance from the beach. (Codes in the **SelectingHotels** folder)

* 2. In the second stage, 225 beaches in England (out of 1803 beaches in the UK) that had at least 3 years of pre and 3 years of post-periods are sampled. (Codes in the **SelectingBeaches** folder)

* 3. In the third and final stage, only the hotels based on the hotel sample from the first stage that had been paired with one of the 225 beaches from the beach sample in the second stage have been kept. The final hotel sample includes 1017 hotels and 120 beaches. (Codes in the **finalHotelSample** folder). 
