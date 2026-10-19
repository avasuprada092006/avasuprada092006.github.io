from pathlib import Path
import csv, json, random, statistics
from datetime import date, timedelta

OUT=Path(__file__).parent; rng=random.Random(19072026); priorities=["High","Medium","Low"]; sla={"High":8,"Medium":24,"Low":48}; cats=["Account access","Billing","Delivery","Product help","Returns"]; channels=["Email","Chat","Web form"]; bias={"Account access":1.03,"Billing":.92,"Delivery":1.14,"Product help":1.08,"Returns":1.18}; base={"High":6.4,"Medium":17.2,"Low":34.0}; rows=[]; start=date(2025,1,1)
for i in range(480):
 d=start+timedelta(days=rng.randrange(365)); p=rng.choices(priorities,weights=[18,47,35],k=1)[0]; c=rng.choice(cats); ch=rng.choices(channels,weights=[38,42,20],k=1)[0]; target=sla[p]; resolution=round(base[p]*rng.uniform(.38,1.58)*bias[c],1); response=round(min(resolution*rng.uniform(.05,.38),target*.9),1); met=int(resolution<=target); rating=max(1,min(5,round(rng.gauss(4.25 if met else 2.95,.8)))); rows.append({"ticket_id":f"T{i+1:04d}","created_date":d.isoformat(),"priority":p,"category":c,"channel":ch,"first_response_hours":response,"resolution_hours":resolution,"sla_hours":target,"sla_met":met,"customer_rating":rating})
rows.sort(key=lambda x:(x["created_date"],x["ticket_id"]))
with (OUT/"tickets.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
rate=sum(x["sla_met"] for x in rows)/len(rows)*100; med=statistics.median(x["resolution_hours"] for x in rows); avg=statistics.mean(x["customer_rating"] for x in rows)
(OUT/"metrics.json").write_text(json.dumps({"row_count":len(rows),"sla_rate_pct":round(rate,1),"median_resolution_hours":round(med,1),"average_rating":round(avg,2)},indent=2),encoding="utf-8")
print("Wrote synthetic tickets.csv and metrics.json")
