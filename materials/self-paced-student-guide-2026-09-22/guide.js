for (const prompt of document.querySelectorAll('.prompt')) {
  const button = document.createElement('button');
  button.type = 'button'; button.className = 'copy'; button.textContent = 'Copy request';
  button.addEventListener('click', async () => {
    const text = [...prompt.querySelectorAll('p,li')].map(el => el.textContent).join('\n');
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(text);
      button.textContent = 'Copied';
      document.getElementById('copy-status').textContent = 'Request copied. Paste it into Copilot or a chat interface.';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(prompt);
      range.setEndBefore(button);
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      button.textContent = 'Select the request and copy';
      document.getElementById('copy-status').textContent = 'Automatic copying is unavailable. Select the request text and use Copy.';
    }
    setTimeout(() => { button.textContent = 'Copy request'; }, 3500);
  });
  prompt.append(button);
}
function markCurrent() {
  for (const link of document.querySelectorAll('nav a')) {
    if (link.hash && link.hash === window.location.hash) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}
window.addEventListener('hashchange', markCurrent); markCurrent();
const navigation = document.querySelector('.nav-toggle');
if (navigation && window.matchMedia) {
  const narrow = window.matchMedia('(max-width: 850px)');
  const adaptNavigation = () => { navigation.open = !narrow.matches; };
  adaptNavigation(); narrow.addEventListener('change', adaptNavigation);
}
const printButton = document.querySelector('[data-print]');
if (printButton) printButton.addEventListener('click', () => window.print());
if (location.protocol !== 'file:') {
  const download = document.createElement('a');
  download.className = 'button secondary'; download.href = 'student-guide.zip';
  download.download = ''; download.textContent = 'Download the whole guide';
  document.getElementById('download-actions')?.prepend(download);
}
let closedDetails = [];
window.addEventListener('beforeprint', () => {
  closedDetails = [...document.querySelectorAll('main details:not([open])')];
  closedDetails.forEach(el => { el.open = true; });
});
window.addEventListener('afterprint', () => closedDetails.forEach(el => { el.open = false; }));
