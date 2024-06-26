
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
                <div class="d-flex flex-column ml-2"><span class="font-weight-bold">@Nick</span><span class="day">1 day ago</span></div>
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
  
  
  
