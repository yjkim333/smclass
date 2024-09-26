//jquery
let num=0;
let num2=0;
$(function(){

  //우측버튼
  $("#right").click(function(){
    //alert("우측버튼 클릭");
    num += 100;
    num2 += 360;
    if(num>=900){
      alert("stop click!!");
      return false;
    }
    $("#box").animate({
      left:num,rotate:num2+"deg"
    },1000);
    $("#box").stop();
  });

  //좌측버튼
  $("#left").click(function(){
    //alert("좌측버튼 클릭");
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left:num, rotate:num2+"deg"
    },1000);
    if(num<=0){
      alert("더 이상 못감");
      return false;
    }
    $("#box").stop();
  });

});//jquery