const API = 'http://127.0.0.1:5000';

function savePlayer(data){
 fetch(API+'/save',{
   method:'POST',
   headers:{'Content-Type':'application/json'},
   body:JSON.stringify(data)
 });
}
