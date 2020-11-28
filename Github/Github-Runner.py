from pyfcm import FCMNotification


my_api_key = "AIzaSyDjCRTvcoY_wUnh4eC6iqSOphLf_7vgpiE"
my_registration_id = "dL6pNRnkf4U:APA91bECg7PIqeq4zvu7x3aPfqJssODKCAyQC_NKi_5jBV1c9gx8r295wHrdvyU567sqhjs0HGsd5yRzDoRby7iuEAUrqXoHYexyHyHvPwUjgK2W0q4mvK3CwmqT2ADpIN5nxFVVVxN6"

#uploaded to github and therefore insecure because it doesn't matter here
push_service = FCMNotification(api_key=my_api_key)

message_title = "Github update"
message_body = "pull"
result = push_service.notify_single_device(registration_id=my_registration_id, message_title=message_title, message_body=message_body)