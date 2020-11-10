import pandas as pd


if __name__ == "__main__":
    
    path = 'C://Users/RafaeldeOliveiraGatt/Desktop/ufc/data'

    most_recent_event = pd.read_csv('{}/{}.{}'.format(path, 'most-recent-event', 'csv'))
    task_dummy = pd.read_csv('{}/{}.{}'.format(path, 'task-dummy', 'csv'))
    ufc_master = pd.read_csv('{}/{}.{}'.format(path, 'ufc-master', 'csv'))
    upcoming_events = pd.read_csv('{}/{}.{}'.format(path, 'upcoming-event', 'csv'))

    
