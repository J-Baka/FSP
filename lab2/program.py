#!/usr/local/bin/python3
#Saul Morales, Donald Jalving, Malane Lieng, Brandon Nguyen, Matthew Hernandez, 
#Monica Velasco, Kamari Hooks, Gabby Gil- Mazariegos, Gregorio Lopez
import json
import os
import xml.etree.ElementTree as xmltree
from logger import Logger


class Program:
    # !/usr/local/bin/python3
    import json
    import os
    import xml.etree.ElementTree as xmltree
    from logger import Logger

    class Program:
        def __init__(self, x):
            self.this_folder = os.path.dirname(x)
            self.data_folder = os.path.join(self.this_folder, os.pardir, os.pardir, "Lab2")
            self.data_folder = os.path.abspath(self.data_folder)
            self.logger = Logger(os.path.join(self.data_folder, "log.txt"))

        def run(self):
            try:
                self.log_startup(),self.load_xml(),self.load_json(),self.load_csv()
            except Exception as e:
                print(e.__repr__())

        def log_startup(self):
            self.logger.log("Application starting up...")
            self.logger.log("Data folder: {0}".format(self.data_folder))

    def load_xml(self):
        filename = os.path.join(self.data_folder, "michael-kennedy-blog.xml")
        self.logger.log("Loading XML file: {0}".format(filename))
        dom = xmltree.ElementTree()
        print(dom)
        dom.parse(filename)
        root = dom.getroot()
        print(root)

        print("Titles of recent posts:")
        items = list(dom.findall("channel/item"))
        self.logger.log("Found {0} titles in RSS feed.".format(len(items)))
        
                # writing to xml 
        myfile = open('data/xml_output.xml', 'w')
        myfile.write(items)
        
        for item in items:
            print("{0} [{1}]".format(
                item.find("title").text,
                item.find("link").text))
        print()

        def load_json(self):
            filename = os.path.join(self.data_folder, "python-course.json")
            self.logger.log("Loading JSON file: {0}".format(filename))

            with open(filename, "r") as fin:
                data = json.loads(fin.read())
                print("Course title: {0}".format(data["Name"]))
                self.logger.log("Found course title to be: {0}".format(data["Name"]))
                engagements = data["Engagements"]
                print("Number of engagements: {0}".format(len(engagements)))
                print("Locations:")
                for e in engagements:
                    print("\t" + e["City"] + " on " + e["StartDate"] + " [active? " + str(e["ActiveEngagement"]) + "]")
                with open("new.json", "w") as write_file:
                json.dump(data, write_file)
            print()

    def load_csv(self):
        filename = os.path.join(self.data_folder, "fx-seven-day.csv")
        self.logger.log("Loading CSV file: {0}".format(filename))

        # Answer what is the 7 day average for RUPEEs to USD?
        # (need to go from rupees -> canadian dollars -> usd)

        lookup = self.build_currency_lookup(filename)
        rupee = lookup["INR"]
        usd = lookup["USD"]
        rupees_per_canadian_dollar = self.average(rupee["values"])
        usa_per_canadian_dollar = self.average(usd["values"])

        rupee_per_usd = usa_per_canadian_dollar / rupees_per_canadian_dollar

        print("1 USD is worth {0} Rupees.".format(rupee_per_usd))
        self.logger.log("1 USD is worth {0} Rupees.".format(rupee_per_usd))
        with open("fx-seven-day.csv", 'r') as old, open("new.csv", 'w') as new: #outputs to new .csv file
            writer = csv.writer(new)
            writer.writerows(line.split() for line in old)

        @staticmethod
        def build_currency_lookup(filename):
            lookup = dict()
            with open(filename, "r") as fin:
                for line in fin:
                    if line is None or line.strip().startswith('#') or line.startswith(
                            'Date'):  # optimized with one line
                        continue

                    parts = line.split(sep=',')
                    entry = {
                        "name": parts[0].strip(),
                        "key": parts[1].strip(),
                        "values": [float(parts[2]), float(parts[3]), float(parts[4]),
                                float(parts[5]),float(parts[6]), float(parts[7]), float(parts[8]),]
                        # reduced amount of lines
                    }

                    lookup[entry["key"]] = entry
            return lookup

        @staticmethod
        def average(numbers):
            if len(numbers) <= 0:
                return float('nan')

            return sum(numbers) / float(len(numbers))

    if __name__ == "__main__":
        p = Program("C:\Lab2")
        p.run()

