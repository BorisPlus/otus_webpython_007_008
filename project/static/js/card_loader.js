class Card {
    static showFullCard(id) {
        var fullCard = document.getElementById(this.id+'_full_card');
        fullCard.style.display = 'block';
    }
    static hideFullCard(id) {
        var fullCard = document.getElementById(this.id);
        fullCard.style.display = 'none';
    }
}

autoLoad = function() {
    var cards = document.getElementsByClassName("card");
    var i;
    for (i = 0; i < cards.length; i++) {
        cards[i].onclick = Card.showFullCard;
    }
    var fullCards = document.getElementsByClassName("full_card");
    for (i = 0; i < fullCards.length; i++) {
        fullCards[i].onclick = Card.hideFullCard;
    }
};

if (window.addEventListener) // W3C standard
{
  window.addEventListener('load', autoLoad, false); // NB **not** 'onload'
}
else if (window.attachEvent) // Microsoft
{
  window.attachEvent('onload', autoLoad);
}
