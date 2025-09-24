from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

options = webdriver.ChromeOptions()
options.add_argument("--incognito")       # fresh incognito window
options.add_argument("--disable-cache")   # no cache
options.add_argument("--disable-application-cache")
options.add_argument("--disk-cache-size=0")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/travel/flights")


sleep(random.uniform(1, 3))
destination = "Berlin"
search_box = driver.switch_to.active_element
search_box.send_keys(destination)
sleep(3)
first_suggestion = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "zsRT0d"))
    )
first_suggestion.click()
print("✅ Selected Berlin from suggestions")

try :
    where_from = driver.find_element(By.XPATH, '//input[@class="II2One j0Ppje zmMKJ LbIaRd"]')
    where_from.send_keys(Keys.CONTROL, "a")
    where_from.send_keys(Keys.DELETE)
 # extra clear
    
    
    where_from.send_keys('Casablanca')
    sleep(1)
    # Wait for the dropdown and click the first suggestion
    first_suggestion = driver.find_element(By.CLASS_NAME, 'zsRT0d') 
    first_suggestion.click()
    print("✅ Selected Casablanca from suggestions")

except Exception as ex :
    print('erorr ', ex)
sleep(random.uniform
      (1, 3))
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


    
try:
        # Attempt 2
        start_search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search"]'))
        )
        start_search.click()
        print("Second attempt succeeded!")
        
except (TimeoutException, ElementClickInterceptedException) as x:
        print('Second attempt fail because:', x)
        print('....................')
        
        try:
            # Attempt 3
            start_search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@role="button" and @jsname="LgbsSe"]'))
            )
            start_search.click()
            print("Third attempt succeeded!")
            
        except Exception as x:
            print('Third attempt fail because:', x)
            print('All search button attempts failed!')
sleep(random.uniform(2,4))
from selenium.webdriver.common.action_chains import ActionChains

departure_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Departure"]'))
)

driver.execute_script("arguments[0].click();", departure_input)
print("✅ Departure input opened with JS click")

#Date selection attempts
# ----------------------------
try:
    # Attempt 1: Exact aria-label
    target_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Thursday, September 30, 2025"]'))
    )
    driver.execute_script("arguments[0].click();", target_date)
    print("✅ Attempt 1 succeeded: clicked using exact aria-label")

except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e1:
    print("❌ Attempt 1 failed:", e1)
    print("....................")

    try:
        # Attempt 2: Match by jsname + text() = 25
        target_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@jsname="nEWxA" and text()="30"]'))
        )
        driver.execute_script("arguments[0].click();", target_date)
        print("✅ Attempt 2 succeeded: clicked using text()")

    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e2:
        print("❌ Attempt 2 failed:", e2)
        print("....................")

        try:
            # Attempt 3: Partial aria-label contains()
            target_date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@jsname="nEWxA" and contains(@aria-label, "September 30, 2025")]'))
            )
            driver.execute_script("arguments[0].click();", target_date)
            print("✅ Attempt 3 succeeded: clicked using contains()")

        except Exception as e3:
            print("❌ Attempt 3 failed:", e3)
            print("All attempts to select the date failed 🚨")

sleep(random.uniform(1,3))
return_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Return"]'))
)

driver.execute_script("arguments[0].click();", return_input)
print("✅ Return input opened with JS click")
sleep(random.uniform(2, 4))
#
try:
    # Attempt 1: Exact aria-label
    target_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Thursday, October 16, 2025"]'))
    )
    driver.execute_script("arguments[0].click();", target_date)
    print("✅ Attempt 1 succeeded: clicked using exact aria-label")

except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e1:
    print("❌ Attempt 1 failed:", e1)
    print("....................")

    try:
        # Attempt 2: Match by jsname + text() = 25
        target_date = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@jsname="nEWxA" and text()="25"]'))
        )
        driver.execute_script("arguments[0].click();", target_date)
        print("✅ Attempt 2 succeeded: clicked using text()")

    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e2:
        print("❌ Attempt 2 failed:", e2)
        print("....................")

        try:
            # Attempt 3: Partial aria-label contains()
            target_date = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@jsname="nEWxA" and contains(@aria-label, "October 16, 2025")]'))
            )
            driver.execute_script("arguments[0].click();", target_date)
            print("✅ Attempt 3 succeeded: clicked using contains()")

        except Exception as e3:
            print("❌ Attempt 3 failed:", e3)
            print("All attempts to select the date failed 🚨")
sleep(random.uniform(2, 4))
try:
    # Attempt 1: button that has a span with text Done
    done_button = WebDriverWait(driver, 6).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Done"]]'))
    )
    driver.execute_script("arguments[0].click();", done_button)
    print("✅ Done clicked (attempt 1)")

except Exception as e1:
    print("❌ Attempt 1 failed:", e1)
    try:
        # Attempt 2: span with exact text Done, then get parent button
        done_span = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, '//span[text()="Done"]'))
        )
        done_button = done_span.find_element(By.XPATH, './ancestor::button')
        driver.execute_script("arguments[0].click();", done_button)
        print("✅ Done clicked (attempt 2)")

    except Exception as e2:
        print("❌ Attempt 2 failed:", e2)
        try:
            # Attempt 3: any button with role=button and text Done
            done_button = WebDriverWait(driver, 6).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@role="button"]//span[contains(text(),"Done")]'))
            )
            driver.execute_script("arguments[0].click();", done_button)
            print("✅ Done clicked (attempt 3)")
        except Exception as e3:
            print("❌ Attempt 3 failed:", e3)
            print("All Done button attempts failed 😢")

sleep(random.uniform(2,4))
try:
    # Attempt 1
    start_search = driver.find_element(By.CLASS_NAME, "VfPpkd-Jh9lGc")
    start_search.click()
    sleep(random.uniform(1,5))
    print("First attempt succeeded!")
    
except (NoSuchElementException, ElementClickInterceptedException) as x:
    print('First attempt fail because:', x)
    print('....................')
    
    try:
        # Attempt 2
        start_search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search"]'))
        )
        start_search.click()
        print("Second attempt succeeded!")
        
    except (TimeoutException, ElementClickInterceptedException) as x:
        print('Second attempt fail because:', x)
        print('....................')
        
        try:
            # Attempt 3
            start_search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@role="button" and @jsname="LgbsSe"]'))
            )
            start_search.click()
            print("Third attempt succeeded!")
            
        except Exception as x:
            print('Third attempt fail because:', x)
            print('All search button attempts failed!')
            
sleep(10)



# 2️⃣ Wait for initial flight cards
# ----------------------------
cardss = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'pIav2d'))
)
print(f"Initial results : {len(cardss)}")

# ----------------------------
# 3️⃣ Click 'View more flights' if exists
# ----------------------------
try:
    view_more_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='View more flights']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_more_btn)
    driver.execute_script("arguments[0].click();", view_more_btn)
    print("✅ Clicked 'View more flights' button")
    sleep(3)
except Exception as e:
    print(f"Could not find 'View more flights' button: {e}")

# ----------------------------
# 4️⃣ Get all flight cards again after loading more
# ----------------------------
cardss = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, 'pIav2d'))
)
print(f"✅ More flights loaded: {len(cardss)}")
from datetime import datetime, timedelta
import re

def extract_time(text: str) -> str:
    """
    Extracts time in format HH:MM AM/PM from a string like 'Departure time: 7:30AM.'
    """
    match = re.search(r"(\d{1,2}:\d{2}\s?[AP]M)", text, re.IGNORECASE)
    if match:
        return match.group(1).replace(" ", "")  # remove any space before AM/PM
    return text  # fallback

def normalize_time(time_str: str) -> str:
    """
    Ensures time string is in 'HH:MM AM/PM' format for datetime parsing
    """
    time_str = time_str.strip()
    if re.match(r"\d{1,2}:\d{2}[AP]M", time_str, re.IGNORECASE):
        time_str = time_str[:-2] + " " + time_str[-2:]  # add space before AM/PM
    return time_str

def calculate_duration(departure_time: str, arrival_time: str) -> str:
    try:
        dep = datetime.strptime(departure_time.strip(), "%I:%M %p")
        arr = datetime.strptime(arrival_time.strip(), "%I:%M %p")
        if arr < dep:  # overnight flight
            arr += timedelta(days=1)
        duration = arr - dep
        hours, remainder = divmod(duration.seconds, 3600)
        minutes = remainder // 60
        return f"{hours} hr {minutes} min" if minutes else f"{hours} hr"
    except Exception as e:
        return f"Error: {e}"

# ----------------------------
# Scrape flight info
# ----------------------------
results = []

for i, cd in enumerate(cardss, start=1):
    try:
        # Scroll card into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cd)
        sleep(1)

        # Departure + Arrival
        dep_raw = cd.find_element(By.CSS_SELECTOR, 'div.wtdjmc').get_attribute("aria-label")
        arr_raw = cd.find_element(By.CSS_SELECTOR, 'div.XWcVob').get_attribute("aria-label")
        dep = normalize_time(extract_time(dep_raw))
        arr = normalize_time(extract_time(arr_raw))

        # Airline
        try:
            airline = cd.find_element(By.CSS_SELECTOR, 'div.sSHqwe span').text.strip()
        except:
            airline = ""

        # Stops
        stops = ""
        for selector in ["span.rGRiKd", "span.VG3hNb"]:
            try:
                elem = WebDriverWait(cd, 2).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                stops = elem.text.strip()
                if stops:
                    break
            except:
                continue
        if not stops:
            try:
                stops = cd.find_element(By.XPATH, ".//span[contains(text(),'stop')]").text.strip()
            except:
                stops = ""

        # Price
        try:
            price = cd.find_element(By.CSS_SELECTOR, 'div.U3gSDe span[role="text"]').text.strip()
        except:
            price = ""

        # Duration
        duration = calculate_duration(dep, arr)

        # Skip cards with incomplete info
        if not (airline and stops and price):
            print(f"⚠️ Skipping incomplete card {i}: airline='{airline}', stops='{stops}', price='{price}'")
            continue

        # Append results
        results.append((dep, arr, airline, duration, stops, price))

        print(f"{i}. {dep} → {arr} | {airline} | {duration} | {stops} | {price}")

    except Exception as e:
        print(f"⚠️ Error in card {i}: {e}")

# ----------------------------
# 6️⃣ Remove duplicates (based on dep+arr+airline)
# ----------------------------
seen = set()
clean_results = []
for dep, arr, airline, duration, stops, price in results:
    key = (dep, arr, airline)
    if key not in seen:
        clean_results.append((dep, arr, airline, duration, stops, price))
        seen.add(key)

print(f"✅ Cleaned results: {len(clean_results)} unique flights")
import csv
# ----------------------------
# 7️⃣ Save to CSV
# ----------------------------
keys = ["Departure", "Arrival", "Airline", "Duration", "Stops", "Price"]
important_data = [{"Departure": dep, "Arrival": arr, "Airline": airline,
                   "Duration": duration, "Stops": stops, "Price": price} for dep, arr, airline, duration, stops, price in clean_results]

with open("flights.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(important_data)

print("✅ Saved to flights.csv")

# ----------------------------
# 8️⃣ Done
# ----------------------------
driver.quit()
