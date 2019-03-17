let sourceName = document.getElementById('source-for-selector').defaultValue;
let beginSliceInd = sourceName.indexOf('/');
let endSliceIndex = sourceName.indexOf('.');
sourceName  = sourceName.slice(beginSliceInd+1, endSliceIndex);
const mySelect = document.getElementById('source-selector');

for(let i, j = 0; i = mySelect.options[j]; j++) {
    if(i.value == sourceName) {
        mySelect.selectedIndex = j;
        break;
    }
}