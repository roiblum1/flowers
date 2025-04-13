onload = () => {
    document.body.classList.remove("container");
    
    // Add some additional animation for the blessing text
    setTimeout(() => {
        const blessingText = document.querySelector('.blessing-text');
        if (blessingText) {
            blessingText.style.fontSize = '28px';
            setTimeout(() => {
                blessingText.style.fontSize = '24px';
            }, 300);
        }
    }, 1500);
};