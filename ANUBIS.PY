import wolframalpha
import pyautogui
pyautogui.alert("ANUBIS uses WolfRam|Alpha for functioning.Click ok to continue.")
spam = pyautogui.prompt("Write question here:") 
f_o_r = 1
##question=raw_input()

app_id="VH4PQ6-U2KA6H32J8"
client =wolframalpha.Client(app_id)
res=client.query(spam)
answer = next(res.results).text

pyautogui.alert(answer)







