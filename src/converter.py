"""
convert CSV file to semi-colon separated file standard for AFT Reader
"""
import datetime
from os import path
class Converter(object):

    @staticmethod
    def csv_convert(inputfile):
        datetime_object = datetime.datetime.now()
        date,year,month = str(datetime_object.day).zfill(2),str(datetime_object.year),str(datetime_object.month).zfill(2)
        header_text = "Frontend Data;          Version;          V1.06;;;;;;;;;;;;;;;;\n\n\n"
        csv_table = []
        output_table = []
        with open(inputfile) as file:
            for line in file:
                line = line.strip("\n")
                csv_table.append(line)

        test_system = csv_table[1].split(",")[5]

        for line in csv_table:
            output_table.append(line.replace(",",";"))

        output_filname = f"isl_{year}{month}{date}_{test_system}_AFT1.csv"
        output_path = path.join("data","output",output_filname)
        with open(output_path, mode="w") as file:
            file.write(header_text)
            for line in output_table:
                file.write(line + "\n")