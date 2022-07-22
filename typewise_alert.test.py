import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(140, 50, 100) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
    
  def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -40)== 'TOO_LOW') 
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 25)== 'NORMAL') 
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 50)== 'TOO_HIGH') 
   
  def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -50)== 'TOO_LOW') 
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 35)== 'NORMAL') 
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 80)== 'TOO_HIGH') 
    
  def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -60)== 'TOO_LOW') 
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 30)== 'NORMAL') 
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 90)== 'TOO_HIGH') 
    
  def test_send_to_controller_breachType_too_high(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == f'{0xfeed}, TOO_HIGH')
    
  def test_send_to_controller_breachType_too_low(self):
    self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')
    
  def test_send_to_email_TOO_LOW(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_LOW') ==f'To: a.b@c.com, Hi, the temperature is too low')
    
  def test_send_to_email_TOO_HIGH(self):
    self.assertTrue(typewise_alert.send_to_email('TOO_HIGH') ==f'To: a.b@c.com, Hi, the temperature is too high') 

  def test_check_and_alert_send_to_email(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING',-20) == f'To: a.b@c.com, Hi, the temperature is too low')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING',-5 ) == f'To: a.b@c.com, Hi, the temperature is too low')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING',-5) == f'To: a.b@c.com, Hi, the temperature is too low')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL','PASSIVE_COOLING', 70)== f'To: a.b@c.com, Hi, the temperature is too high')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING',-25)==f'To: a.b@c.com, Hi, the temperature is too low')
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'HI_ACTIVE_COOLING', 100)==f'To: a.b@c.com, Hi, the temperature is too high') 
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', -35)==f'To: a.b@c.com, Hi, the temperature is too low')     
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 120)==f'To: a.b@c.com, Hi, the temperature is too high')   
    self.assertFalse(typewise_alert.check_and_alert('NA', 'MED_ACTIVE_COOLING',30)==f'To: a.b@c.com, Not applicable')
    
  def test_check_and_alert_to_controller(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING',-40)==f'{0xfeed}, TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', 130)==f'{0xfeed}, TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'HI_ACTIVE_COOLING', 35)==f'{0xfeed}, NORMAL')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING',-10)==f'{0xfeed}, TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING', 90)==f'{0xfeed}, TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER','PASSIVE_COOLING', 15)==f'{0xfeed}, NORMAL')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING', -25)==f'{0xfeed}, TOO_LOW')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING', 100)==f'{0xfeed}, TOO_HIGH')
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'MED_ACTIVE_COOLING',30)==f'{0xfeed}, NORMAL')  
    self.assertFalse(typewise_alert.check_and_alert('NA', 'MED_ACTIVE_COOLING',25)==f'{0xfeed}, Not applicable')
    
    
if __name__ == '__main__':
  unittest.main()
