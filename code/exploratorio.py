import os
import pandas as pd
from decorador import gerador_try_except


df_recents_events = pd.read_csv("C://Users/RafaeldeOliveiraGatt/Desktop/ufc/data/most-recent-event.csv")
df_upcoming_events = pd.read_csv("C://Users/RafaeldeOliveiraGatt/Desktop/ufc/data/upcoming-event.csv")
df_ufc_master = pd.read_csv("C://Users/RafaeldeOliveiraGatt/Desktop/ufc/data/ufc-master.csv")
df_task_dummy = pd.read_csv("C://Users/RafaeldeOliveiraGatt/Desktop/ufc/data/task-dummy.csv")

