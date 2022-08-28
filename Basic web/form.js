
"555" === 555

console.log("Hello World")
var height = 200;
const Nickname = "MaMa";
const ismale = false;
var money = null;
let bigNumber = 10n

console.log(height,Nickname,ismale,money,bigNumber);

const person = {
      name : "Zania",
      age : 17,
      height : 162,
      weight : 60,
      bf : true
}
person.name = "Zaniasocool" //ใส่แทนได้จาก person.name อันแรกได้
person.city = "Bangkok" //ใส่เพิ่มได้ตลอด เหมือนเราเพิ่มข้อมูลให้ person เฉย ๆ

console.log(person.name,person.age);

const animals = ["Fish","Cat","Dog"]
console.log(animals)
console.log(animals[1])

animals.push("Tiger")//ใส่ตัวเพิ่มไปด้านหลังสุด
console.log(animals)

animals.pop()//เอาตัวที่อยู่หลังสุดออก
console.log(animals)

animals.unshift("Duck")//เพิ่มตัวไว้ด้านหน้าสุด(ค่าที่0)
console.log(animals)

animals.shift()//ลบตัวหน้าสุด
console.log(animals)