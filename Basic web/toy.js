function cal(){
    const items = document.getElementById("items").value //ตอนนี้ค่าของ("item")เป็นสตริงอยู่
    const price = document.getElementById("price").value
let result = 0 
for(let i = 1 ; i <= Number(items); i++) 
{result += Number (price)}
   
document.getElementById("result").innerHTML = result
}
