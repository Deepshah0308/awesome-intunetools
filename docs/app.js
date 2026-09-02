// Filters the tools that are already in the document. Nothing is rendered here,
// so the page works fully without JavaScript and stays crawlable.
(function () {
  var q = document.getElementById('q');
  var tally = document.getElementById('tally');
  var empty = document.getElementById('empty');
  var reset = document.getElementById('reset');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('.cat'));
  var tools = Array.prototype.slice.call(document.querySelectorAll('.tool'));
  var total = tools.length;
  var cat = 'all';

  function apply() {
    var term = q.value.trim().toLowerCase();
    var shown = 0;
    tools.forEach(function (el) {
      var okCat = cat === 'all' || el.dataset.cat === cat;
      var okText = !term || el.dataset.text.indexOf(term) !== -1;
      var show = okCat && okText;
      el.hidden = !show;
      if (show) shown++;
    });
    sections.forEach(function (s) {
      var live = s.querySelectorAll('.tool:not([hidden])').length;
      s.hidden = live === 0;
      var c = s.querySelector('.count');
      if (c) c.textContent = live;
    });
    empty.hidden = shown !== 0;
    if (shown === total) {
      tally.textContent = 'Showing all ' + total + ' tools';
    } else if (shown === 1) {
      tally.textContent = '1 tool matches';
    } else {
      tally.textContent = shown + ' of ' + total + ' tools match';
    }
  }

  var timer;
  q.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(apply, 90);
  });

  chips.forEach(function (btn) {
    btn.addEventListener('click', function () {
      chips.forEach(function (b) {
        b.classList.remove('on');
        b.setAttribute('aria-pressed', 'false');
      });
      btn.classList.add('on');
      btn.setAttribute('aria-pressed', 'true');
      cat = btn.dataset.filter;
      apply();
    });
  });

  reset.addEventListener('click', function () {
    q.value = '';
    cat = 'all';
    chips.forEach(function (b) { b.classList.toggle('on', b.dataset.filter === 'all'); });
    apply();
    q.focus();
  });

  function fromHash() {
    var id = location.hash.replace('#', '');
    var match = chips.filter(function (b) { return b.dataset.filter === id; })[0];
    if (match) match.click();
  }
  window.addEventListener('hashchange', fromHash);

  chips.forEach(function (b) { b.setAttribute('aria-pressed', b.classList.contains('on')); });
  apply();
})();
