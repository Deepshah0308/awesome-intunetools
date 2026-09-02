// Submission form: validates in-browser, mirrors input into a live preview of
// the directory card, then opens a pre-filled GitHub issue. No backend, and no
// data leaves the page until the person chooses to open GitHub.
(function () {
  var REPO = 'https://github.com/Deepshah0308/awesome-intunetools';
  var form = document.getElementById('submitForm');
  if (!form) return;

  var KIND_LABEL = { repo: 'Open source', web: 'Hosted tool', guide: 'Guide' };
  var required = ['tool_name', 'tool_url', 'author', 'category', 'description'];
  var $ = function (id) { return document.getElementById(id); };

  function validUrl(v) {
    try {
      var u = new URL(v);
      return u.protocol === 'https:' || u.protocol === 'http:';
    } catch (err) { return false; }
  }

  function setError(id, show) {
    var msg = $('err_' + id);
    if (msg) msg.hidden = !show;
    var input = $(id);
    if (!input) return;
    input.setAttribute('aria-invalid', show ? 'true' : 'false');
    var field = input.closest('.field');
    if (field) field.classList.toggle('field-invalid', show);
  }

  // ---- live preview -------------------------------------------------------
  function host(v) {
    try { return new URL(v).hostname.replace(/^www\./, ''); }
    catch (err) { return 'example.com'; }
  }

  function paint() {
    $('pv_name').textContent = $('tool_name').value.trim() || 'Your tool name';
    $('pv_author').textContent = $('author').value.trim() || 'Author';
    $('pv_desc').textContent = $('description').value.trim() ||
      'A one-sentence description of what problem it solves will appear here as you type.';
    var kind = $('kind').value;
    var badge = $('pv_kind');
    badge.textContent = KIND_LABEL[kind] || 'Open source';
    badge.className = 'kind kind-' + kind;
    $('pv_src').textContent = host($('tool_url').value.trim());
  }

  function counter(id) {
    var el = $(id), out = $('count_' + id);
    if (!el || !out) return;
    var sync = function () { out.textContent = el.value.length; };
    el.addEventListener('input', sync);
    sync();
  }

  ['tool_name', 'author', 'description', 'tool_url'].forEach(function (id) {
    $(id).addEventListener('input', paint);
  });
  $('kind').addEventListener('change', paint);
  counter('description');
  counter('notes');
  paint();

  // clear an error as soon as the person starts fixing it
  required.forEach(function (id) {
    $(id).addEventListener('input', function () { setError(id, false); });
    $(id).addEventListener('change', function () { setError(id, false); });
  });

  // ---- submit -------------------------------------------------------------
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    var values = {};
    var firstBad = null;

    required.forEach(function (id) {
      var v = ($(id).value || '').trim();
      values[id] = v;
      var bad = !v || (id === 'tool_url' && !validUrl(v));
      setError(id, bad);
      if (bad && !firstBad) firstBad = id;
    });

    values.kind = $('kind').value;
    values.notes = ($('notes').value || '').trim();

    if (firstBad) {
      $(firstBad).focus();
      return;
    }

    var params = new URLSearchParams({
      template: 'tool-submission.yml',
      labels: 'tool submission',
      title: 'Tool submission: ' + values.tool_name,
      tool_name: values.tool_name,
      tool_url: values.tool_url,
      author: values.author,
      category: values.category,
      kind: values.kind,
      description: values.description
    });
    if (values.notes) params.set('notes', values.notes);

    window.open(REPO + '/issues/new?' + params.toString(), '_blank', 'noopener');
  });
})();
