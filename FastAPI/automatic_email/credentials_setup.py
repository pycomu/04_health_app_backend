#%%
import keyring

#save credentials
def save_cred():
    service_name=input('Enter Service name:')
    username=input('Enter username:')
    password=input('Enter Password:')
    
    #keyring.set_password(service_name,'username',username)
    keyring.set_password(service_name,username,password)
    print('credentials saved succesfully!')
    
save_cred()
#%%

def get_cred(service_name):
    #username=keyring.get_password(service_name,'username')
    password=keyring.get_password(service_name,"healthappbmi@gmail.com")
    return password
get_cred("Automaticemail")
#%%

# %%
