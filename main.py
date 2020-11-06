from src.converter import Converter
import os

input_path = os.path.join("data","input")
for filename in os.listdir(input_path):
    Converter.csv_convert(os.path.join(input_path,filename))