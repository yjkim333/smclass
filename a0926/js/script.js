//1.ajax를 활용한 데이터 가져오기
  //제이쿼리 선언
  let count=1;
  let id_num;
  let total;
  let avg;
  let temp = 0;//수정버튼 확인
  let tr_this;
  $(function(){
    //ajax선언
    $.ajax({
      url:"js/stuData.json",
      type:"get",
      data:"",
      dataType:"json",
      
      success:function(data){
        //console.log(data);
        
        //데이터가져오기 버튼 이벤트
        $(document).on("click","#dataBtn",function(){
          let stu_data = "";
          for(var i=0;i<data.length;i++){
            total = data[i].kor + data[i].eng + data[i].math;
            avg = (total/3).toFixed(2); //toFixed()
            stu_data +=`<tr id='${data[i].no}'>`
            stu_data +=`<td>${data[i].no}</td>`
            stu_data +=`<td>${data[i].name}</td>`
            stu_data +=`<td>${data[i].kor}</td>`
            stu_data +=`<td>${data[i].eng}</td>`
            stu_data +=`<td>${data[i].math}</td>`
            stu_data +=`<td>${total}</td>`
            stu_data +=`<td>${avg}</td>`
            stu_data +=`<td><button id='updateBtn'>수정</button><button id='delBtn'>삭제</button></td>>`
            stu_data +=`</tr>`
            count++;
            //console.log(count);
          }
          $("#tbody").html(stu_data);
        });
        
        //삭제버튼 이벤트
        $(document).on("click","#delBtn",function(){
          id_num = $(this).closest("tr").attr("id");
          if(confirm(id_num + "번 학생의 성적정보를 삭제하시겠습니까?")){
            $("#"+id_num).remove();
            alert("정보가 삭제되었습니다.");
          }
        });

        //성적입력버튼 이벤트
        $(document).on("click","#create",function(){
          
          //input 입력 데이터
          //번호:count
          let name = $("#name").val();  //value-js, val-jquery
          let kor = Number($("#kor").val());
          let eng = Number($("#eng").val());
          let math = Number($("#math").val());
          total = kor+eng+math;
          avg = (total/3).toFixed(2);
          //console.log(name,kor,eng,math,total,avg);

          //input 입력된 데이터가 있는지 확인
          if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
            alert("내용을 모두 입력하세요.");
            return false;
          }

          alert("성적 정보를 저장합니다.");

          //표를 만들어서 추가
          let stu_data = "";
          stu_data +=`<tr id='${count}'>`
          stu_data +=`<td>${count}</td>`
          stu_data +=`<td>${name}</td>`
          stu_data +=`<td>${kor}</td>`
          stu_data +=`<td>${eng}</td>`
          stu_data +=`<td>${math}</td>`
          stu_data +=`<td>${total}</td>`
          stu_data +=`<td>${avg}</td>`
          stu_data +=`<td><button id='updateBtn'>수정</button><button id='delBtn'>삭제</button></td>>`
          stu_data +=`</tr>`
          
          $("#tbody").prepend(stu_data);

          //버튼 클릭 후 input 내용 삭제
          $("#name").val("");
          $("#kor").val("");
          $("#eng").val("");
          $("#math").val("");
        });

        //수정 버튼 이벤트
        $(document).on("click","#updateBtn",function(){
          //수정버튼이 클릭이 되어있는지 확인
          if(temp==1){
            alert("수정완료 또는 수정 취소 버튼을 먼저 클릭하세요.");
            return false;
          }
          if(confirm("정보를 수정하시겠습니까?")){

            $(this).css({"color":"gray","font-weight":"600"});
            tr_this=$(this)

            id_num=$(this).closest("tr").attr("id");
            $("#create,#update,#updateCancel").toggle();
            temp=1;
            //데이터 input 창에 넣기
            let u_data = $(this).closest("tr");
            console.log(u_data.children("td:eq(1)").text());
            console.log(u_data.children("td:eq(2)").text());
            console.log(u_data.children("td:eq(3)").text());
            console.log(u_data.children("td:eq(4)").text());

            $("#name").val(u_data.children("td:eq(1)").text());
            $("#kor").val(u_data.children("td:eq(2)").text());
            $("#eng").val(u_data.children("td:eq(3)").text());
            $("#math").val(u_data.children("td:eq(4)").text());;
            
          }
        });

        //수정 완료 이벤트
        $(document).on("click","#update",function(){
          $(tr_this).css({"color":"black","font-weight":"400"});
          
          //input에 입력된 데이터 가져오기
          let name = $("#name").val();
          let kor = Number($("#kor").val());
          let eng = Number($("#eng").val());
          let math = Number($("#math").val());
          console.log(math);
          total = kor+eng+math;
          avg = (total/3).toFixed(2);

          //input에 입력된 데이터가 있는지 확인
          if(name=="" || kor=="" || eng=="" || math==""){
            alert("모든 정보를 입력하세요.");
            return false;
          }

          //테이블을 만들어서 수정 데이터 넣기
          let stu_data = "";
          stu_data +=`<td>${id_num}</td>`
          stu_data +=`<td>${name}</td>`
          stu_data +=`<td>${kor}</td>`
          stu_data +=`<td>${eng}</td>`
          stu_data +=`<td>${math}</td>`
          stu_data +=`<td>${total}</td>`
          stu_data +=`<td>${avg}</td>`
          stu_data +=`<td><button id='updateBtn'>수정</button><button id='delBtn'>삭제</button></td>>`
          console.log(id_num);
          $("#"+id_num).html(stu_data);
 
          //input 창 안에 있는 데이터지우기
          $("#name").val("");  //value-js, val-jquery
          $("#kor").val("");
          $("#eng").val("");
          $("#math").val("");  
          
          alert("성적 수정이 완료되었습니다.");

          $("#create,#update,#updateCancel").toggle();
          temp=0;
          
        });

        //수정취소버튼 이벤트
        $(document).on("click","#updateCancel",function(){
          alert("수정 취소합니다.");
          $(tr_this).css({"color":"black","font-weight":"400"});

          //input 창 안에 있는 데이터지우기
          $("#name").val("");  //value-js, val-jquery
          $("#kor").val("");
          $("#eng").val("");
          $("#math").val("");

          $("#create,#update,#updateCancel").toggle();
          temp=0;

        });

      },
      error:function(){
        alert("Fail..")
      }
    });//ajax
  });//제이쿼리
