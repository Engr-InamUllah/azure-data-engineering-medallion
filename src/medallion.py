import csv, json
from pathlib import Path

def run(source: Path, root: Path):
    bronze=list(csv.DictReader(source.open(encoding="utf-8")))
    silver=[]; seen=set()
    for r in bronze:
        if r["transaction_id"] in seen or float(r["amount"])<0: continue
        seen.add(r["transaction_id"]); silver.append({**r,"amount":round(float(r["amount"]),2)})
    gold={"transactions":len(silver),"revenue":round(sum(r["amount"] for r in silver),2)}
    for layer,payload in (("bronze",bronze),("silver",silver),("gold",gold)):
        path=root/layer/"data.json";path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(payload,indent=2))
    return gold
if __name__=="__main__":run(Path("data/transactions.csv"),Path("output"))