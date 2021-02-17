
//Format number of last column.
var formatter = new Intl.NumberFormat('en-US', {
    style: 'decimal',
    maximumFractionDigits: '2'
});
  
x = document.getElementsByTagName('td');

for (let i = 0; i < x.length; i++) {
    i+=2;
    x[i].innerHTML = formatter.format(x[i].innerHTML);
}
  

  