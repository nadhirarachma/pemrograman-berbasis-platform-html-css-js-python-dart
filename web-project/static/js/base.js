// get all the stars
// let one = document.getElementById("first")
// let two = document.getElementById('second')
// let three = document.getElementById('third')
// let four = document.getElementById('fourth')
// let five = document.getElementById('fifth')

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

// const form = document.querySelector('.rate-form')
// const confirmBox = document.getElementById('confirm-box')
// const csrf = document.getElementsByName('csrfmiddlewaretoken')

// const handleStarSelect = (size) => {
//     const children = form.children
//     for (let i=0; i< children.length; i++){
//         if (i <= size){
//             children[i].classList.add('checked')
//         }
//         else{
//             children[i].classList.remove('checked')
//         }
//     }
// }
// console.log(one)

// // longer version to be optimized
// const handleSelect = (selection) => {
//     switch(selection){
//         case 'first':{
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
        //     handleStarSelect(1)
        //     return
        // }
        // case 'second':{
            // one.classList.add('checked')
            // two.classList.add('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
        //     handleStarSelect(2)
        //     return
        // }
        // case 'third':{
            // one.classList.add('checked')
            // two.classList.add('checked')
            // three.classList.add('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
        //     handleStarSelect(3)
        //     return
        // }
        // case 'fourth':{
            // one.classList.add('checked')
            // two.classList.add('checked')
            // three.classList.add('checked')
            // four.classList.add('checked')
            // five.classList.remove('checked')
        //     handleStarSelect(4)
        //     return
        // }
        // case 'fifth':{
            // one.classList.add('checked')
            // two.classList.add('checked')
            // three.classList.add('checked')
            // four.classList.add('checked')
            // five.classList.add('checked')
//             handleStarSelect(5)
//             return
//         }
        
//     }

// }
// const getNumericValue = (stringValue) =>{
//     let numericValue;
//     if (stringValue === 'first'){
//         numericValue = 1

//     }
//     else if (stringValue === 'second'){
//         numericValue = 2
//     }
//     else if (stringValue === 'third'){
//         numericValue = 3
//     }
//     else if (stringValue === 'fourth'){
//         numericValue = 4
//     }
//     else if (stringValue === 'fifth'){
//         numericValue = 5
//     }
//     else{
//         numericValue = 0
//     }
//     return numericValue
// }

// if (one){
//     const arr = [one, two, three, four, five]
    
//     arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
//         handleSelect(event.target.id)
//     }))
    
//     arr.forEach(item => item.addEventListener('click', (event)=>{
//         const val = event.target.id
//         console.log(val)
        
//         form.addEventListener('submit', e=>{
//             e.preventDefault()
//             const id = e.target.id
//             console.log(id)
//             const val_num = getNumericValue(val)

//             $.ajax({
//                 type: 'POST',
//                 url: '/healthy_advice/rate_anu',
//                 data: {
//                     'csrfmiddlewaretoken' : csrf[0].value,
//                     'el_id' : id,
//                     'val' : val_num,
//                 },
//                 success: function(response){
//                     console.log(response)
//                     confirmBox.innerHTML = '<h1>Thank you for your feedback😊 $(response.score)</h1>'
//                 },
//                 error: function(error){
//                     console.error(error);
//                     confirmBox.innerHTML = '<h1>MASIH SALAH YA ALLAH PUSYANG😊 </h1>'
//                 }
//             })
//         })
//     }))
// }


const getMessageData = () => {
    return $(document).ready(function(){
              $.ajax({
                  url: "/healthy_advice/get_all_comment", 
                  success: function(results){
                      results.map((result)=>{
                        insertTableData(result);
                      }
                    )
                  }
                }
              );
            }
          );
  }
  const insertTableData = (result) => {
    return $("#kartu-comment").append(`
    <div class="d-flex flex-row align-items-center add-comment p-2 bg-white rounded"><img class="rounded-circle" src="https://i.imgur.com/QvDFBCC.jpg" width="40"><input type="text" class="form-control border-0 no-box-shadow ml-1" placeholder="Leave a constructive comment..."></div>
    <div class="p-3 bg-white mt-2 rounded">
        <div class="d-flex justify-content-between">
            <div class="d-flex flex-row user"><img class="rounded-circle img-fluid img-responsive" src="https://i.imgur.com/Yxje2El.jpg" width="40">
                <div class="d-flex flex-column ml-2"><span class="font-weight-bold">@Nick</span><span class="day"></span></div>
            </div>
            <div class="d-flex align-items-center px-3 heart border"><i class="fa fa-heart heart-icon"></i><span class="ml-2">35</span></div>
        </div>
        <div class="comment-text text-justify mt-2">
            <p>${result.fields.comment_field}</p>
        </div>
    </div>
    <div class="p-3 bg-white mt-2 rounded">
        <div class="d-flex justify-content-between">
            <div class="d-flex flex-row user"><img class="rounded-circle img-fluid img-responsive" src="https://i.imgur.com/JXZLwEY.jpg" width="40">
                <div class="d-flex flex-column ml-2"><span class="font-weight-bold">@Samantha</span><span class="day">2 days ago</span></div>
            </div>
            <div class="d-flex align-items-center px-3 heart border"><i class="fa fa-heart-o heart-icon"></i><span class="ml-2">35</span></div>
        </div>
        <div class="comment-text text-justify mt-2">
            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
        </div>
        <div class="d-flex justify-content-end align-items-center comment-buttons mt-2 text-right"><span class="mr-3 delete">Delete</span><button class="btn btn-success btn-sm border-0 px-3" type="button">Edit</button></div>
    </div>`)
  }
  getMessageData();
  
  
  
