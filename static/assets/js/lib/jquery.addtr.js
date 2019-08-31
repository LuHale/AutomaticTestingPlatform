
　　function addTr(){

　　　　var tb=document.getElementById("table1");

　　　　var newTr=tb.insertRow(2);//表示在第二行后添加一行

　　　　var newTd=newTr.insertCell();//表示在添加的行上添加第一格

　　　　newTd.innerHTML="邮箱:";

　　　　var newTd2=newTr.insertCell();//表示在添加的行上添加第二格

　　　　newTd.innerHTML="<input type='text' name='email' />";

　　}

