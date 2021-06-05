import requests
import webbrowser
import json
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
loop=0
print("looking for slots")
while loop == 0:
    arena=requests.get("https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457727-457733-457739-457742-457745-457726-457725-457728-457730-457736-457743-457729-457732-457738-457744-457734-457737-457740-457731&insurance_sector=public&practice_ids=158431&destroy_temporary=true&limit=4", headers=headers)
    messe = requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457549-457532-457533-457597-457566-457531-457558-457591-457594-457567-457593-457554-457556-457563-457569-457536-457543-457596-457529-457530&insurance_sector=public&practice_ids=158434&destroy_temporary=true&limit=4", headers=headers)
    erika=requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=457976-457928-457927-457930-457917-457939-457975-457964-457970-457907-457924-457971-457912-457916-457922-457967-457933-457940-457968-457963-457973-457931-457915-457918-457938-457935-457979-457966-457926-457941-457937-457951-457952-457954-457947-457977-457923&insurance_sector=public&practice_ids=158437&destroy_temporary=true&limit=4", headers=headers)
    velo=requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457195-457211-457201-457991-457205-457193&insurance_sector=public&practice_ids=158435&destroy_temporary=true&limit=4", headers=headers)
    tegelp=requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2495719&agenda_ids=457250&insurance_sector=public&practice_ids=158436&destroy_temporary=true&limit=4", headers=headers)
    tegelm=requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=465555&insurance_sector=public&practice_ids=191612&destroy_temporary=true&limit=4", headers=headers)
    templ=requests.get(
        "https://www.doctolib.de/availabilities.json?start_date=2021-06-05&visit_motive_ids=2537716&agenda_ids=467906-481913-481915-481920-481917-467934-467937-467938-467939-467910-467908-467903-467907-467935-467936-467893-467895-467896-467900-467901-467905-467911-467897-467898-467912-467940-481914-481916-481919-481921-467894-467933-467899&insurance_sector=public&practice_ids=191611&destroy_temporary=true&limit=4", headers=headers)
    json_data_arena = json.loads(arena.text)
    json_data_messe = json.loads(messe.text)
    json_data_erika = json.loads(erika.text)
    json_data_velo = json.loads(velo.text)
    json_data_tegelp = json.loads(tegelp.text)
    json_data_tegelm = json.loads(tegelm.text)
    json_data_templ = json.loads(templ.text)

    #arena_total = json_data_arena["total"]
    #messe_total = json_data_arena["total"]
    #erika_total = json_data_arena["total"]
    #velo_total = json_data_arena["total"]
    #tegelp_total = json_data_arena["total"]
    #tegelm_total = json_data_arena["total"]
    #templ_total = json_data_arena["total"]

    arena_avlb = json_data_arena["availabilities"]
    messe_avlb = json_data_messe["availabilities"]
    erika_avlb = json_data_erika["availabilities"]
    velo_avlb = json_data_velo["availabilities"]
    tegelp_avlb = json_data_tegelp["availabilities"]
    tegelm_avlb = json_data_tegelm["availabilities"]
    templ_avlb = json_data_templ["availabilities"]

    if len(arena_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158431")
            print(arena.text)
            print(len(arena_avlb))
            print ("found slot - arena")
            time.sleep(30)
    else:
            print(arena.text)
            print(len(arena_avlb))
    if len(messe_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158434")
            print(messe.text)
            print(len(messe_avlb))
            print("found slot - messe")
            time.sleep(30)
    else:
            print(messe.text)
            print(len(messe_avlb))
    if len(erika_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158437")
            print(erika.text)
            print(len(erika_avlb))
            print("found slot - erika")
            time.sleep(30)
    else:
            print(erika.text)
            print(len(erika_avlb))
    if len(velo_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158435")
            print(velo.text)
            print(len(velo_avlb))
            print("found slot - velo")
            time.sleep(30)
    else:
            print(velo.text)
            print(len(velo_avlb))
    if len(tegelp_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158436")
            print(tegelp.text)
            print(len(tegelp_avlb))
            print("found slot - tegel-pf")
            time.sleep(30)
    else:
            print(tegelp.text)
            print(len(tegelp_avlb))
    if len(tegelm_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-191612")
            print(tegelm.text)
            print(len(tegelm_avlb))
            print("found slot - tegel-md")
            time.sleep(30)
    else:
            print(tegelm.text)
            print(len(tegelm_avlb))
    if len(templ_avlb)!=0:
            webbrowser.open_new_tab("https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-191611")
            print(templ.text)
            print(len(templ_avlb))
            print("found slot - templ")
            time.sleep(30)
    else:
            print(templ.text)
            print(len(templ_avlb))
    #print("looking for slots")
    #time.sleep(0.5)

