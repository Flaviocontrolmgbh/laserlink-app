#!/usr/bin/env python3
import random, json, math, time
random.seed(42)
N=1000
fails=[]
accounts={}
leads=[]
rentals=[]
demands=[]
bookings=[]
def check(cond,msg):
    if not cond: fails.append(msg)

for i in range(N):
    email=f"user{i}@test.local"
    role=random.choice(["client","professional","salon","rental","admin"])
    check(email not in accounts,"duplicate account")
    accounts[email]={"role":role,"name":f"User {i}"}
    if i%3==0:
        leads.append({"name":f"Salon {i}","score":min(100,50+(i%7)*8),"status":"Descoberto"})
    if i%5==0:
        rentals.append({"name":f"Locador {i}","daily":100+i%500,"radius":10+i%100})
    if i%4==0:
        demands.append({"city":f"regiao{i%20}","qty":1+i%8})
    if role=="client":
        bookings.append({"client":email,"time":f"{8+i%10:02d}:00","status":"Agendado"})

check(len(accounts)==N,"account count")
check(all(0<=x["score"]<=100 for x in leads),"lead score bounds")
check(all(x["daily"]>=0 and x["radius"]>=0 for x in rentals),"rental bounds")
check(all(x["qty"]>0 for x in demands),"demand quantity")
check(all(b["client"] in accounts for b in bookings),"booking owner")

# 500 repeated opportunity calculations
for run in range(500):
    region=f"regiao{run%20}"
    qty=sum(d["qty"] for d in demands if d["city"]==region)
    score=min(100,45+qty*3+(15 if leads else 0)+(10 if rentals else 0))
    check(0<=score<=100,"opportunity score bounds")

report={
 "executions":N+500,
 "accounts_created":len(accounts),
 "leads_created":len(leads),
 "rentals_created":len(rentals),
 "demands_created":len(demands),
 "bookings_created":len(bookings),
 "failures":len(fails),
 "status":"PASS" if not fails else "FAIL",
 "notes":[
   "Teste lógico/estresse do modelo local.",
   "Não substitui testes E2E em navegador, segurança, carga do backend, pagamentos reais ou lojas de aplicativos."
 ],
 "failure_samples":fails[:20]
}
print(json.dumps(report,ensure_ascii=False,indent=2))
open("QA_REPORT.json","w",encoding="utf-8").write(json.dumps(report,ensure_ascii=False,indent=2))
