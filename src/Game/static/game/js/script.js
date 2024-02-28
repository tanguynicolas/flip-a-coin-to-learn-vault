let heads = 0;
let tails = 0;
let coin = document.querySelector('.coin');
let flipBtn = document.getElementById('flip-button');
let resetBtn = document.getElementById('reset-button');

async function updateStats(){
    heads = await (await fetch('/heads/', { method: 'GET' })).text();
    tails = await (await fetch('/tails/', { method: 'GET' })).text();
}

function updateStatsOnPage(){
    document.getElementById('heads-count').textContent = `Face : ${heads}`;
    document.getElementById('tails-count').textContent = `Pile : ${tails}`;
}

function disableButton() {
    flipBtn.disabled = true;
    setTimeout(()=>{
        flipBtn.disabled = false;
    }, 3000);
}

flipBtn.addEventListener("click", async ()=>{
    let i = Math.floor(Math.random() * 2);
    coin.style.animation = "none";
    if (i) {
        setTimeout(()=>{
            coin.style.animation = "spin-heads 3s forwards";
        }, 100);
        await (await fetch('/heads/', { method: 'POST' })).text();
    }else{
        setTimeout(()=>{
            coin.style.animation = "spin-tails 3s forwards";
        }, 100);
        await (await fetch('/tails/', { method: 'POST' })).text();
    }
    updateStats();
    setTimeout(updateStatsOnPage, 3000);
    disableButton();
});

resetBtn.addEventListener("click", ()=>{
    coin.style.animation = "none";

    // Reset the counters in the database via API & on page
    fetch('/reset/', { method: 'POST' });
    updateStats();
    updateStatsOnPage();
});
