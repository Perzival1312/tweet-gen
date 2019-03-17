const data = document.getElementById('sentence-array');
const arr = document.getElementById('sentence-array').innerText;
arrs = arr.slice(1, arr.length-1)
splitArr = arrs.split(', ')
retStr = ""
for(let i=0; i<splitArr.length; i+=2) {
    splitArr[i] = '<h1>'+splitArr[i]+'\t-'+localStorage[splitArr[i+1].slice(1, -1)]+'<hr /></h1>'
    retStr += splitArr[i]
}
data.innerHTML = retStr
