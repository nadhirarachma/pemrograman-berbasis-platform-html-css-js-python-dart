// get all the stars
let one = document.getElementById("first")
let two = document.getElementById('second')
let three = document.getElementById('third')
let four = document.getElementById('fourth')
let five = document.getElementById('fifth')

// form.map((f)=>{
//     f.map((element)=>{
//         console.log(element)
//         let one = document.getElementById("first")
//         let two = document.getElementById('second')
//         let three = document.getElementById('third')
//         let four = document.getElementById('fourth')
//         let five = document.getElementById('fifth')
//         const arr = [one, two, three, four, five]
//         arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
//             handleSelect(event.target.id)
//         }))
//     })
// })

const form = document.querySelectorAll('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
    const children = form.children
    console.log(children)
}
handleStarSelect(4)

console.log(one)

// longer version to be optimized
const handleSelect = (selection) => {
    switch(selection){
        case 'first':{
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'second':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'third':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }
        case 'fourth':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return
        }
        case 'fifth':{
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return
        }
        
    }

}

const arr = [one, two, three, four, five]

arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
    handleSelect(event.target.id)
}))