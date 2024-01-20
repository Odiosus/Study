
document.addEventListener('DOMContentLoaded', () => {

    const buttons = document.querySelectorAll('.btn');
    const activebutid = window.sessionStorage.getItem('activebutton');

    let lastactive = activebutid
        ? document.getElementById(activebutid)
        : null;

    lastactive?.classList.add('active');

    function clickhandler() {

        lastactive?.classList.remove('active');
        window.sessionStorage.removeItem('activeaCont');
        window.sessionStorage.setItem('activebutton', this.id);
    }

    for (const but of buttons) {
        but.addEventListener('click', clickhandler);
    }

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
