let player = {
  level: 1,
  sea: 1,
  hp: 100,
  stamina: 100,
  beli: 0,
  fragments: 0
};

function updateHUD(){
  document.getElementById('level').innerText = 'Lv. ' + player.level;
  document.getElementById('sea').innerText = 'Sea ' + player.sea;
  document.getElementById('hp').innerText = 'HP: ' + player.hp;
  document.getElementById('stamina').innerText = 'STA: ' + player.stamina;
  document.getElementById('beli').innerText = 'Beli: ' + player.beli;
  document.getElementById('fragments').innerText = 'Fragments: ' + player.fragments;
}

function loadQuests(){
  document.getElementById('content').innerHTML = 
    <h2>Quests</h2>
    <button onclick='completeQuest()'>Completar Quest</button>
  ;
}

function completeQuest(){
  player.level += 1;
  player.beli += 500;
  updateHUD();
}

function rollFruit(){
  document.getElementById('content').innerHTML = 
    <h2>Fruta obtenida</h2>
    <p>🔥 Flame Fruit</p>
  ;
}

function startRaid(){
  player.fragments += 100;
  updateHUD();
  document.getElementById('content').innerHTML = 
    <h2>Raid completada</h2>
    <p>+100 Fragments</p>
  ;
}

function openInventory(){
  document.getElementById('content').innerHTML = 
    <h2>Inventario</h2>
    <p>Espadas, frutas, items aquí</p>
  ;
}

updateHUD();
