"""
convert CSV file to semi-colon separated file standard for AFT Reader
"""
import datetime
from os import path
import pandas as pd
class Converter(object):

    datetime_object = datetime.datetime.now()
    hour, minute, second = str(datetime_object.hour).zfill(2), str(datetime_object.minute).zfill(2), str(
        datetime_object.second).zfill(2)
    date, year, month = str(datetime_object.day).zfill(2), str(datetime_object.year), str(
        datetime_object.month).zfill(2)

    @staticmethod
    def process(inputfile,output_path):
        table = Converter.import_from_file(inputfile)
        if table is None:
            return
        return Converter.output_csv(output_path,table)

    @staticmethod
    def import_from_file(inputfile):
        """
        Accepts an excell file and coverts it into a ready-to-import AFT format. Filename is generated based on the TType column
        :param inputfile: directory and filename of the CSV
        :param output_path: folder to output AFT file
        :return: None
        """


        extension = inputfile.split(".")[1].lower()
        if "~" in inputfile:
            return
        elif extension == "csv":
            print(f"processing csv file: {inputfile}")
            df = pd.read_csv(inputfile, header=None, dtype=str)
        elif extension == "xls" or extension == "xlsx":
            print(f"processing Excel file: {inputfile}")
            df = pd.read_excel(inputfile, header=None, dtype=str)
        else:
            print(f"Skipping unknown filetype: {inputfile}")
            return

        data_table = df.values.tolist()

        return data_table

    @staticmethod
    def output_csv(output_path,input_table):
        header_text = "Frontend Data;          Version;          V1.06;;;;;;;;;;;;;;;;\n\n\n" \
                      "Date;SampleID;SIType;WNo;SlID;TType;StTiter;Time;SampleType;PName;Surname;DayOfB;MonOfB;YearOfB;PatientID;Comm\n"
        test_system = input_table[1][5]
        output_table = []
        for line in input_table[1:]:
            line[0] = f"{Converter.month}/{Converter.date}/{Converter.year}"
            line[7] = f"{Converter.hour}:{Converter.minute}:{Converter.second}"
            output_table.append(";".join(line))

        output_filname = f"isl_{Converter.year}{Converter.month}{Converter.date}_{Converter.hour}{Converter.minute}{Converter.second}_{test_system}_AFT1.csv"
        with open(path.join(output_path,output_filname), mode="w") as file:
            file.write(header_text)
            for line in output_table:
                file.write(line + "\n")
        print(f"{output_filname} created in Image Navigator.\n")
