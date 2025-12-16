const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

let player = { x: 100, y: 200 };

function draw() {
    ctx.clearRect(0,0,800,500);
    ctx.fillStyle='blue';
    ctx.fillRect(player.x, player.y, 30, 30);
    requestAnimationFrame(draw);
}

draw();

document.addEventListener('keydown', e => {
    if(e.key==='w') player.y -= 10;
    if(e.key==='s') player.y += 10;
    if(e.key==='a') player.x -= 10;
    if(e.key==='d') player.x += 10;
});
