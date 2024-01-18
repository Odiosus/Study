

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn');
    const activebutid = window.sessionStorage.getItem('activebutton');
    const aConts = document.querySelectorAll('.aCont');
    const activeAId = window.sessionStorage.getItem('activeaCont');

    let lastactive = activebutid
        ? document.getElementById(activebutid)
        : null;

    let lastactive1 = activeAId
        ? document.getElementById(activeAId)
        : null;

    lastactive?.classList.add('active');

    function clickhandler() {
        lastactive?.classList.remove('active');
        lastactive1?.classList.remove('activea');
        this.classList.add('active');
        window.sessionStorage.setItem('activebutton', this.id);
        window.sessionStorage.setItem('activeaCont', this.id);
    }

    for (const but of buttons) {
        but.addEventListener('click', clickhandler);
    }

});


document.addEventListener('DOMContentLoaded', () => {
    const aConts = document.querySelectorAll('.aCont');
    const activeAId = window.sessionStorage.getItem('activeaCont');

    let lastactive1 = activeAId
        ? document.getElementById(activeAId)
        : null;

    lastactive1?.classList.add('activea');

    function clickhandler1() {
        lastactive1?.classList.remove('activea');
        this.classList.add('activea');
        window.sessionStorage.setItem('activeaCont', this.id);
    }

    for (const aC of aConts) {
        aC.addEventListener('click', clickhandler1);
    }

});

document.getElementById('delbN').onclick = function(e){
  window.sessionStorage.removeItem('activebutton', this.id);
}