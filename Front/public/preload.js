const { ipcRenderer } = require('electron');

process.once('loaded', () => {
    console.log('Preload script is loaded');
    window.ipcRenderer = ipcRenderer;
});
