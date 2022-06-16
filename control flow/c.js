
var egs = 0
var chees = 0

var report = "blank"

if (egs>=10 && chees >=10){
    report = "sTRONG SALES OF BOTH EGS AND CHEES"
}else if (egs===0 && chees ===0){
    report="Nothing Sold"
}else{
    report="We had some Sales of items"
}
console.log(report)