import asyncio
import SQLite3_tool
import user_interface

async def mds():
    loop_active = True
    while (loop_active == True):
        print("________________________")
        print("My Diary Space")
        print("________________________")
        print("Choose action:")
        print("1 - Zadej si storku")
        print("2 - ")
        print("3 - ")
        print("4 - ")
        print("5 - ")
        print("6 - Turn-off My Diary Space")

        action = int(input("What can I do for you? Put your number of action 1 - 6:\n"))
        match action:
            case 1:
                texts = ["Note name", "Note txtint"]
                note_name = user_interface.get_input_from_user(texts[0])
                note = int(user_interface.get_input_from_user(texts[1]))
                db_tool = SQLite3_tool
                # */*/ Napriklad zde jde zmenit datovy tip z plosne funkce inputu
                db_tool.insert_to_diarybase(note_name,note)

            case 6:
                loop_active = False
                print("Evidence ending while 5 sec!\nHave a nice day. :)")
                await asyncio.sleep(5)

asyncio.run(mds())