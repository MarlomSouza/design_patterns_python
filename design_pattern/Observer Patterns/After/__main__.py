from kpis import KPIs
from current_kpis import CurrentKPIs
from forescast_kpis import ForecastKPIs


with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(10, 5, 3)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50.10, 20)

print("Detaching the current Kpis...")
kpis.set_kpis(20, 19, 2)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      