//自作関数
function sumAry(ary1, ary2, ary3){
  var i, result = [];
  for (i = 0; i < ary1.length; i++){
    result[i] = [Number(ary1[i]) + Number(ary2[i]) + Number(ary3[i])];
    if(ary1[i+1]==""){
        break;
    }
  }
  return result;
}
