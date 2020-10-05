import pyshorteners

def URL_shortener(url):
    
    s = pyshorteners.Shortener()
    shortened_url = s.osdb.short(url)
    print("Here's your shortened URL:")
    print(shortened_url)

choice = 'y'
while(choice == 'y' or choice == 'yes'):
    url = input("Enter the URL you want shortened: ")
    URL_shortener(url)
    choice = input("Do you want to continue shortening? (y/yes for yes, any other letter for no): ")
    