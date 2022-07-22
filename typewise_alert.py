
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit=0
    coolingType_dict={"PASSIVE":35,"HI_ACTIVE":45,"MED_ACTIVE":40}    #Cooling Type classification
    for cool_type in coolingType_dict.keys():
        if cool_type==coolingType:
            upperLimit=coolingType_dict[cool_type]
    breachType=infer_breach(value,lowerLimit,upperLimit)
    return breachType


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType=classify_temperature_breach(value,coolingType)
  if alertTarget == 'TO_CONTROLLER':
    message=send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    message=send_to_email(breachType)
  return message


def send_to_controller(breachType):
  header = 0xfeed
  controller_message='{header}, {breach}'.format(header = header,breach=breachType)
  print(controller_message)
  return controller_message


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
      email_message=f'To: {recepient},Hi, the temperature is too low'.format(recepient=recepient)
  elif breachType == 'TOO_HIGH':
      email_message=f'To: {recepient},Hi, the temperature is too high'.format(recepient=recepient)
  print(email_message)
  return email_message
