import subprocess
import json


#Variaveis
err_list = []

#ADD THIS CODE TO THE MAIN LOOP
wifi = subprocess.run(["netsh", "wlan", "show", "profile"], shell=True, check=True, capture_output=True)
wifis = str(wifi)
cont = wifis.count("    All User Profile     ")
ac1 = wifis.replace("\\r","").replace("\\n","")
ac2 = ac1.replace("CompletedProcess(args=['netsh', 'wlan', 'show', 'profile'], returncode=0, stdout=b'Profiles on interface Wi-Fi:","",1).replace("Group policy profiles (read only)---------------------------------    <None>User profiles-------------","",1).replace("', stderr=b'')","",-1)

#"Users" will be a important variable 
Users = ac2.split("    All User Profile     : ")
Users.pop(0)




dic_wifi = {
    "Profile information" :{
        "Version" : "",
        "Type" : "",
        "Name" : "",
        "Connection mode" : "",
        "Network broadcast" : "",
        "AutoSwitch" : "",
        "MAC Randomization" : ""
    },
    "Connectivity settings" :{
        "Number of SSIDs" : "",
        "SSID name" : "",
        "Network type" : "",
        "Radio type" : "",
    },
    "Security settings" :{
        "Authentication" : "",
        "Cipher" : "",
        "Authentication" : "",
        "Cipher" : "",
        "Security key" : "",
        "Key Content" : ""
    },
    "Cost settings" :{
        "Cost":"",
        "Congested" : "",
        "Approaching Data Limit" : "",
        "Over Data Limit" : "",
        "Roaming" : "",
        "Cost Source" : ""
    }
}
dic_open = {
    "Profile information" :{
        "Version" : "",
        "Type" : "",
        "Name" : "",
        "Connection mode" : "",
        "Network broadcast" : "",
        "AutoSwitch" : "",
        "MAC Randomization" : ""
    },
    "Connectivity settings" :{
        "Number of SSIDs" : "",
        "SSID name" : "",
        "Network type" : "",
        "Radio type" : "",
        "Vendor extension" : ""
    },
    "Security settings" :{
        "Authentication" : "",
        "Cipher" : "",
        "Key Index" : ""
    },
    "Cost settings" :{
        "Cost":"",
        "Congested" : "",
        "Approaching Data Limit" : "",
        "Over Data Limit" : "",
        "Roaming" : "",
        "Cost Source" : ""
    }
}


#FUNCTIONS
##


#funcao para guardar "Wifis.json" os dicts
def store(dct): #store .json
    jsons = json.dumps(dct, indent = 4)
    f = open("Wifis.json","a")
    f.write(jsons)
    f.close()




#Function to transform the data(list whit info) in a dict
def dict_func(lista, dict):
    #lista = lista whit usefull info
    #dict = to use one type of dict (one to open wifis and one to personal wifis)

    #Comun to open wifis and personal wifis
    dict["Profile information"]["Version"] = lista[0]
    dict["Profile information"]["Type"] = lista[1]
    dict["Profile information"]["Name"] = lista[2]
    dict["Profile information"]["Connection mode"] = lista[3]
    dict["Profile information"]["Network broadcast"] = lista[4]
    dict["Profile information"]["AutoSwitch"] = lista[5]
    dict["Profile information"]["MAC Randomization"] = lista[6]
    dict["Connectivity settings"]["Number of SSIDs"] = lista[7]
    dict["Connectivity settings"]["SSID name"] = lista[8]
    dict["Connectivity settings"]["Networktype"] = lista[9]
    dict["Connectivity settings"]["Radio type"] = lista[10]
    dict["Connectivity settings"]["Vendor extension"] = lista[11]
    
    
    try:
    ## to home and personal wifis
        dict["Security settings"]["Authentication"] = lista[12]
        dict["Security settings"]["Cipher"] = lista[13]
        dict["Security settings"]["Authentication"] = lista[14]
        dict["Security settings"]["Cipher"] = lista[15]
        dict["Security settings"]["Security key"] = lista[16]
        dict["Security settings"]["Key Content"] = lista[17]
        dict["Cost settings"]["Cost"] = lista[18]
        dict["Cost settings"]["Congested"] = lista[19]
        dict["Cost settings"]["Approaching Data Limit"] = lista[20]
        dict["Cost settings"]["Over Data Limit"] = lista[21]
        dict["Cost settings"]["Roaming"] = lista[22]
        dict["Cost settings"]["Cost Source"] = lista[23]
    
    except IndexError as identifier:
     ##this exeptions will happen when the wifi dosent need password
        dict["Security settings"]["Authentication"] = lista[12]
        dict["Security settings"]["Cipher"] = lista[13]
        dict["Security settings"]["Key Index"] = lista[14]
        dict["Cost settings"]["Cost"] = lista[15]
        dict["Cost settings"]["Congested"] = lista[16]
        dict["Cost settings"]["Approaching Data Limit"] = lista[17]
        dict["Cost settings"]["Over Data Limit"] = lista[18]
        dict["Cost settings"]["Roaming"] = lista[19]
        dict["Cost settings"]["Cost Source"] = lista[20]



'''
def err_func():
    global reveal
    for x in range(len(err_list)):
        local = err_list[x] #LOCAL e o qie e aficionado a lista
        entry = 'name={}'.format(local)
        reveal = subprocess.run(['netsh','wlan','show','profile', entry,'key=clear'], shell=True, capture_output=True)
        
        
        #Remove useless information
        sclean = str(reveal)
        cleann = sclean.replace("\\r\\n\\r\\n","  ").replace("\\r","").replace("\\n","").replace(insert,"")
        text_to_delet = "CompletedProcess(args=['netsh', 'wlan', 'show', 'profile', 'name={wifi_err}', 'key=clear'], returncode=0, stdout=b'Profile {wifi_err} on interface Wi-Fi: =======================================================================   Applied: All User Profile      Profile information -------------------     Version                : ".format(wifi_err=local)
        cleann2 = cleann.replace(text_to_delet, "",1).replace("', stderr=b'')","",-1)
        cleann4 = cleann2.replace("Applied: All User Profile","").replace("=======================================================================","")
        cleann3 = cleann2.replace("    Type                   :","",1).replace("    Name                   :","",1).replace("    Control options        :         Connection mode    :","",1).replace("        Network broadcast  :","",1).replace("        AutoSwitch         :","",1).replace("        MAC Randomization  :","",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :","",1).replace("    SSID name              :","",1).replace("    Network type           :","",1).replace("    Radio type             :","",1).replace("    Vendor extension          :","",1).replace("  Security settings -----------------     Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Security key           :","",1).replace("    Key Content            :","",1).replace("  Cost settings -------------     Cost                   :","",1).replace("    Congested              :","",1).replace("    Approaching Data Limit :","",1).replace("    Over Data Limit        :","",1).replace("    Roaming                :","",1).replace("    Cost Source            :","",1)
        cleann1 = cleann2.replace("    Type                   :",".",1).replace("    Name                   :",".",1).replace("    Control options        :         Connection mode    :",".",1).replace("        Network broadcast  :",".",1).replace("        AutoSwitch         :",".",1).replace("        MAC Randomization  :",".",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :",".",1).replace("    SSID name              :",".",1).replace("    Network type           :",".",1).replace("    Radio type             :",".",1).replace("    Vendor extension          :",".",1).replace("  Security settings -----------------     Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Security key           :",".",1).replace("    Key Content            :",".",1).replace("  Cost settings -------------     Cost                   :",".",1).replace("    Congested              :",".",1).replace("    Approaching Data Limit :",".",1).replace("    Over Data Limit        :",".",1).replace("    Roaming                :",".",1).replace("    Cost Source            :",".",1)
        
        #Store data
        lista_err = cleann1.split(". ") #list whit useful information
        dict_func(lista_err, dic_open)   #store data 
        store(dic_open)
'''







##RUNNED CODE
#
for x in range(len(Users)):
    #define global variables
    global revealer
    global lista
    global dict_wifi
    wifiname = (Users[x])
    
    try:
        #scrape the info
        insert = 'name="{}"'.format(wifiname)
        reveal = subprocess.run(['netsh','wlan','show','profile', insert,'key=clear'], shell=True, check=True, capture_output=True)
    
    except subprocess.CalledProcessError:
        #this exeption happen to open wifis
        ##CHANGE THE ERR_LIST FUNCTiON AND ADD IT TO THE LOOP
        #err_list.append(wifiname)
        #wifiname = local
        
        entry = f'name={wifiname}'
        reveal = subprocess.run(['netsh','wlan','show','profile', entry,'key=clear'], shell=True, capture_output=True)
        
        
        #Remove useless information
        sclean = str(reveal)
        cleann = sclean.replace("\\r\\n\\r\\n","  ").replace("\\r","").replace("\\n","").replace(insert,"")
        text_to_delet = f"CompletedProcess(args=['netsh', 'wlan', 'show', 'profile', 'name={wifiname}', 'key=clear'], returncode=0, stdout=b'Profile {wifiname} on interface Wi-Fi: =======================================================================   Applied: All User Profile      Profile information -------------------     Version                : "
        cleann2 = cleann.replace(text_to_delet, "",1).replace("', stderr=b'')","",-1)
        cleann4 = cleann2.replace("Applied: All User Profile","").replace("=======================================================================","")
        cleann3 = cleann2.replace("    Type                   :","",1).replace("    Name                   :","",1).replace("    Control options        :         Connection mode    :","",1).replace("        Network broadcast  :","",1).replace("        AutoSwitch         :","",1).replace("        MAC Randomization  :","",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :","",1).replace("    SSID name              :","",1).replace("    Network type           :","",1).replace("    Radio type             :","",1).replace("    Vendor extension          :","",1).replace("  Security settings -----------------     Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Security key           :","",1).replace("    Key Content            :","",1).replace("  Cost settings -------------     Cost                   :","",1).replace("    Congested              :","",1).replace("    Approaching Data Limit :","",1).replace("    Over Data Limit        :","",1).replace("    Roaming                :","",1).replace("    Cost Source            :","",1)
        cleann1 = cleann2.replace("    Type                   :",".",1).replace("    Name                   :",".",1).replace("    Control options        :         Connection mode    :",".",1).replace("        Network broadcast  :",".",1).replace("        AutoSwitch         :",".",1).replace("        MAC Randomization  :",".",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :",".",1).replace("    SSID name              :",".",1).replace("    Network type           :",".",1).replace("    Radio type             :",".",1).replace("    Vendor extension          :",".",1).replace("  Security settings -----------------     Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Security key           :",".",1).replace("    Key Content            :",".",1).replace("  Cost settings -------------     Cost                   :",".",1).replace("    Congested              :",".",1).replace("    Approaching Data Limit :",".",1).replace("    Over Data Limit        :",".",1).replace("    Roaming                :",".",1).replace("    Cost Source            :",".",1)
        
        #Store data
        lista_err = cleann1.split(". ") #list whit useful information
        dict_func(lista_err, dic_open)   #store data 
        store(dic_open)
        



    else:  #To personal wifis
        
        sclean = str(reveal)
        cleann = sclean.replace("\\r\\n\\r\\n","  ").replace("\\r","").replace("\\n","").replace(insert,"")
        
        #Clean data
        text_to_delet = "CompletedProcess(args=['netsh', 'wlan', 'show', 'profile', '', 'key=clear'], returncode=0, stdout=b'Profile {} on interface Wi-Fi: =======================================================================   Applied: All User Profile      Profile information -------------------     Version                : ".format(wifiname)
        cleann2 = cleann.replace(text_to_delet, "'",1).replace("', stderr=b'')","",-1)
        cleann3 = cleann2.replace("    Type                   :","",1).replace("    Name                   :","",1).replace("    Control options        :         Connection mode    :","",1).replace("        Network broadcast  :","",1).replace("        AutoSwitch         :","",1).replace("        MAC Randomization  :","",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :","",1).replace("    SSID name              :","",1).replace("    Network type           :","",1).replace("    Radio type             :","",1).replace("    Vendor extension          :","",1).replace("  Security settings -----------------     Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Authentication         :","",1).replace("    Cipher                 :","",1).replace("    Security key           :","",1).replace("    Key Content            :","",1).replace("  Cost settings -------------     Cost                   :","",1).replace("    Congested              :","",1).replace("    Approaching Data Limit :","",1).replace("    Over Data Limit        :","",1).replace("    Roaming                :","",1).replace("    Cost Source            :","",1)
        cleann1 = cleann2.replace("    Type                   :",".",1).replace("    Name                   :",".",1).replace("    Control options        :         Connection mode    :",".",1).replace("        Network broadcast  :",".",1).replace("        AutoSwitch         :",".",1).replace("        MAC Randomization  :",".",1).replace("  Connectivity settings ---------------------     Number of SSIDs        :",".",1).replace("    SSID name              :",".",1).replace("    Network type           :",".",1).replace("    Radio type             :",".",1).replace("    Vendor extension          :",".",1).replace("  Security settings -----------------     Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Authentication         :",".",1).replace("    Cipher                 :",".",1).replace("    Security key           :",".",1).replace("    Key Content            :",".",1).replace("  Cost settings -------------     Cost                   :",".",1).replace("    Congested              :",".",1).replace("    Approaching Data Limit :",".",1).replace("    Over Data Limit        :",".",1).replace("    Roaming                :",".",1).replace("    Cost Source            :",".",1)
        
        #store data
        lista = cleann1.split(". ") #create a list whit useful information
        dict_func(lista,dic_wifi) #change the list to the "dic_wifi"
        store(dic_wifi) #add to the file

#err_func()