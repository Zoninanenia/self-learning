let score = Number(prompt("Type your score here 💝"))

if (score >= 80 && score <= 100)
{document.getElementById("score").innerHTML = "A"}

else if (score >= 70 && score < 80)
{document.getElementById("score").innerHTML = "B"}

else if (score >= 60 && score < 70)
{document.getElementById("score").innerHTML = "C"}

else if (score >= 50 && score < 60)
{document.getElementById("score").innerHTML = "D"}

else if (score < 50 && score >= 0)
{document.getElementById("score").innerHTML = "F"}

else
{document.getElementById("score").innerHTML = "Invalid score ,Please refresh and try again."}