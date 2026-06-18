import tempfile,unittest
from pathlib import Path
from src.medallion import run
class MedallionTest(unittest.TestCase):
 def test_deduplicates(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);s=p/"x.csv";s.write_text("transaction_id,amount\n1,10\n1,10\n2,5\n")
   self.assertEqual(run(s,p/"out"),{"transactions":2,"revenue":15.0})
if __name__=="__main__":unittest.main()