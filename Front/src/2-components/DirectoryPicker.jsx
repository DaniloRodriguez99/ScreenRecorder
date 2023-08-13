import Button, { ButtonProps } from '@mui/material/Button';
import React, { useEffect, useState } from 'react';


export default function DirectoryPicker() {
    const [selectedDir, setSelectedDir] = useState('');

    useEffect(() => {
      if (window.ipcRenderer) {
        window.ipcRenderer.on('directory-selected', (event, path) => {
          setSelectedDir(path);
        });
    
        return () => {
          window.ipcRenderer.removeAllListeners('directory-selected');
        }
      }
    }, []);
    
  
    const handleDirectoryPicker = () => {
      if (window.ipcRenderer) {
        window.ipcRenderer.send('open-directory-dialog');
      }
    }

  return (
    <div>
    <Button variant="contained" color="primary" component="span" onClick={handleDirectoryPicker}>
      Seleccionar Directorio
    </Button>
      <p>Directorio seleccionado: { "No implementado aun " }</p>
    </div>
  );
}
