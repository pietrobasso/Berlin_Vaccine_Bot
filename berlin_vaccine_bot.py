import requests
import webbrowser
import json
import time
from datetime import datetime, timedelta, date
import asyncio
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class Doctor:
  name: str
  requestUrl: str
  pageUrl: str


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
}
loop = 0
waitingTime = 30
doctors = [
  Doctor(
    "GKH",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-07&visit_motive_ids=2806956&agenda_ids=469719&insurance_sector=public&practice_ids=162056&limit=3",
    "https://www.doctolib.de/krankenhaus/berlin/gkh-havelhoehe-impfzentrum"
  ),
  Doctor(
    "Arena",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457727-457733-457739-457742-457745-457726-457725-457728-457730-457736-457743-457729-457732-457738-457744-457734-457737-457740-457731&insurance_sector=public&practice_ids=158431&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158431"
  ),
  Doctor(
    "Messe",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457549-457532-457533-457597-457566-457531-457558-457591-457594-457567-457593-457554-457556-457563-457569-457536-457543-457596-457529-457530&insurance_sector=public&practice_ids=158434&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158434"
  ),
  Doctor(
    "Erika",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=457976-457928-457927-457930-457917-457939-457975-457964-457970-457907-457924-457971-457912-457916-457922-457967-457933-457940-457968-457963-457973-457931-457915-457918-457938-457935-457979-457966-457926-457941-457937-457951-457952-457954-457947-457977-457923&insurance_sector=public&practice_ids=158437&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158437"
  ),
  Doctor(
    "Velo",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457195-457211-457201-457991-457205-457193&insurance_sector=public&practice_ids=158435&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158435"
  ),
  Doctor(
    "Tegel Pfizer",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457250&insurance_sector=public&practice_ids=158436&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158436"
  ),
  Doctor(
    "Tegel Moderna",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=465555&insurance_sector=public&practice_ids=191612&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-191612"
  ),
  Doctor(
    "Tempelhof",
    "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=467906-481913-481915-481920-481917-467934-467937-467938-467939-467910-467908-467903-467907-467935-467936-467893-467895-467896-467900-467901-467905-467911-467897-467898-467912-467940-481914-481916-481919-481921-467894-467933-467899&insurance_sector=public&practice_ids=191611&destroy_temporary=true&limit=4",
    "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-191611"
  )
]
goalDate = date.today() + timedelta(days=14)
print("Looking for slots. Goal date:", goalDate)


def earlierThanGoalDate(data):
  if "next_slot" in data:
    slotTime = datetime.strptime(data["next_slot"], "%Y-%m-%d")
    return slotTime.date() < goalDate
  else:
    return False


def fetch(session, doctor):
  with session.get(doctor.requestUrl, headers=headers) as response:
    data = json.loads(response.text)
    if earlierThanGoalDate(data):
      webbrowser.open_new_tab(doctor.pageUrl)
      print("Found slot at", doctor.name, "on", data["next_slot"], "🚀")
      time.sleep(waitingTime)
    else:
        pass
    return response.text


async def get_data_asynchronous():
  with ThreadPoolExecutor(max_workers=10) as executor:
    with requests.Session() as session:
      loop = asyncio.get_event_loop()
      tasks = [
        loop.run_in_executor(
          executor,
          fetch,
          # Allows us to pass in multiple arguments to `fetch`
          *(session, doctor)
        )
        for doctor in doctors
      ]
      for response in await asyncio.gather(*tasks):
          pass


def main():
  loop = asyncio.get_event_loop()
  future = asyncio.ensure_future(get_data_asynchronous())
  loop.run_until_complete(future)


while loop == 0:
  main()
