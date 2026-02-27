const translateBtn = document.getElementById('translateBtn');
const btnText      = document.getElementById('btnText');
const spinner      = document.getElementById('spinner');
const inputText    = document.getElementById('inputText');
const sourceLang   = document.getElementById('sourceLang');
const targetLang   = document.getElementById('targetLang');
const resultCard   = document.getElementById('resultCard');
const errorCard    = document.getElementById('errorCard');
const inputResult  = document.getElementById('inputResult');
const outputResult = document.getElementById('outputResult');
const errorMsg     = document.getElementById('errorMsg');
const srcLabel     = document.getElementById('srcLabel');
const tgtLabel     = document.getElementById('tgtLabel');

function showError(msg) {
  errorMsg.textContent = msg;
  errorCard.classList.add('visible');
  resultCard.classList.remove('visible');
}

function hideMessages() {
  errorCard.classList.remove('visible');
  resultCard.classList.remove('visible');
}

function setLoading(val) {
  translateBtn.disabled = val;
  spinner.classList.toggle('active', val);
  btnText.textContent = val ? 'Translating...' : 'Translate';
}

async function doTranslate() {
  hideMessages();

  const text = inputText.value.trim();
  const src  = sourceLang.value;
  const tgt  = targetLang.value;

  if (!text) return showError('Please enter some text to translate.');
  if (!tgt)  return showError('Please select a target language.');

  setLoading(true);
  try {
    const res = await fetch('/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, source_lang: src, target_lang: tgt }),
    });

    const data = await res.json();

    if (data.error) {
      showError(data.error);
    } else {
      srcLabel.textContent     = data.source;
      tgtLabel.textContent     = data.target;
      inputResult.textContent  = data.input;
      outputResult.textContent = data.translation;
      resultCard.classList.add('visible');
    }
  } catch (err) {
    showError('Network error. Make sure the server is running.');
  } finally {
    setLoading(false);
  }
}

translateBtn.addEventListener('click', doTranslate);

inputText.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.key === 'Enter') doTranslate();
});

inputText.addEventListener('input', hideMessages);
targetLang.addEventListener('change', hideMessages);
