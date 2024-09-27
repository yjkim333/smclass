//jquery
$(function(){

  $("#searchBtn").click(function(){
    alert("검색 버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=Y%2BduMd7L0jpQJx4Q09xs0zpRg0z3FvIYfWQVMCwtC%2BEY33tNGgPCV8ehJtjvLj4dCCOS6koa0w%2Fw6W7qksNz4w%3D%3D&numOfRows=10&pageNo=1&MobileOS=ET&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        alert("성공");
        let p_data = "";
        let id = data.response.body.items.item
        console.log(id);
        for(var i=0;i<id.length;i++){
        p_data +=`<tr id=''>`
        p_data +=`<td>${id[i].galContentId}</td>`
        p_data +=`<td>${id[i].galTitle}</td>`
        p_data +=`<td>${id[i].galPhotographer}</td>`
        p_data +=`<td>${id[i].galModifiedtime}</td>`
        p_data +=`<td><img src="${id[i].galWebImageUrl}"></td>`
        p_data +=`</tr'>`
        }
        $("#tbody").html(p_data);
      },
      error:function(){
        alert("Fail..");
      }
      
    });//ajax
  });//searchBtn
});//jquery