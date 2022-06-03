"""
convert CSV file to semi-colon separated file standard for AFT Reader
"""
import datetime
from os import path
import pandas as pd
class Converter(object):

    @staticmethod
    def process(inputfile,output_path, log_path):
        table = Converter.import_from_file(inputfile)
        if table is None:
            return
        return Converter.output_csv(output_path,table,log_path)

    @staticmethod
    def import_from_file(inputfile):
        """
        Accepts an excell file and coverts it into a ready-to-import AFT format.
    Filename is generated based on the TType column
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
        df.dropna(subset=[1], inplace=True)
        df.dropna(axis='columns', inplace=True)
        data_table = df.values.tolist()

        return data_table

    @staticmethod
    def output_csv(output_path,input_table,log_path):
        datetime_object = datetime.datetime.now()
        hour, minute, second, microsecond = str(datetime_object.hour).zfill(2), str(datetime_object.minute).zfill(2), str(
            datetime_object.second).zfill(2),str(datetime_object.microsecond).zfill(2)[2:]
        date, year, month = str(datetime_object.day).zfill(2), str(datetime_object.year), str(
            datetime_object.month).zfill(2)
        header_text = "Frontend Data;          Version;          V1.06;;;;;;;;;;;;;;;;\n\n\n" \
                      "Date;SampleID;SIType;WNo;SlID;TType;StTiter;Time;SampleType;PName;Surname;DayOfB;MonOfB;YearOfB;PatientID;Comm\n"
        test_system = input_table[1][5]
        output_table = []
        lot = input("Please type the slide lot number used for this scan event\n")
        label = input("Please describe the test event\n")
        initials = input("Please type your initials\n")
        for line in input_table[1:]:
            for pos,value in enumerate(line):
                if not (pos == 1 or pos == 4):
                    continue
                for character in value:
                    if not character.isalnum() and character not in "_- ":
                        print("Invalid character detected. Slide and sample IDs may only contain alphanumeric characters, dashes, or underscores.")
                        return
        for value in (label,initials,lot):
            for character in value:
                if not character.isalnum() and character not in "_- ":
                    print("Invalid character detected. Label and Initials may only contain alphanumeric characters, dashes, or underscores.")
                    return
        for line in input_table[1:]:
            line[0] = f"{month}/{date}/{year}"
            line[7] = f"{hour}:{minute}:{second}"
            line[9] = initials
            line[14] = lot
            line[15] = label
            output_table.append(";".join(line))

        output_filename = f"isl_{year}{month}{date}_{hour}{minute}{second}_{microsecond}_{test_system}_AFT1.csv"
        with open(path.join(output_path,output_filename), mode="w") as file:
            file.write(header_text)
            for line in output_table:
                file.write(line + "\n")

        with open(path.join(log_path,"log.csv"), mode="a",) as file:
            file.write(f"{test_system},{label},{initials},{year}-{month}-{date} {hour}:{minute}\r")
        print("Event added to log")
