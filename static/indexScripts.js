const body = document.getElementsByTagName('body')[0];
const all = document.getElementsByTagName("*");
let sourceName = document.getElementById('source-for-selector').defaultValue;
let beginSliceInd = sourceName.indexOf('/');
let endSliceIndex = sourceName.indexOf('.');
sourceName  = sourceName.slice(beginSliceInd+1, endSliceIndex);
const mySelect = document.getElementById('source-selector');
// sets correct value to dropdown menu
for(let i, j = 0; i = mySelect.options[j]; j++) {
    if(i.value == sourceName) {
        mySelect.selectedIndex = j;
        for(let k=0; k<all.length; k++){
            body.classList.add(sourceName)
        }
        break;
    }
}
// gets the conversion table for titles so that they are "readable"
let conversionObj = {}
for(let i=0; i<mySelect.options.length; i++){
    conversionObj = Object.assign(conversionObj, {[mySelect.options[i].value]: mySelect.options[i].text})
    localStorage[mySelect.options[i].value] =  mySelect.options[i].text
}
