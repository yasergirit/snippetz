# Outlier Detection
# This function helps to find outliers in a dataset

def find_outliers(data):
    global q_list
    q_list = []
    sorted_data = data.sort_values()
    
    for q, p in {"Q1": 25, "Q2": 50, "Q3": 75}.items():
        
        # Calculate Q1, Q2, Q3 and IQR.
        Q = np.percentile(sorted_data, p, interpolation = 'midpoint')
        q_list.append(Q)
        
        print("Checking...", q)
        time.sleep(2) 
        print("{}: {} percentile of the {} values is,".format(q,p,data.name), Q)
    
    global Q1, Q2, Q3
    
    Q1 = q_list[0]
    Q2 = q_list[1]
    Q3 = q_list[2]
    
    IQR = Q3 - Q1 
    print("Interquartile range is", IQR)
    
    # Find the lower and upper limits as Q1 – 1.5 IQR and Q3 + 1.5 IQR, respectively
    global low_lim, up_lim
    
    low_lim = Q1 - 1.5 * IQR
    up_lim = Q3 + 1.5 * IQR
    
    time.sleep(1)
    print(" ")
    print("Checking limits")
    time.sleep(2)
    print("low_limit is", low_lim)
    print("up_limit is", up_lim)
    
    
    time.sleep(1)
    # Find outliers in the dataset
    outliers =[]
    for x in sorted_data:
        if ((x> up_lim) or (x<low_lim)):
             outliers.append(x)
    print("\nOutliers are being added to list. Please wait!")
    time.sleep(3)
    print("\nOutliers in the dataset is", outliers)
