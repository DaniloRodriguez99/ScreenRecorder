// features/counterSlice.js
import { createSlice } from '@reduxjs/toolkit';
import io from 'socket.io-client';
import { RecordSettingsModel } from '../../5-crossCuttingConcerns/models/RecordSettingsModel';
import { useSelector } from 'react-redux';

const initialState = {
    recordSocket: null,
    isRecording: false,
    recordSettings: new RecordSettingsModel(),
    serverStatus: 'offline'
  };

export const mainSlice = createSlice({
    name: 'main',
    initialState,
    reducers: {
      setRecordSocket: (state, action) => {
        state.recordSocket = action.payload;
      },
      onRecording: (state, action) => {
        state.isRecording = action.payload;
      },
      setRecordSettings: (state, action) => {
        state.recordSettings = action.payload;
      },
    },
  });

export const { setRecordSocket, onRecording, setRecordSettings } = mainSlice.actions;

// Thunk para inicializar el socket
export const initializeSocket = () => (dispatch: any) => {
    const socket = io('http://localhost:5000');
    
    
    socket.on('connect', () => {

      console.log("Conectandose al servidor....")

      socket.on('record_start', (output: boolean) => {
        dispatch(onRecording(output))
      });
  
      socket.on('record_cancel', (isCancelled: boolean) => {
        if(isCancelled) {
          dispatch(onRecording(false))
        }
      });
  
      socket.on('record_end', (isStopped: boolean) => {
        if(isStopped) {
          dispatch(onRecording(!isStopped))
        }
      });
      
      socket.on('getRecordSettings', (output: string) => {
        let mappedResponse: RecordSettingsModel = JSON.parse(output)
        dispatch(setRecordSettings(mappedResponse));
      });

      console.log("Conectado")

    })

    socket.on('disconnect', function() {
      console.log('Desconectado del servidor');
      
      // Intenta reconectarte después de un retraso
      setTimeout(() => {
        console.log('Tratando de conectar');
        socket.connect();
      }, 5000);  // Intenta cada 5 segundos, por ejemplo
    });

    
    dispatch(setRecordSocket(socket));
};


export const startRecord = (settings: RecordSettingsModel) => (dispatch: any, getState: any) => {
  const { main: { recordSocket } } = getState();

  if (recordSocket) {
    dispatch(onRecording(true))
    recordSocket.emit('record_start', JSON.stringify(settings));
  } else {
      console.error('Socket no inicializado');
  }
}

export const cancelRecord = () => (dispatch: any, getState: any) => {
  const { main: { recordSocket } } = getState();

  if (recordSocket) {
    recordSocket.emit('record_cancel');
  } else {
      console.error('Socket no inicializado');
  }
}

export const getRecordSettings = () => (dispatch: any, getState: any) => {
  const { main: { recordSocket } } = getState();

  if (recordSocket) {
    recordSocket.emit('getRecordSettings');
  } else {
    console.error('Socket no inicializado');
  }
}
  

export default mainSlice.reducer;
