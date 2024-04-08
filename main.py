

# Application Default credentials are automatically created.
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta
import pandas as pd
import sys

#Firebase Cert
PATH_TO_CERT = "serviceAccount2.json"
#Firebase Database Name
COLLECTION_NAME = "bookings"
#+8 GMT for Singapore
time_zone = timedelta(hours=8)

def booking_to_html(file_path, docs):
    headers = ["Date", "Start Time", "End Time", "Activity", "Venue", "Pax", "Logistics"]
    data = [headers]
    activity = "Practice"
    venue = "Music Room 2"
    pax = 6
    logs = "nil"
    for doc in docs:
        doc_values = doc.to_dict()
        date = (doc_values["start"] + time_zone).date().strftime("%d/%m/%y")
        start = (doc_values["start"] + time_zone).time().strftime("%H:%M")
        end = (doc_values["end"] + time_zone).time().strftime("%H:%M")
        row = [date, start, end, activity, venue, pax, logs]
        data.append(row)

    df = pd.DataFrame(data[1:], columns=data[0])
    #df.to_csv(file_path,)
    df.to_html(file_path, index=False)

def get_weekly_docs(db, start_date, end_date):
    return db.collection("bookings").where("start" ,">=", start_date).where("start", "<=", end_date).get()

if __name__ == "__main__":
    start_date_text = sys.argv[1]
    end_date_text = sys.argv[2]
    start_filter_date = datetime.strptime(start_date_text, '%d/%m/%y') - time_zone
    end_filter_date = datetime.strptime(end_date_text, '%d/%m/%y') - time_zone + timedelta(hours=23)

    # Use a service account.
    cred = credentials.Certificate(PATH_TO_CERT)
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    docs = get_weekly_docs(db, start_filter_date,end_filter_date)
    booking_to_html("results.html", docs)
