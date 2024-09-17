from data.data_loader import DataLoader
from analysis.data_processor import DataProcessor
from ui.main_window import run_gui

if __name__ == '__main__':
    # Daten laden
    persons = DataLoader.load_data()

    # Initialisierung des DataProcessors
    processor = DataProcessor(persons)

    # Start des GUI
    run_gui(processor)
