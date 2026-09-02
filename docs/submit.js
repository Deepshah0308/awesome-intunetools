// Turns the submission form into a pre-filled GitHub issue. No backend, no
// third-party form service, and no data leaves the page until the person
// chooses to open GitHub.
(function () {
  var REPO = 'https://github.com/Deepshah0308/awesome-intunetools';
  var form = document.getElementById('submitForm');
  if (!form) return;

  var required = ['tool_name', 'tool_url', 'author', 'category', 'description'];

  function setError(id, show) {
    var el = document.getElementById('err_' + id);
    if (el) el.hidden = !show;
    var input = document.getElementById(id);
    if (input) input.setAttribute('aria-invalid', show ? 'true' : 'false');
  }

  function validUrl(v) {
    try {
      var u = new URL(v);
      return u.protocol === 'https:' || u.protocol === 'http:';
    } catch (err) {
      return false;
    }
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    var values = {};
    var firstBad = null;

    required.forEach(function (id) {
      var v = (document.getElementById(id).value || '').trim();
      values[id] = v;
      var bad = !v || (id === 'tool_url' && !validUrl(v));
      setError(id, bad);
      if (bad && !firstBad) firstBad = id;
    });

    values.kind = document.getElementById('kind').value;
    values.notes = (document.getElementById('notes').value || '').trim();

    if (firstBad) {
      document.getElementById(firstBad).focus();
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
