import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(0,0, 35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(-1,0, 35) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(30, 0,35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(35,0,35) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(37,0,35) == 'TOO_HIGH')
   
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 35)=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 30)=='NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 30)=='NORMAL')
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == "__main__":
  unittest.main()
