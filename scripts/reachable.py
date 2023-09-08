import csv
import requests
import os
import time

os.system('clear')

# copy and paste this in the header of each script
print()
print("        ********************************************************************\n"
      "        **                                                                **\n"      
      "        **            W E L C O M E  TO  J O E T I L I T I E S!           **\n"
      "        **                                                                **\n"
      "        **             This Joetility is the Website Reacher!             **\n"
      "        **                                                                **\n"
      "        ********************************************************************\n")
print()
# since you're forgetful, add this note to each script tellling what it does bruh
print("        ******                --> USAGE  NOTE <--                     ******\n"
      "        * This Joetility will do a website check from sites.csv and return *\n"
      "        * a code and status for each website in the csv PLUS... afterwards *\n"
      "        * you'll be asked if you want to add a website site to the list!!  *\n")

time.sleep(3)

CSV_FILENAME = "/Users/joehome/Documents/GitHub/joetilities/csv/sites.csv"


# get the sites
def load_websites_from_csv():
    if not os.path.exists(CSV_FILENAME):
        return []
    
    websites = []
    with open(CSV_FILENAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            websites.append(row[0])
    return websites

# add site to csv
def save_website_to_csv(website):
    with open(CSV_FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website])

# check the sites from the csv
def check_website_status(website):
    try:
        response = requests.head(website, timeout=5)
        status_code = response.status_code
        
        # english status based on returned code
        if 100 <= status_code < 200:
            print()
            return "Infm. Error (100-199)"
        elif 200 <= status_code < 300:
            print()
            return "Success!! (200-299)"
        elif 300 <= status_code < 400:
            print()
            return "Success-ish!! (300-399)"
        elif 400 <= status_code < 500:
            print()
            return "Client Error (400-499)"
        elif 500 <= status_code < 600:
            print()
            return "Server Error (500-599)"
        else:
            print()
            return status_code 
    except requests.ConnectionError:
        if website.startswith('http://'):
            # retry with https
            try:
                https_website = website.replace('http://', 'https://', 1)
                response = requests.head(https_website, timeout=5)
                status_code = response.status_code
                # english status based on returned code
                if 100 <= status_code < 200:
                    print()
                    return "Infm. Error (100-199)"
                elif 200 <= status_code < 300:
                    print()
                    return "Success!! (200-299)"
                elif 300 <= status_code < 400:
                    print()
                    return "Success-ish!! (300-399)"
                elif 400 <= status_code < 500:
                    print()
                    return "Client Error (400-499)"
                elif 500 <= status_code < 600:
                    print()
                    return "Server Error (500-599)"
                else:
                    print()
                    return status_code                             
            except requests.ConnectionError:
                return f"Connection Error (also failed with https)"
            except requests.Timeout:
                return "Timeout (https)"
            except requests.RequestException as e:
                return f"Error with https: {str(e)}"
        return "Connection Error"
    except requests.Timeout:
        return "Timeout"
    except requests.RequestException as e:
        return str(e)


def main():
    websites = load_websites_from_csv()
    print("Loading from sites.csv...")
    time.sleep(2)
    print("Checking your sites...\n")
    for website in websites:
        status = check_website_status(website)
        print(f"  ---> {website} - {status}")
        
    choice = input("\nWould you like to add a new website to the list? (y/n) ").lower()
    if choice == 'y':
        new_website = input("\nEnter the new site to be added including\n"
                            "the preferred prefix (http:// or https://) :")
        save_website_to_csv(new_website)
        print()
        print(f"{new_website} added to the to the file!\n")
    else:
        time.sleep(1)
        print()
        print("        ******             ----> Later Gator! <----                  ******\n")
        time.sleep(1)


# run it brah
if __name__ == "__main__":
    main()
