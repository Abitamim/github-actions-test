from pyfcm import FCMNotification


my_api_key = "AIzaSyDjCRTvcoY_wUnh4eC6iqSOphLf_7vgpiE"
my_registration_id = "AAAA0LI0lc8:APA91bFszMEf9jEIrN-fsY5gBKLTm5OVlruqaoylfu-7m2XY15_oneSlOKdqEHxosK1af4-wQWnEGnWoE-dNPd7efKzSHhFrFrvq4kNP8PUrcj5CM8FwyF2T8hDTZ99g0QnQBqGKQIDe"

#uploaded to github and therefore insecure because it doesn't matter here
push_service = FCMNotification(api_key=my_api_key)

message_title = "Github update"
message_body = "pull"
result = push_service.notify_single_device(registration_id=my_registration_id, message_title=message_title, message_body=message_body)