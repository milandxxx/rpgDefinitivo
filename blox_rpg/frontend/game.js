const API = 'http://127.0.0.1:5000';
let token = '';
let player = {x:100,y:100,hp:100,fruit:null};

function register(){
fetch(API+'/register',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({username:user.value,password:pass.value})
})
}

function login(){
fetch(API+'/login',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({username:user.value,password:pass.value})
})
.then(r=>r.json())
.then(d=>{
token=d.token;
loginDiv.style.display='none';
gameUI.style.display='block';
});
}

function getFruit(){
fetch(API+'/fruit',{
method:'POST',
headers:{'Authorization':'Bearer '+token}
})
.then(r=>r.json())
.then(d=>{
player.fruit=d.fruit;
hud.innerText='Fruta: '+player.fruit;
});
}

const canvas=document.getElementById('game');
const ctx=canvas.getContext('2d');

function loop(){
ctx.clearRect(0,0,800,500);
ctx.fillStyle='blue';
ctx.fillRect(player.x,player.y,30,30);
requestAnimationFrame(loop);
}
loop();

document.addEventListener('keydown',e=>{
if(e.key==='w')player.y-=5;
if(e.key==='s')player.y+=5;
if(e.key==='a')player.x-=5;
if(e.key==='d')player.x+=5;
});
