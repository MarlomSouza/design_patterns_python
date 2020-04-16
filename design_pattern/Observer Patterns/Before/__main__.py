from .KPI_data import  KPI_Data

for kpi in KPI_Data:
    if kpi.name == 'open':
        print(f'Current open tickets: {kpi.value}')
    elif kpi.name == 'new':
        print(f"Current new tickets: {kpi.value}")
    elif kpi.name == 'closed':
        print(f"Current closed ticket: {kpi.value}")

