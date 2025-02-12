from typing import List, Dict
import pandas as pd

class DataLoader:
    def __init__(self, input_path: str, file_names: List[str]) -> None:
        """
        Initializes the DataProcessor with the given input path and file names.

        Args:
            input_path (str): The directory path where the files are stored.
            file_names (List[str]): List of file names to be read.

        Returns:
            None
        """
        self.input_path = input_path
        self.file_names = file_names
        
    def read_files(self) -> Dict[str, pd.DataFrame]:
        """
        Reads the files specified in the file names and stores them in a dictionary.

        Returns:
            Dict[str, pd.DataFrame]: A dictionary where keys are file names and values are DataFrames.
        """
        self.data = {}
        print("Reading files...")
        for file in self.file_names:
            with open(self.input_path + file + '.txt', 'r') as f:
                self.data[file] = pd.read_csv(f, header=None, sep='\t')
        return self.data
    
    def print_shape(self) -> None:
        """
        Prints the shape of each loaded DataFrame.

        Returns:
            None
        """
        print("Files read:")
        for file in self.data:
            print(f"{file}: {self.data[file].shape}")
            
    def create_target_df(self) -> pd.Series:
        """
        Renames the columns in the data['target'] and creates the wanted target DataFrame by extracting the column 'Valve_Condition'.

        Returns:
            pd.Series: A pandas Series containing the 'Valve_Condition' column from the target DataFrame.
        """
        target_columns = ['Cooler_Condition', 'Valve_Condition', 
                          'Internal_Pump_Leakage', 'Hydraulic_Accumulator', 
                          'Stable_Flag']
        self.data['target'].columns = target_columns
        self.valve_condition = self.data['target']['Valve_Condition']
        return self.valve_condition