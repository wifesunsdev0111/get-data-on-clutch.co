from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from selenium_driverless.types.webelement import NoSuchElementException
import re
from time import sleep
import quickstart




urls = ["https://clutch.co/agencies", "https://clutch.co/agencies/digital", "https://clutch.co/agencies/digital-strategy", "https://clutch.co/agencies/digital-marketing",
        "https://clutch.co/agencies/social-media-marketing", "https://clutch.co/agencies/content-marketing", "https://clutch.co/agencies/email", "https://clutch.co/agencies/inbound-marketing",
        "https://clutch.co/agencies/direct-marketing", "https://clutch.co/agencies/app-marketing", "https://clutch.co/agencies/event", "https://clutch.co/agencies/experiential", "https://clutch.co/agencies/creative",
        "https://clutch.co/pr-firms", "https://clutch.co/agencies/video-production", "https://clutch.co/agencies/branding", "https://clutch.co/agencies/naming", "https://clutch.co/agencies/ppc",
        "https://clutch.co/seo-firms", "https://clutch.co/agencies/sem", "https://clutch.co/agencies/conversion-optimization", "https://clutch.co/agencies/market-research", "https://clutch.co/agencies/media-buying",
        "https://clutch.co/it-services/marketing-automation", "https://clutch.co/web-developers", "https://clutch.co/developers", "https://clutch.co/directory/mobile-application-developers",
        "https://clutch.co/directory/iphone-application-developers", "https://clutch.co/directory/android-application-developers", "https://clutch.co/developers/ecommerce", "https://clutch.co/developers/artificial-intelligence",
        "https://clutch.co/developers/blockchain", "https://clutch.co/developers/virtual-reality", "https://clutch.co/developers/internet-of-things", "https://clutch.co/developers/ruby-rails",
        "https://clutch.co/developers/shopify", "https://clutch.co/developers/wordpress", "https://clutch.co/developers/drupal", "https://clutch.co/developers/magento", "https://clutch.co/developers/dot-net", "https://clutch.co/web-developers/php",
        "https://clutch.co/app-developers/wearables", "https://clutch.co/developers/testing", "https://clutch.co/agencies/design", "https://clutch.co/agencies/digital-design", "https://clutch.co/web-designers",
        "https://clutch.co/agencies/ui-ux", "https://clutch.co/agencies/packaging-design", "https://clutch.co/agencies/print-design", "https://clutch.co/agencies/graphic-designers", "https://clutch.co/agencies/logo-designers",
        "https://clutch.co/agencies/product-design", "https://clutch.co/agencies/design/interior", "https://clutch.co/it-services", "https://clutch.co/it-services/analytics", "https://clutch.co/it-services/staff-augmentation",
        "https://clutch.co/it-services/cybersecurity", "https://clutch.co/it-services/cloud", "https://clutch.co/it-services/msp", "https://clutch.co/bpo", "https://clutch.co/hr", "https://clutch.co/consulting",
        "https://clutch.co/accounting", "https://clutch.co/accounting/payroll", "https://clutch.co/call-centers", "https://clutch.co/call-centers/answering-services", "https://clutch.co/call-centers/telemarketing",
        "https://clutch.co/transcription", "https://clutch.co/translation", "https://clutch.co/real-estate", "https://clutch.co/logistics/supply-chain-management", "https://clutch.co/logistics/manufacturing-companies",
        "https://clutch.co/logistics/customs-brokers", "https://clutch.co/logistics/distribution-companies", "https://clutch.co/logistics/fulfillment-services", "https://clutch.co/logistics/freight-forwarders", "https://clutch.co/logistics/rail-freight-companies",
        "https://clutch.co/logistics/air-freight-companies", "https://clutch.co/logistics/trucking-companies", "https://clutch.co/logistics/container-shipping-companies", "https://clutch.co/logistics/3pls", "https://clutch.co/logistics/shipping-companies",
        "https://clutch.co/law", "https://clutch.co/hr/executive-search", "https://clutch.co/hr/staffing", "https://clutch.co/hr/recruiting", "https://clutch.co/hr/consultants", "https://clutch.co/hr/peo", "https://clutch.co/hr/outsourcing"]




# options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# for url in urls:
def replace_str(str):
    str_1 =  str.replace('\t', '').replace('\n', '')
    modified_string = re.sub(r"\s+", " ", str_1)
    return modified_string

for url in urls:
    driver =  webdriver.Chrome()
    driver.maximize_window() 
    driver.get(url)
    sleep(5)
    cookie_button = driver.find_element(By.CSS_SELECTOR, "a[id=\"CybotCookiebotDialogBodyButtonAccept\"]")
    cookie_button.click()
    sleep(1)
    company_lists = []
    company_list_1 = []
    company_list_2 = []

    while True:
        try:
            sleep(20)
            next = driver.find_element(By.CSS_SELECTOR, "li[class=\"page-item next\"]")
            try:
                company_list_1 = driver.find_elements(By.CSS_SELECTOR, "li[class=\"provider provider-row sponsor \"]")
            except:
                pass

            try:
                company_list_2 = driver.find_elements(By.CSS_SELECTOR, "li[class=\"provider provider-row\"]")
            except:
                pass

            company_lists = company_list_1 + company_list_2

            for index, company in enumerate(company_lists):
                print(index, len(company_lists))
                
                category = ""
                company_name = ""
                empolyees = ""
                location = ""
                hourly_rate = ""
                total_reviews = ""
                review_rating = ""
                min_project_size = ""
                found_date = ""
                most_common_project_size = ""
                headquarters_address = ""

                try:
                    driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", company)
                except:
                    pass
            
                sleep(5)
                try:
                    location = company.find_element(By.CSS_SELECTOR, "span[class=\"locality\"]").text
                except:
                    pass
            
                try:
                    detail_dom = company.find_element(By.CSS_SELECTOR, "a[class=\"directory_profile\"]")
                except:
                    pass
                
                try:
                    detail_dom.click()
                except:
                    pass

                sleep(6)
                
                try:
                    window_handles = driver.window_handles
                    driver.switch_to.window(window_handles[0])
                except:
                    pass
                
                sleep(2)
                

                try:
                    category = driver.find_element(By.CSS_SELECTOR, "h2[class=\"profile-summary__tagline\"]").text
                except:
                    pass

                try:
                    company_name = driver.find_element(By.CSS_SELECTOR, "a[class=\"website-link__item\"]").text
                except:
                    pass

                try:
                    empolyees_icon = driver.find_element(By.CSS_SELECTOR, "li[data-tooltip-content=\"<i>Employees</i>\"]")
                    empolyees = empolyees_icon.text
                except:
                    pass

                try:
                    hourly_rate = driver.find_element(By.CSS_SELECTOR, "li[data-tooltip-content=\"<i>Avg. hourly rate</i>\"]").text
                except:
                    pass
            
                try:
                    min_project_size = driver.find_element(By.CSS_SELECTOR, "li[data-tooltip-content=\"<i>Min. project size</i>\"]").text
                except:
                    pass

                try:
                    found_date = driver.find_element(By.CSS_SELECTOR, "li[data-tooltip-content=\"<i>Founded</i>\"]").text
                except:
                    pass
                
                try:
                    profile_section = driver.find_element(By.CSS_SELECTOR, "section[class=\"container profile-metrics profile-metrics--section profile-section\"]")
                    profiles = profile_section.find_elements(By.CSS_SELECTOR, "div[class=\"profile-metrics--card sg-colored-card sg-colored-card--border-top\"]")

                except:
                    pass
                
                try:
                    total_reviews_dom = profiles[1]
                    total_reviews = total_reviews_dom.find_element(By.TAG_NAME, "dd").text
                except:
                    pass

                try:
                    most_common_project_size_dom = profiles[2]
                    most_common_project_size = most_common_project_size_dom.find_element(By.TAG_NAME, "dd").text
                except:
                    pass
                
                try:
                    review_rating_dom = profiles[3]
                    review_rating = review_rating_dom.find_element(By.TAG_NAME, "dd").text
                except:
                    pass

                try:
                    headquarters_address = driver.find_element(By.CSS_SELECTOR, "address[class=\"detailed-address to-hide hidden location_element\"]").text
                except:
                    pass
                
                try:
                    phone_number = driver.find_element(By.CSS_SELECTOR, "a[class=\"tel location_element to-hide hidden\"]").text
                except:
                    pass
                

                quickstart.main()
                columnCount = quickstart.getColumnCount()
                    
                results = []
                results.append(str(columnCount + 1))
                results.append(replace_str(category))
                results.append(replace_str(company_name))
                results.append(replace_str(empolyees))
                results.append(replace_str(location))
                results.append(replace_str(hourly_rate))
                results.append(replace_str(total_reviews))
                results.append(replace_str(review_rating))
                results.append(replace_str(min_project_size))
                results.append(replace_str(found_date))
                results.append(replace_str(most_common_project_size))
                results.append(replace_str(headquarters_address))
                results.append(replace_str(phone_number))

                print(results)

                RANGE_DATA = f'company_info!A{columnCount + 2}:M'
                quickstart.insert_data(RANGE_DATA, results)
                
                sleep(2)
                
                try:
                    driver.close()
                except:
                    pass
                
                sleep(2)
                
                try:
                    driver.switch_to.window(window_handles[1])
                except:
                    pass
            
            sleep(5)
            try:
                next.click()
            except:
                 next_again = driver.find_element(By.CSS_SELECTOR, "li[class=\"page-item next\"]")
                 next_again.click()
        
        except:
            break
    driver.quit()







        
            

