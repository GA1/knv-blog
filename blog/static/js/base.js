var headerHeight = document.getElementById('page-header').offsetHeight;
var header = document.getElementById('page-header')
header.style.marginTop = -headerHeight

var contentHeight = document.getElementById('content-div').offsetHeight;
var content = document.getElementById('content-div');
content.style.marginTop = headerHeight;