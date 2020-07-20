import pandas as pd


# Create class: PeakEstMain
class PeakEstMain:
    
    """Creates pre-processing class for estimation of true peaks in a distribution
    :filename: name of dataset file to be preprocessed specified columns in dataset
    :get_stats: returns descriptive stats for dataset
    """
    # Define initialization method
    def __init__(self, filename):
        # Set filename as instance variable
        self.filename = filename
        # Set data_as_csv as instance variable. Convert 'Voltage' column
        # to an array for input to peak calculation functions
        self.data_as_csv = pd.read_csv(filename)
        #self.data_as_csv.columns[1] = self.data_as_csv[1].reset_index().values

    # Define get_stats method, with argument self
    def _get_stats(self):
        # Return a description data_as_csv
        return self.data_as_csv.describe()

         
