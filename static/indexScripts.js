let sourceName = document.getElementById('source-for-selector').defaultValue.slice(8, -5);
const mySelect = document.getElementById('source-selector');

for(let i, j = 0; i = mySelect.options[j]; j++) {
    if(i.value == sourceName) {
        mySelect.selectedIndex = j;
        break;
    }
}