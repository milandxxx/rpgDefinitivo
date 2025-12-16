fetch('/quests')
    .then(res => res.json())
    .then(data => {
        let div = document.getElementById('quests');
        data.forEach(q => {
            div.innerHTML += <div><b></b></div>;
        });
    });
