const data = document.getElementById('sentence-array');
const arr = document.getElementById('sentence-array').innerText;
arrs = arr.slice(1, arr.length-1)
splitArr = arrs.split(', ')
retStr = ""
for(let i=0; i<splitArr.length; i++) {
    splitArr[i] = '<h1>'+splitArr[i]+'<hr /></h1>'
    retStr += splitArr[i]
}
data.innerHTML = retStr
