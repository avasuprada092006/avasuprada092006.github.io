from pathlib import Path
import csv, json, random
from datetime import date, timedelta

OUT = Path(__file__).parent
rng = random.Random(20261019)
products = {"Electronics": [("Wireless Mouse",899,.62),("USB Hub",1299,.58),("Webcam",3499,.67)], "Home": [("Desk Lamp",1199,.55),("Storage Box",499,.48),("Water Bottle",699,.44)], "Books": [("Data Basics",499,.52),("Design Handbook",699,.50),("Career Guide",399,.46)], "Grocery": [("Coffee Pack",349,.71),("Snack Box",249,.66),("Tea Pack",199,.63)]}
regions=["North","South","East","West"]; bias=[.92,.95,.97,1,1.02,1.05,1.08,1.03,1.10,1.14,1.22,1.28]; rows=[]; start=date(2025,1,1)
for i in range(720):
 d=start+timedelta(days=rng.randrange(365)); cat=rng.choices(list(products),weights=[31,25,18,26],k=1)[0]; product,base,cost_share=rng.choice(products[cat]); qty=rng.choices([1,2,3,4],weights=[55,28,12,5],k=1)[0]; discount=round(rng.choice([0,.05,.1,.15,.2]),2); price=round(base*bias[d.month-1]*rng.uniform(.92,1.08),2); revenue=round(qty*price*(1-discount),2); cost=round(qty*price*cost_share,2); rows.append({"order_id":f"R{i+1:04d}","order_date":d.isoformat(),"region":rng.choices(regions,weights=[31,29,19,21],k=1)[0],"category":cat,"product":product,"quantity":qty,"unit_price_inr":price,"discount_pct":discount,"revenue_inr":revenue,"cost_inr":cost,"profit_inr":round(revenue-cost,2)})
rows.sort(key=lambda x:(x["order_date"],x["order_id"]))
with (OUT/"orders.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
monthly={}
for x in rows: monthly[x["order_date"][:7]]=monthly.get(x["order_date"][:7],0)+x["revenue_inr"]
revenue=sum(x["revenue_inr"] for x in rows); profit=sum(x["profit_inr"] for x in rows)
(OUT/"metrics.json").write_text(json.dumps({"row_count":len(rows),"revenue":round(revenue,2),"profit":round(profit,2),"margin_pct":round(profit/revenue*100,1),"monthly":monthly},indent=2),encoding="utf-8")
print("Wrote synthetic orders.csv and metrics.json")
