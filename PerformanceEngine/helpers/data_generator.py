import json
import random
from names_generator import generate_name

all_services = ["Applications Development", "Applications Maintenance", "Mainframe services", "Service Desk", "Managed Services", "Support"]
all_countries_str = "Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Cape Verde, Central African Republic, Chad, Comoros, Cote d'Ivoire, Democratic Republic of the Congo, Djibouti, Egypt, Equatorial Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Morocco, Mozambique, Namibia, Niger, Nigeria, Republic of the Congo, Reunion, Rwanda, Saint Helena, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Western Sahara, Zambia, Zimbabwe, Afghanistan, Armenia, Azerbaijan, Bahrain, Bangladesh, Bhutan, Brunei, Burma, Cambodia, China, Cyprus, East Timor, Georgia, Hong Kong, India, Indonesia, Iran, Iraq, Israel, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Laos, Lebanon, Macau, Malaysia, Maldives, Mongolia, Nepal, North Korea, Oman, Pakistan, Philippines, Qatar, Saudi Arabia, Singapore, South Korea, Sri Lanka, Syria, Taiwan, Tajikistan, Thailand, Turkey, Turkmenistan, United Arab Emirates, Uzbekistan, Vietnam, Yemen, Anguilla, Antigua and Barbuda, Aruba, The Bahamas, Barbados, Bermuda, British Virgin Islands, Cayman Islands, Cuba, Dominica, Dominican Republic, Grenada, Guadeloupe, Haiti, Jamaica, Martinique, Montserrat, Netherlands Antilles, Puerto Rico, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Trinidad and Tobago, Turks and Caicos Islands, U.S. Virgin Islands, Belize, Costa Rica, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Albania, Andorra, Austria, Belarus, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Holy See, Hungary, Iceland, Ireland, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Macedonia, Malta, Moldova, Monaco, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, Russia, San Marino, Slovak Republic, Slovenia, Spain, Serbia, Serbia and Montenegro, Sweden, Switzerland, Ukraine, the United Kingdom, Canada, Greenland, Mexico, Saint Pierre and Miquelon, United States, the countries within the regions of the Caribbean and Central America, American Samoa, Australia, Christmas Island, Cocos (Keeling) Islands, Cook Islands, Federated States of Micronesia, Fiji, French Polynesia, Guam, Kiribati, Marshall Islands, Nauru, New Caledonia, New Zealand, Niue, Northern Mariana Islands, Palau, Papua New Guinea, Pitcairn Islands, Samoa, Solomon Islands, Tokelau, Tonga, Tuvalu, Vanuatu, Wallis and Futuna Islands, Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Falkland Islands, French Guiana, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela "
all_countries = all_countries_str.split(", ")
print(len(all_countries))
all_suppliers = []  # {service: [] for service in all_services}

count = 0
with open('helpers/all_india_services_data.json') as services_json:
    suppliers_data = json.loads(services_json.read())
    total = len(suppliers_data) * 5 * len(all_countries) * len(all_services)
    for supplier in suppliers_data:
        for i in range(5):
            for country in all_countries:
                for service in all_services:
                    print(f"Generating {count} / {total}")
                    count += 1
                    current_supplier = f'{supplier["Company"]} {generate_name()}'
                    rank = f'{supplier["Rank"]}'
                    delivery_time = random.randint(25, 400)
                    cost_ratio = random.randint(900, 1250)
                    cost = delivery_time * cost_ratio
                    rating = random.randint(70, 99)
                    escalations = random.randint(3, 500)
                    year = random.randint(2002, 2021)
                    resources = random.randint(300, 9000)
                    all_suppliers.append({
                        "Supplier Name": current_supplier,
                        "Country": country,
                        "Service": service,
                        "Avg. Cost($)": cost,
                        "Rating": rating,
                        "Average Delivery Time": delivery_time,
                        "Number of Escalations": escalations,
                        "Year": year,
                        "Resources": resources,
                        "Rank": rank
                    })

print(len(all_suppliers))

for service in all_services:
    with open(f'/Users/vigneswaran/Projects/sirion/SupplierPerformance/sample_data/all_suppliers.json', 'w', encoding='utf-8') as f:
        json.dump(all_suppliers, f, ensure_ascii=False, indent=4)


