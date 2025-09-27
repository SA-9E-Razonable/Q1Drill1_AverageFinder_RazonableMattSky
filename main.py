from pyscript import document

def compute_average(event):
	score1 = float(document.getElementById("score1").value)
	score2 = float(document.getElementById("score2").value)

	average = (score1 + score2) / 2

	if score1 > 100 or score2 > 100 or score1 < 0 or score2 < 0:
		document.getElementById("result").innerText = "Score must be 0-100!"
		return
	
	if average == 100:
		result = "got perfect 💯"
	elif average >=75:
		result = "passed 🔥"
	else:
		result = "are cooked 👹"

	document.getElementById("result").innerText = f"Average: {average}. You {result}!"