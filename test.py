import schedule
import time
import requests
#minimalmodbus?
import minimalmodbus

instr = minimalmodbus.Instrument('dev address?', 1)
#minimalmodbus.Instrument<id=0xb7437b2c, address=1>
#setup something abbove I guess?

#this will get the tempureture I guess?
temp_result = instr.read_register(24, 1)
temp_result = int(temp_result);
##########
tony_ser_url = "http://holyshit.com/post";
#test_file = open("tonystext.txt", "rb"); dont need to oprn file anymore.

def job(temp_result):
    print("hello");
    test_response = requests.post(tony_ser_url, files = {"tony_form_name": temp_result});
    if test_response.ok:
      print("upload completed")
      print(test_response.text)
    else:
      print("something wrong. go finf tony")

    return

schedule.every().day.at("01:00").do(job,"Uploaded")

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
