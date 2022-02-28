from datetime import datetime, timedelta

def strip_date():

    # datetime_object = datetime.strptime(fridayDate, '%m/%d')
    day = datetime.today()
    friday = day + timedelta(days=day.weekday()) + timedelta(days=4, weeks=0)
    # print(datetime_object)
    return friday

def generate_la(dt_obj):
    mon = dt_obj - timedelta(days=4)
    tue = dt_obj - timedelta(days=3)
    print(str(mon.month)+"/"+str(mon.day)+" 9am - 10:00am Mentor Meeting")
    print(str(tue.month)+"/"+str(tue.day)+" 10:20am - 11:40am Recitation")
    print(str(tue.month)+"/"+str(tue.day)+" 5:40pm - 07:00pm Recitation")
    print("1 hour prep")
    return

dt = strip_date()
generate_la(dt)