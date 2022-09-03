//ใช้ร่วมกับ html นะ


//สุ่มหัวก้อยแบบแสดงผลออกมาว่าถูกไหม

let round = prompt("คุณจะเล่นทั้งหมดกี่รอบ ?")
for(var i = 0 ; i < round ; i++){
    var answer = prompt("คุณคิดว่าเป็นหัว หรือ ก้อย")
    var random_answer = ""
    if(Math.floor(Math.random()*10) <= 4){
        //อันนี้หัว
        //*10 แสดงว่าเอาสุ่ม 0-9  *11 คือเอา 0-10
        random_answer = "หัว"
    }
    else{
        //อันนี้ก้อย
        random_answer = "ก้อย"
    }
    
    if(answer == random_answer){
        alert("ถูกต้องงง")
    }
    else{
        alert("ผิดดด")
    }
    console.log(random_answer+ " : " + answer)
}
